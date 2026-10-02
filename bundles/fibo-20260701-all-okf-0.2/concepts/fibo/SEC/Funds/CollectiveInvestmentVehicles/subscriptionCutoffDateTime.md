---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: subscription cutoff date time
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Last date/time at which an order to subscribe can be given.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/subscriptionCutoffDateTime
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: subscription cutoff date time
type: Ontology Property
---

# subscription cutoff date time

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/subscriptionCutoffDateTime>

## Definition

Last date/time at which an order to subscribe can be given.

## Relationships

- **Domain**: [FundSubscriptionTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md)
- **Range**: [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)

## Annotations

- **label** (en): subscription cutoff date time
- **definition** (en): Last date/time at which an order to subscribe can be given.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
