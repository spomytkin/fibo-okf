---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issue price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The price at which the Fund Unit was first issued.
  domain:
  - concept: /concepts/fibo/SEC/Funds/Funds/FundUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Price.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Price
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/issuePrice
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: issue price
type: Ontology Property
---

# issue price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/issuePrice>

## Definition

The price at which the Fund Unit was first issued.

## Relationships

- **Domain**: [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)
- **Range**: [Price](/concepts/fibo/FND/Accounting/CurrencyAmount/Price.md)

## Annotations

- **label** (en): issue price
- **definition** (en): The price at which the Fund Unit was first issued.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
