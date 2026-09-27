---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: driver's license identification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system for allocating identifiers to driver's, operating, or non-driver identification documents
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Schemes for driver's license identification are typically regionally defined, and there may be jurisdiction-specific
      scope required as an additional restriction on a specific scheme.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicenseIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicenseIdentificationScheme
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: driver's license identification scheme
type: Ontology Class
---

# driver's license identification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicenseIdentificationScheme>

## Definition

system for allocating identifiers to driver's, operating, or non-driver identification documents

## Relationships

- **Subclass of**: [IdentificationScheme](<https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [DriversLicenseIdentifier](/concepts/fibo/FND/AgentsAndPeople/People/DriversLicenseIdentifier.md)

## Annotations

- **label**: driver's license identification scheme
- **definition**: system for allocating identifiers to driver's, operating, or non-driver identification documents
- **explanatoryNote**: Schemes for driver's license identification are typically regionally defined, and there may be jurisdiction-specific scope required as an additional restriction on a specific scheme.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
