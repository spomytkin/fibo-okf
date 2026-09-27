---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: price is traded
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'The highest valuation over the period specified. Notes from Equity review, may apply to Debt also: this can be
      regarded as a derived price. See also note in LowPrice Difference: different rules used. May be based on trade OR quote
      price Analytic or Price?? this is a derived type but with a much simpler rule.'
  domain:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/ExchangeTradedBondPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/ExchangeTradedBondPrice
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/priceIsTraded
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: price is traded
type: Ontology Property
---

# price is traded

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/priceIsTraded>

## Definition

The highest valuation over the period specified. Notes from Equity review, may apply to Debt also: this can be regarded as a derived price. See also note in LowPrice Difference: different rules used. May be based on trade OR quote price Analytic or Price?? this is a derived type but with a much simpler rule.

## Relationships

- **Domain**: [ExchangeTradedBondPrice](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/ExchangeTradedBondPrice.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): price is traded
- **definition** (en): The highest valuation over the period specified. Notes from Equity review, may apply to Debt also: this can be regarded as a derived price. See also note in LowPrice Difference: different rules used. May be based on trade OR quote price Analytic or Price?? this is a derived type but with a much simpler rule.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
