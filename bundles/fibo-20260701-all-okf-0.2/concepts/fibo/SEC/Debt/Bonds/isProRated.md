---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is pro-rated
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the coupon is pro rated to the actual number of days in the payment period versus the number
      of payment periods
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isProRated
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: is pro-rated
type: Ontology Property
---

# is pro-rated

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isProRated>

## Definition

indicates whether the coupon is pro rated to the actual number of days in the payment period versus the number of payment periods

## Relationships

- **Domain**: [InterestPaymentTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is pro-rated
- **definition**: indicates whether the coupon is pro rated to the actual number of days in the payment period versus the number of payment periods

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
