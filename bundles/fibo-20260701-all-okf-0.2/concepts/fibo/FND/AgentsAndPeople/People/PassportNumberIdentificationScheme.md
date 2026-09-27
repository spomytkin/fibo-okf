---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: passport number identification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system for allocating identifiers to passports
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Schemes for passport identification are jurisdiction-specific by country.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PassportNumber
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PassportNumberIdentificationScheme
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: passport number identification scheme
type: Ontology Class
---

# passport number identification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PassportNumberIdentificationScheme>

## Definition

system for allocating identifiers to passports

## Relationships

- **Subclass of**: [IdentificationScheme](<https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [PassportNumber](/concepts/fibo/FND/AgentsAndPeople/People/PassportNumber.md)

## Annotations

- **label**: passport number identification scheme
- **definition**: system for allocating identifiers to passports
- **explanatoryNote**: Schemes for passport identification are jurisdiction-specific by country.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
