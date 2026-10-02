"""Build an explicit semantic model from a parsed RDF graph."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

from rdflib import BNode, Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS

from .semantic import Annotation, OntologyEntity, OntologyModel, Relationship, Restriction, SourceFile

ENTITY_TYPE_MAP = {
    OWL.Class: "class",
    RDFS.Class: "class",
    OWL.ObjectProperty: "object_property",
    OWL.DatatypeProperty: "datatype_property",
    OWL.AnnotationProperty: "annotation_property",
    RDF.Property: "property",
    OWL.NamedIndividual: "individual",
    OWL.Ontology: "ontology",
    SKOS.Concept: "concept",
}
PROPERTY_CHARACTERISTICS = {
    OWL.FunctionalProperty: "functional",
    OWL.InverseFunctionalProperty: "inverse_functional",
    OWL.TransitiveProperty: "transitive",
    OWL.SymmetricProperty: "symmetric",
    OWL.AsymmetricProperty: "asymmetric",
    OWL.ReflexiveProperty: "reflexive",
    OWL.IrreflexiveProperty: "irreflexive",
}
RELATIONSHIP_KINDS = {
    RDFS.subClassOf: "subclass_of",
    RDFS.subPropertyOf: "subproperty_of",
    RDFS.domain: "domain",
    RDFS.range: "range",
    OWL.equivalentClass: "equivalent_to",
    OWL.equivalentProperty: "equivalent_to",
    OWL.disjointWith: "disjoint_with",
    OWL.inverseOf: "inverse_of",
    OWL.sameAs: "same_as",
    OWL.differentFrom: "different_from",
    RDFS.seeAlso: "see_also",
    RDFS.isDefinedBy: "defined_by",
}
RESTRICTION_PREDICATES = {
    OWL.cardinality: "exact_cardinality",
    OWL.qualifiedCardinality: "exact_qualified_cardinality",
    OWL.minCardinality: "min_cardinality",
    OWL.minQualifiedCardinality: "min_qualified_cardinality",
    OWL.maxCardinality: "max_cardinality",
    OWL.maxQualifiedCardinality: "max_qualified_cardinality",
    OWL.someValuesFrom: "some_values_from",
    OWL.allValuesFrom: "all_values_from",
    OWL.hasValue: "has_value",
    OWL.hasSelf: "has_self",
}
UNSUPPORTED_PREDICATES = {
    OWL.unionOf: "union_of",
    OWL.intersectionOf: "intersection_of",
    OWL.complementOf: "complement_of",
    OWL.propertyChainAxiom: "property_chain_axiom",
    OWL.hasKey: "has_key",
    OWL.withRestrictions: "datatype_restriction",
    OWL.disjointUnionOf: "disjoint_union_of",
}
ANNOTATION_SKIP_TYPES = set(ENTITY_TYPE_MAP) | set(PROPERTY_CHARACTERISTICS)


def _local_name(iri: URIRef) -> str:
    text = str(iri)
    return text.rsplit("#", 1)[-1].rstrip("/").rsplit("/", 1)[-1]


def _category(types: list[URIRef]) -> str:
    categories = {ENTITY_TYPE_MAP[rdf_type] for rdf_type in types if rdf_type in ENTITY_TYPE_MAP}
    return sorted(categories)[0] if categories else "entity"


def _restriction(graph: Graph, node: BNode) -> Restriction | None:
    if (node, RDF.type, OWL.Restriction) not in graph:
        return None
    property_iri = next(iter(graph.objects(node, OWL.onProperty)), None)
    if not isinstance(property_iri, URIRef):
        return None
    kind = "restriction"
    cardinality = None
    filler = None
    value = None
    for predicate, candidate_kind in RESTRICTION_PREDICATES.items():
        candidate = next(iter(graph.objects(node, predicate)), None)
        if candidate is None:
            continue
        kind = candidate_kind
        if "cardinality" in kind:
            try:
                cardinality = int(str(candidate))
            except ValueError:
                value = str(candidate)
        elif predicate == OWL.hasValue:
            value = str(candidate)
        elif isinstance(candidate, URIRef):
            filler = str(candidate)
        else:
            value = str(candidate)
        break
    if filler is None:
        qualified = next(iter(graph.objects(node, OWL.onClass)), None)
        if qualified is None:
            qualified = next(iter(graph.objects(node, OWL.onDataRange)), None)
        if isinstance(qualified, URIRef):
            filler = str(qualified)
    return Restriction(property=str(property_iri), kind=kind, cardinality=cardinality, filler=filler, value=value)


def build_semantic_model(
    graph: Graph,
    origins: dict[URIRef, set[str]],
    source_files: list[SourceFile],
) -> OntologyModel:
    entities: dict[str, OntologyEntity] = {}
    subjects = sorted({subject for subject in graph.subjects() if isinstance(subject, URIRef)}, key=str)
    for subject in subjects:
        rdf_types = sorted({value for value in graph.objects(subject, RDF.type) if isinstance(value, URIRef)}, key=str)
        category = _category(rdf_types)
        annotation_values = []
        for predicate, value in graph.predicate_objects(subject):
            if isinstance(value, Literal):
                annotation_values.append(Annotation(
                    predicate=str(predicate),
                    value=str(value),
                    language=value.language,
                    datatype=str(value.datatype) if value.datatype else None,
                ))
        has_label = any(
            annotation.predicate in {str(RDFS.label), str(SKOS.prefLabel)}
            for annotation in annotation_values
        )
        if category == "entity" and not has_label:
            continue

        entity = OntologyEntity(
            iri=str(subject),
            kind=category,
            rdf_types=[str(value) for value in rdf_types],
            deprecated=any(
                (subject, OWL.deprecated, value) in graph and str(value).lower() in {"true", "1"}
                for value in graph.objects(subject, OWL.deprecated)
            ),
            source_paths=sorted(origins.get(subject, set())),
        )
        entity.annotations = sorted(
            set(annotation_values),
            key=lambda annotation: (annotation.predicate, annotation.language or "", annotation.value, annotation.datatype or ""),
        )
        for rdf_type in rdf_types:
            if rdf_type in PROPERTY_CHARACTERISTICS:
                entity.characteristics.append(PROPERTY_CHARACTERISTICS[rdf_type])
        for predicate, value in graph.predicate_objects(subject):
            if predicate == RDF.type:
                continue
            if isinstance(value, URIRef):
                entity.relations.append(Relationship(
                    kind=RELATIONSHIP_KINDS.get(predicate, "related_to"),
                    predicate=str(predicate),
                    target=str(value),
                ))
            elif isinstance(value, BNode):
                restriction = _restriction(graph, value)
                if restriction:
                    entity.restrictions.append(restriction)
        entity.relations.sort(key=lambda relation: (relation.kind, relation.predicate, relation.target))
        entity.restrictions.sort(key=lambda item: (item.property, item.kind, item.cardinality or -1, item.filler or "", item.value or ""))
        entity.characteristics = sorted(set(entity.characteristics))
        entities[entity.iri] = entity

    unsupported: Counter[str] = Counter()
    warnings: list[dict[str, str]] = []
    for subject, predicate, _ in graph:
        if predicate in UNSUPPORTED_PREDICATES:
            code = UNSUPPORTED_PREDICATES[predicate]
            unsupported[code] += 1
            warnings.append({"code": f"OWL_{code.upper()}_NOT_PROJECTED", "subject": str(subject)})
        if isinstance(subject, BNode) and (subject, RDF.type, OWL.Restriction) in graph:
            # Recognized restrictions are projected; no loss warning is needed.
            continue
    imports = sorted({str(value) for value in graph.objects(None, OWL.imports) if isinstance(value, URIRef)})
    version_iris = sorted({str(value) for value in graph.objects(None, OWL.versionIRI) if isinstance(value, URIRef)})
    return OntologyModel(
        entities=entities,
        source_files=source_files,
        version_iris=version_iris,
        imports=imports,
        triple_count=len(graph),
        unsupported=unsupported,
        warnings=warnings,
    )
