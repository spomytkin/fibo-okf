---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: minimum initial subscription amount
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Minimum initial subscription value.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/minimumInitialSubscriptionAmount
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: minimum initial subscription amount
type: Ontology Property
---

# minimum initial subscription amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/minimumInitialSubscriptionAmount>

## Definition

Minimum initial subscription value.

## Relationships

- **Domain**: [FundSubscriptionTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label** (en): minimum initial subscription amount
- **definition** (en): Minimum initial subscription value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
