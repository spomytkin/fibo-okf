---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: driver's license
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an official document which states that a person may operate a motorized vehicle, such as a motorcycle, car, truck
      or a bus, on a public roadway or provides official identifying information for a non-driver
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://en.wikipedia.org/wiki/Non-driver_identification_card#Non-driver_identification_cards
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: driving licence
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicenseIdentifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/IdentityDocument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IdentityDocument
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicense
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: driver's license
type: Ontology Class
---

# driver's license

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicense>

## Definition

an official document which states that a person may operate a motorized vehicle, such as a motorcycle, car, truck or a bus, on a public roadway or provides official identifying information for a non-driver

## Relationships

- **Subclass of**: [IdentityDocument](/concepts/fibo/FND/AgentsAndPeople/People/IdentityDocument.md)

## Constraints

- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: exact qualified cardinality 1 of type [DriversLicenseIdentifier](/concepts/fibo/FND/AgentsAndPeople/People/DriversLicenseIdentifier.md)

## Annotations

- **label**: driver's license
- **definition**: an official document which states that a person may operate a motorized vehicle, such as a motorcycle, car, truck or a bus, on a public roadway or provides official identifying information for a non-driver
- **adaptedFrom**: https://en.wikipedia.org/wiki/Non-driver_identification_card#Non-driver_identification_cards
- **synonym**: driving licence

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
