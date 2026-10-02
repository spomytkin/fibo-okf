---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: driver's license identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier associated with a drivers' or operating license for operating a motor vehicle or non-driver identification
      card
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: driver's license number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicenseIdentificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicense
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicenseIdentifier
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: driver's license identifier
type: Ontology Class
---

# driver's license identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicenseIdentifier>

## Definition

identifier associated with a drivers' or operating license for operating a motor vehicle or non-driver identification card

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [DriversLicenseIdentificationScheme](/concepts/fibo/FND/AgentsAndPeople/People/DriversLicenseIdentificationScheme.md)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [DriversLicense](/concepts/fibo/FND/AgentsAndPeople/People/DriversLicense.md)

## Annotations

- **label**: driver's license identifier
- **definition**: identifier associated with a drivers' or operating license for operating a motor vehicle or non-driver identification card
- **synonym**: driver's license number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
