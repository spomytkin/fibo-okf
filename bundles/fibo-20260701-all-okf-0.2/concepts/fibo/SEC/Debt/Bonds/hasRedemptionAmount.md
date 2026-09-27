---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has redemption amount
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the amount of the principal paid with a redemption payment
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/RedemptionPayment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RedemptionPayment
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasRedemptionAmount
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has redemption amount
type: Ontology Property
---

# has redemption amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasRedemptionAmount>

## Definition

indicates the amount of the principal paid with a redemption payment

## Relationships

- **Domain**: [RedemptionPayment](/concepts/fibo/SEC/Debt/Bonds/RedemptionPayment.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label**: has redemption amount
- **definition**: indicates the amount of the principal paid with a redemption payment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
