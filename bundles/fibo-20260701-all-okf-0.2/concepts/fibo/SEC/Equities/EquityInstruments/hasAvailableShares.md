---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has available shares
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the number of shares outstanding less those shares that are restricted, i.e., those that are available
      for trading
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasAmount
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasAvailableShares
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has available shares
type: Ontology Property
---

# has available shares

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasAvailableShares>

## Definition

indicates the number of shares outstanding less those shares that are restricted, i.e., those that are available for trading

## Relationships

- **Range**: [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **Subproperty of**: [hasAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md)

## Annotations

- **label** (en): has available shares
- **definition** (en): indicates the number of shares outstanding less those shares that are restricted, i.e., those that are available for trading

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
