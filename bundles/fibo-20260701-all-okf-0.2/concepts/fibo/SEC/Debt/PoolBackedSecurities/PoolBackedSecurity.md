---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pool-backed security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt instrument that derives its cashflow from an underlying pool of mortgage loans or other receivables
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the security is a component of a collateralized debt obligation, then the underlying pool is typically segmented
      into various tranches, each of which provides cash flows to hedge particular risks, or that offset other gains by time
      to maturity or other factors.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/InstrumentPool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/hasEstimatedTotalCollateralValueAtIssuance
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/isPassThrough
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: pool-backed security
type: Ontology Class
---

# pool-backed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity>

## Definition

debt instrument that derives its cashflow from an underlying pool of mortgage loans or other receivables

## Relationships

- **Subclass of**: [TradableDebtInstrument](/concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [InstrumentPool](/concepts/fibo/SEC/Securities/Pools/InstrumentPool.md)
- **[hasEstimatedTotalCollateralValueAtIssuance](/concepts/fibo/SEC/Debt/PoolBackedSecurities/hasEstimatedTotalCollateralValueAtIssuance.md)**: min qualified cardinality 0 of type [CollateralValueAsOfDate](/concepts/fibo/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md)
- **[isPassThrough](/concepts/fibo/SEC/Debt/PoolBackedSecurities/isPassThrough.md)**: exact qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: min qualified cardinality 0 of type [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)

## Annotations

- **label** (en): pool-backed security
- **definition** (en): debt instrument that derives its cashflow from an underlying pool of mortgage loans or other receivables
- **explanatoryNote** (en): If the security is a component of a collateralized debt obligation, then the underlying pool is typically segmented into various tranches, each of which provides cash flows to hedge particular risks, or that offset other gains by time to maturity or other factors.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
