---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has yield
  domain:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
  range:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasYield
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: has yield
type: Ontology Property
---

# has yield

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasYield>

## Relationships

- **Domain**: [TradableDebtInstrument](/concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)
- **Range**: [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)

## Annotations

- **label** (en): has yield

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
