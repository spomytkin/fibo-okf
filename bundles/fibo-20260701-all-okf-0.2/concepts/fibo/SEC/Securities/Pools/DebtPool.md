---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt pool
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: pool consisting of debt instruments, such as bonds, loans or mortgages
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasAnalytic
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DefaultRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasDefaultRate
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PoolFactor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasFactor
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasMeasure
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/InstrumentPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/InstrumentPool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
- id: fibo-source-73259da08c
  resource: references/fibo/SEC/Securities/Pools.rdf
  sha256: 73259da08ce2d3336ab19acd98a9182e1bef062fb636a27936e96545e083ec39
  title: FIBO source SEC/Securities/Pools.rdf
title: debt pool
type: Ontology Class
---

# debt pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool>

## Definition

pool consisting of debt instruments, such as bonds, loans or mortgages

## Relationships

- **Subclass of**: [InstrumentPool](/concepts/fibo/SEC/Securities/Pools/InstrumentPool.md)

## Constraints

- **[hasAnalytic](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/hasAnalytic.md)**: some values from of type [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
- **[hasDefaultRate](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/hasDefaultRate.md)**: some values from of type [DefaultRate](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DefaultRate.md)
- **[hasFactor](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/hasFactor.md)**: some values from of type [PoolFactor](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/PoolFactor.md)
- **[hasMeasure](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/hasMeasure.md)**: some values from of type [PrepaymentSpeed](/concepts/fibo/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [DebtInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)

## Annotations

- **label**: debt pool
- **definition**: pool consisting of debt instruments, such as bonds, loans or mortgages

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
