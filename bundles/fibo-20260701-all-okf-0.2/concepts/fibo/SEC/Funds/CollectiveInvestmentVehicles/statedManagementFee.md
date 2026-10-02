---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: stated management fee
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'The fee that is stated in the Prospectus as being what is to be charged for management. Further notes: Can be
      monetary amount or a percentage or a combination. Action: simple type is wrong.'
  domain:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/Prospectus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/Prospectus
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/statedManagementFee
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: stated management fee
type: Ontology Property
---

# stated management fee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/statedManagementFee>

## Definition

The fee that is stated in the Prospectus as being what is to be charged for management. Further notes: Can be monetary amount or a percentage or a combination. Action: simple type is wrong.

## Relationships

- **Domain**: [Prospectus](/concepts/fibo/SEC/Securities/SecuritiesIssuance/Prospectus.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label** (en): stated management fee
- **definition** (en): The fee that is stated in the Prospectus as being what is to be charged for management. Further notes: Can be monetary amount or a percentage or a combination. Action: simple type is wrong.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
