---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: call premium
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the price over par paid by an issuer to redeem securities when exercising a call provision
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallPremium
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: call premium
type: Ontology Class
---

# call premium

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallPremium>

## Definition

the price over par paid by an issuer to redeem securities when exercising a call provision

## Relationships

- **Subclass of**: [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)

## Annotations

- **label**: call premium
- **definition**: the price over par paid by an issuer to redeem securities when exercising a call provision

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
