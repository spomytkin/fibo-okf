---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: identity document
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any legal document which may be used to verify aspects of a person's identity
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://en.wikipedia.org/wiki/Identification_card
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If issued in the form of a small, mostly standard-sized card, it is usually called an identity card (IC). Countries
      which do not have formal identity documents may require informal documents. In the absence of a formal identity document,
      driving licenses can be used in many countries as a method of proof of identity, although some countries do not accept
      driving licenses for identification, often because in those countries they don't expire as documents and can be old
      and easily forged. Most countries accept passports as a form of identification. Most countries have the rule that foreign
      citizens need to have their passport or occasionally a national identity card from their country available at any time
      if they do not have residence permit in the country.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: identity card
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DateOfBirth
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidenceFor
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidenceFor
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PlaceOfBirth
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidenceFor
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasExpirationDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Government
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDateOfIssuance
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Identifiers/Identifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/LegalDocument
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IdentityDocument
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: identity document
type: Ontology Class
---

# identity document

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IdentityDocument>

## Definition

any legal document which may be used to verify aspects of a person's identity

## Relationships

- **Subclass of**: [LegalDocument](<https://www.omg.org/spec/Commons/Documents/LegalDocument>)

## Constraints

- **[isEvidenceFor](/concepts/fibo/FND/Agreements/Contracts/isEvidenceFor.md)**: exact qualified cardinality 1 of type [DateOfBirth](/concepts/fibo/FND/AgentsAndPeople/People/DateOfBirth.md)
- **[isEvidenceFor](/concepts/fibo/FND/Agreements/Contracts/isEvidenceFor.md)**: max qualified cardinality 1 of type [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)
- **[isEvidenceFor](/concepts/fibo/FND/Agreements/Contracts/isEvidenceFor.md)**: min qualified cardinality 0 of type [PlaceOfBirth](/concepts/fibo/FND/AgentsAndPeople/People/PlaceOfBirth.md)
- **[hasExpirationDate](/concepts/fibo/FND/Arrangements/Documents/hasExpirationDate.md)**: exact qualified cardinality 1 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: exact qualified cardinality 1 of type [Government](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Government.md)
- **[hasDateOfIssuance](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDateOfIssuance>)**: exact qualified cardinality 1 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from of type [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: exact qualified cardinality 1 of type [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Annotations

- **label**: identity document
- **definition**: any legal document which may be used to verify aspects of a person's identity
- **adaptedFrom**: https://en.wikipedia.org/wiki/Identification_card
- **explanatoryNote**: If issued in the form of a small, mostly standard-sized card, it is usually called an identity card (IC). Countries which do not have formal identity documents may require informal documents. In the absence of a formal identity document, driving licenses can be used in many countries as a method of proof of identity, although some countries do not accept driving licenses for identification, often because in those countries they don't expire as documents and can be old and easily forged. Most countries accept passports as a form of identification. Most countries have the rule that foreign citizens need to have their passport or occasionally a national identity card from their country available at any time if they do not have residence permit in the country.
- **synonym**: identity card

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
