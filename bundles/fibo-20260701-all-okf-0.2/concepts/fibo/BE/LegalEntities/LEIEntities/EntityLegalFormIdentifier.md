---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: entity legal form identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: code that denotes an entity legal form as defined in ISO 20275
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/code-lists/iso-20275-entity-legal-forms-code-list
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso.org/obp/ui/#iso:std:iso:20275:ed-1:v1:en
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalForm
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/denotes
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalFormScheme
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalFormIdentifier
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: entity legal form identifier
type: Ontology Class
---

# entity legal form identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalFormIdentifier>

## Definition

code that denotes an entity legal form as defined in ISO 20275

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)

## Constraints

- **[denotes](<https://www.omg.org/spec/Commons/Designators/denotes>)**: exact qualified cardinality 1 of type [EntityLegalForm](/concepts/fibo/BE/LegalEntities/LEIEntities/EntityLegalForm.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [EntityLegalFormScheme](/concepts/fibo/BE/LegalEntities/LEIEntities/EntityLegalFormScheme.md)

## Annotations

- **label**: entity legal form identifier
- **definition**: code that denotes an entity legal form as defined in ISO 20275
- **adaptedFrom**: https://www.gleif.org/en/about-lei/code-lists/iso-20275-entity-legal-forms-code-list
- **adaptedFrom**: https://www.iso.org/obp/ui/#iso:std:iso:20275:ed-1:v1:en

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
