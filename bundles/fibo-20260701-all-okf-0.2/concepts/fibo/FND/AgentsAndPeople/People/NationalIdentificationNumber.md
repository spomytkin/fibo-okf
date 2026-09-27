---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: national identification number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: number or text which appears on an identity document issued by a country or jurisdiction
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://en.wikipedia.org/wiki/National_identification_number
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'A national identification number, national identity number, or national insurance number is used by the governments
      of many countries as a means of tracking their citizens, permanent residents, and temporary residents for the purposes
      of work, taxation, government benefits, health care, and other governmentally-related functions. The number will appear
      on an identity document issued by a country.


      The ways in which such a system is implemented are dependent on the country, but in most cases, a citizen is issued
      an identification number at birth or when they reach a legal age (typically the age of 18). Non-citizens may be issued
      such numbers when they enter the country, or when granted a temporary or permanent residence permit.


      Many countries issued such numbers ostensibly for a singular purpose, but over time, they become a de facto national
      identification number. For example, the United States originally developed its Social Security number system as a means
      of disbursing Social Security benefits. However, due to function creep, the number has become utilized for other purposes
      to the point where it is almost essential to have one to, among other things, open a bank account, obtain a credit card,
      or drive a car.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: national identity number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Government
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/NationalIdentificationNumberScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/NationalIdentificationNumber
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: national identification number
type: Ontology Class
---

# national identification number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/NationalIdentificationNumber>

## Definition

number or text which appears on an identity document issued by a country or jurisdiction

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: exact qualified cardinality 1 of type [Government](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Government.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [NationalIdentificationNumberScheme](/concepts/fibo/FND/AgentsAndPeople/People/NationalIdentificationNumberScheme.md)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)

## Annotations

- **label**: national identification number
- **definition**: number or text which appears on an identity document issued by a country or jurisdiction
- **adaptedFrom**: http://en.wikipedia.org/wiki/National_identification_number
- **explanatoryNote**: A national identification number, national identity number, or national insurance number is used by the governments of many countries as a means of tracking their citizens, permanent residents, and temporary residents for the purposes of work, taxation, government benefits, health care, and other governmentally-related functions. The number will appear on an identity document issued by a country.  The ways in which such a system is implemented are dependent on the country, but in most cases, a citizen is issued an identification number at birth or when they reach a legal age (typically the age of 18). Non-citizens may be issued such numbers when they enter the country, or when granted a temporary or permanent residence permit.  Many countries issued such numbers ostensibly for a singular purpose, but over time, they become a de facto national identification number. For example, the United States originally developed its Social Security number system as a means of disbursing Social Security benefits. However, due to function creep, the number has become utilized for other purposes to the point where it is almost essential to have one to, among other things, open a bank account, obtain a credit card, or drive a car.
- **synonym**: national identity number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
