---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: weighted average remaining term
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: weighted average time to maturity of a portfolio of asset-backed securities (ABS) or mortgage-backed (MBS) securities
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: WART
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The longer the WART, the longer the portfolio's assets will take to mature, on average. WART is often used in relation
      to mortgage-backed securities (MBS) but can also be applied to any portfolio of fixed-income securities. WART is closely
      related to weighted average loan age (WALA), which is its inverse.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: weighted average remaining maturity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ArithmeticMean
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageRemainingTerm
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: weighted average remaining term
type: Ontology Class
---

# weighted average remaining term

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageRemainingTerm>

## Definition

weighted average time to maturity of a portfolio of asset-backed securities (ABS) or mortgage-backed (MBS) securities

## Relationships

- **Subclass of**: [ArithmeticMean](/concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md)
- **Subclass of**: [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)

## Annotations

- **label** (en): weighted average remaining term
- **definition** (en): weighted average time to maturity of a portfolio of asset-backed securities (ABS) or mortgage-backed (MBS) securities
- **abbreviation** (en): WART
- **explanatoryNote** (en): The longer the WART, the longer the portfolio's assets will take to mature, on average. WART is often used in relation to mortgage-backed securities (MBS) but can also be applied to any portfolio of fixed-income securities. WART is closely related to weighted average loan age (WALA), which is its inverse.
- **synonym** (en): weighted average remaining maturity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
