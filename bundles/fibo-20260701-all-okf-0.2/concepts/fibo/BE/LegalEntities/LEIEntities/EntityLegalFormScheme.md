---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: entity legal form scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: scheme that specifies the elements of the codes for entity legal forms, such as those that are sanctioned in a
      given jurisdiction as defined in ISO 20725
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/code-lists/iso-20275-entity-legal-forms-code-list
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso.org/obp/ui/#iso:std:iso:20275:ed-1:v1:en
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalFormIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalFormScheme
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: entity legal form scheme
type: Ontology Class
---

# entity legal form scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalFormScheme>

## Definition

scheme that specifies the elements of the codes for entity legal forms, such as those that are sanctioned in a given jurisdiction as defined in ISO 20725

## Relationships

- **Subclass of**: [ClassificationScheme](<https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme>)
- **Subclass of**: [CodeSet](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [EntityLegalFormIdentifier](/concepts/fibo/BE/LegalEntities/LEIEntities/EntityLegalFormIdentifier.md)

## Annotations

- **label**: entity legal form scheme
- **definition**: scheme that specifies the elements of the codes for entity legal forms, such as those that are sanctioned in a given jurisdiction as defined in ISO 20725
- **adaptedFrom**: https://www.gleif.org/en/about-lei/code-lists/iso-20275-entity-legal-forms-code-list
- **adaptedFrom**: https://www.iso.org/obp/ui/#iso:std:iso:20275:ed-1:v1:en

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
