---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: person
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: individual human being, with consciousness of self
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: natural person
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Locations/Country
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasCitizenship
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DateOfBirth
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasDateOfBirth
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DateOfDeath
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasDateOfDeath
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasGender
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PlaceOfBirth
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPlaceOfBirth
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasResidence
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Age
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAge
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PersonName
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasName
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: person
type: Ontology Class
---

# person

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person>

## Definition

individual human being, with consciousness of self

## Relationships

- **Subclass of**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)

## Constraints

- **[hasCitizenship](/concepts/fibo/FND/AgentsAndPeople/People/hasCitizenship.md)**: min qualified cardinality 0 of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[hasDateOfBirth](/concepts/fibo/FND/AgentsAndPeople/People/hasDateOfBirth.md)**: exact qualified cardinality 1 of type [DateOfBirth](/concepts/fibo/FND/AgentsAndPeople/People/DateOfBirth.md)
- **[hasDateOfDeath](/concepts/fibo/FND/AgentsAndPeople/People/hasDateOfDeath.md)**: min qualified cardinality 0 of type [DateOfDeath](/concepts/fibo/FND/AgentsAndPeople/People/DateOfDeath.md)
- **[hasGender](/concepts/fibo/FND/AgentsAndPeople/People/hasGender.md)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasPlaceOfBirth](/concepts/fibo/FND/AgentsAndPeople/People/hasPlaceOfBirth.md)**: exact qualified cardinality 1 of type [PlaceOfBirth](/concepts/fibo/FND/AgentsAndPeople/People/PlaceOfBirth.md)
- **[hasResidence](/concepts/fibo/FND/AgentsAndPeople/People/hasResidence.md)**: min qualified cardinality 0 of type [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)
- **[hasAge](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAge.md)**: min qualified cardinality 0 of type [Age](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Age.md)
- **[hasName](<https://www.omg.org/spec/Commons/Designators/hasName>)**: min qualified cardinality 0 of type [PersonName](/concepts/fibo/FND/AgentsAndPeople/People/PersonName.md)

## Annotations

- **label** (en): person
- **definition**: individual human being, with consciousness of self
- **synonym**: natural person

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
