---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: national identification number scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system for allocating identifiers to national identification numbers
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Schemes for national identification numbers are jurisdiction-specific by country.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/NationalIdentificationNumber
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/NationalIdentificationNumberScheme
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: national identification number scheme
type: Ontology Class
---

# national identification number scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/NationalIdentificationNumberScheme>

## Definition

system for allocating identifiers to national identification numbers

## Relationships

- **Subclass of**: [IdentificationScheme](<https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [NationalIdentificationNumber](/concepts/fibo/FND/AgentsAndPeople/People/NationalIdentificationNumber.md)

## Annotations

- **label**: national identification number scheme
- **definition**: system for allocating identifiers to national identification numbers
- **explanatoryNote**: Schemes for national identification numbers are jurisdiction-specific by country.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
