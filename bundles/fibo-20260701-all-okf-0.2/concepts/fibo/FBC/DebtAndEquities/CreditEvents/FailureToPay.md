---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: failure to pay
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: default event that is triggered following any applicable grace period in which a payment obligation is missed
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/hasGracePeriod
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/DefaultEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/FailureToPay
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: failure to pay
type: Ontology Class
---

# failure to pay

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/FailureToPay>

## Definition

default event that is triggered following any applicable grace period in which a payment obligation is missed

## Relationships

- **Subclass of**: [DefaultEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md)

## Constraints

- **[hasGracePeriod](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/hasGracePeriod.md)**: max qualified cardinality 1 of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label** (en): failure to pay
- **definition** (en): default event that is triggered following any applicable grace period in which a payment obligation is missed

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
