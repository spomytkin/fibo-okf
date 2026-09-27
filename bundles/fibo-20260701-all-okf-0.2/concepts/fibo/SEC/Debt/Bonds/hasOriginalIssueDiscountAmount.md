---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has original issue discount amount
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the difference between the stated redemption price at maturity and the issue price
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
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
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasOriginalIssueDiscountAmount
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has original issue discount amount
type: Ontology Property
---

# has original issue discount amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasOriginalIssueDiscountAmount>

## Definition

indicates the difference between the stated redemption price at maturity and the issue price

## Relationships

- **Domain**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label**: has original issue discount amount
- **definition**: indicates the difference between the stated redemption price at maturity and the issue price

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
