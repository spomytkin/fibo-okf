---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underwriter takedown amount
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Takedown amount of the security handled by the underwriter(that will be brought into DTC).
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/UnderwriterTakedownForDebt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/UnderwriterTakedownForDebt
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/underwriterTakedownAmount
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: underwriter takedown amount
type: Ontology Property
---

# underwriter takedown amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/underwriterTakedownAmount>

## Definition

Takedown amount of the security handled by the underwriter(that will be brought into DTC).

## Relationships

- **Domain**: [UnderwriterTakedownForDebt](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/UnderwriterTakedownForDebt.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label** (en): underwriter takedown amount
- **definition** (en): Takedown amount of the security handled by the underwriter(that will be brought into DTC).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
