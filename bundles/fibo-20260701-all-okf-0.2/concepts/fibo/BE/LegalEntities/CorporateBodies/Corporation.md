---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: corporation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal organization that is a legal entity (artificial person) distinct from its owners, created under the jurisdiction
      of the laws of a state or nation
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'A corporation has three distinguishing characteristics: (1) separation of ownership from management and general
      liability, i.e., its liability to creditors is limited to its resources, unlike some partnerships and sole proprietorships,
      (2) the ability to negotiate contracts and own property, and (3) transferable ownership, irrespective of changes in
      membership or the lifetimes of its stockholders.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A corporation is managed by or under the direction of a board of directors, which generally determines corporate
      policy. Officers manage the day-to-day affairs of the corporation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: body corporate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/InstrumentOfIncorporation
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isConstitutedBy
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isIncorporatedIn
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: corporation
type: Ontology Class
---

# corporation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation>

## Definition

formal organization that is a legal entity (artificial person) distinct from its owners, created under the jurisdiction of the laws of a state or nation

## Relationships

- **Subclass of**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Constraints

- **[isConstitutedBy](/concepts/fibo/BE/LegalEntities/CorporateBodies/isConstitutedBy.md)**: min qualified cardinality 0 of type [InstrumentOfIncorporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/InstrumentOfIncorporation.md)
- **[isIncorporatedIn](/concepts/fibo/BE/LegalEntities/CorporateBodies/isIncorporatedIn.md)**: exact qualified cardinality 1 of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **[hasLegalName](/concepts/fibo/FND/Relations/Relations/hasLegalName.md)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): corporation
- **definition**: formal organization that is a legal entity (artificial person) distinct from its owners, created under the jurisdiction of the laws of a state or nation
- **explanatoryNote**: A corporation has three distinguishing characteristics: (1) separation of ownership from management and general liability, i.e., its liability to creditors is limited to its resources, unlike some partnerships and sole proprietorships, (2) the ability to negotiate contracts and own property, and (3) transferable ownership, irrespective of changes in membership or the lifetimes of its stockholders.
- **explanatoryNote**: A corporation is managed by or under the direction of a board of directors, which generally determines corporate policy. Officers manage the day-to-day affairs of the corporation.
- **synonym**: body corporate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
