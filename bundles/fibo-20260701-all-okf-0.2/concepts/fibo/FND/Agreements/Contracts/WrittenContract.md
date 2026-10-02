---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: written contract
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal contract that is written and signed by the parties thereto
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasCounterparty
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DateTimeStamp
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasEffectiveDateTimeStamp
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasExecutionDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DateTimeStamp
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasExecutionDateTimeStamp
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractPrincipal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasPrincipalParty
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isAssignable
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractDocument
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDateOfIssuance
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: written contract
type: Ontology Class
---

# written contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract>

## Definition

formal contract that is written and signed by the parties thereto

## Relationships

- **Subclass of**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)

## Constraints

- **[hasCounterparty](/concepts/fibo/FND/Agreements/Contracts/hasCounterparty.md)**: some values from of type [Counterparty](/concepts/fibo/FND/Agreements/Contracts/Counterparty.md)
- **[hasEffectiveDateTimeStamp](/concepts/fibo/FND/Agreements/Contracts/hasEffectiveDateTimeStamp.md)**: min qualified cardinality 0 of type [DateTimeStamp](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTimeStamp>)
- **[hasExecutionDate](/concepts/fibo/FND/Agreements/Contracts/hasExecutionDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasExecutionDateTimeStamp](/concepts/fibo/FND/Agreements/Contracts/hasExecutionDateTimeStamp.md)**: min qualified cardinality 0 of type [DateTimeStamp](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTimeStamp>)
- **[hasPrincipalParty](/concepts/fibo/FND/Agreements/Contracts/hasPrincipalParty.md)**: some values from of type [ContractPrincipal](/concepts/fibo/FND/Agreements/Contracts/ContractPrincipal.md)
- **[isAssignable](/concepts/fibo/FND/Agreements/Contracts/isAssignable.md)**: exact qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: some values from of type [ContractDocument](/concepts/fibo/FND/Agreements/Contracts/ContractDocument.md)
- **[hasDateOfIssuance](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDateOfIssuance>)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label**: written contract
- **definition**: formal contract that is written and signed by the parties thereto

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
