---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is extendable by holder
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the expiration date or maturity date can be extended by the holder
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/isExtendableByHolder
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: is extendable by holder
type: Ontology Property
---

# is extendable by holder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/isExtendableByHolder>

## Definition

indicates whether the expiration date or maturity date can be extended by the holder

## Relationships

- **Domain**: [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is extendable by holder
- **definition**: indicates whether the expiration date or maturity date can be extended by the holder

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
