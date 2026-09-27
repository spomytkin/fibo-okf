---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has first call price
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the amount of the call on the first call date as specified in the call schedule
  domain:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/hasCallPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasCallPrice
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasFirstCallPrice
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has first call price
type: Ontology Property
---

# has first call price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasFirstCallPrice>

## Definition

indicates the amount of the call on the first call date as specified in the call schedule

## Relationships

- **Domain**: [CallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md)
- **Range**: [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **Subproperty of**: [hasCallPrice](/concepts/fibo/SEC/Debt/Bonds/hasCallPrice.md)

## Annotations

- **label**: has first call price
- **definition**: indicates the amount of the call on the first call date as specified in the call schedule

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
