---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has relative price at issue
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a relative price with respect to the face value at which an instrument is issued, namely par, premium
      or discount
  range:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/RelativePrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/RelativePrice
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtIssue
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: has relative price at issue
type: Ontology Property
---

# has relative price at issue

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtIssue>

## Definition

indicates a relative price with respect to the face value at which an instrument is issued, namely par, premium or discount

## Relationships

- **Range**: [RelativePrice](/concepts/fibo/SEC/Debt/DebtInstruments/RelativePrice.md)
- **Subproperty of**: [hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)

## Annotations

- **label**: has relative price at issue
- **definition**: indicates a relative price with respect to the face value at which an instrument is issued, namely par, premium or discount

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
