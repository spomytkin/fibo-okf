---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: birth certificate identification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system for allocating identifiers to birth certificates
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Schemes for birth certificate identification are typically regionally defined, and there may be jurisdiction-specific
      scope required as an additional restriction on a specific scheme.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificateIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificateIdentificationScheme
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: birth certificate identification scheme
type: Ontology Class
---

# birth certificate identification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificateIdentificationScheme>

## Definition

system for allocating identifiers to birth certificates

## Relationships

- **Subclass of**: [IdentificationScheme](<https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [BirthCertificateIdentifier](/concepts/fibo/FND/AgentsAndPeople/People/BirthCertificateIdentifier.md)

## Annotations

- **label**: birth certificate identification scheme
- **definition**: system for allocating identifiers to birth certificates
- **explanatoryNote**: Schemes for birth certificate identification are typically regionally defined, and there may be jurisdiction-specific scope required as an additional restriction on a specific scheme.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
