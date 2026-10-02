---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: weighted average loan age
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: dollar-weighted average measuring the age of the individual loans in a mortgage pass-through or pooled security
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: WALA
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A weighted average loan age (WALA) may apply to pool-backed securities such as Ginnie Mae or Freddie Mac securities.
      The WALA is measured as the time in months since the origination of the loans, with the weighting based on each loan's
      size in proportion to the aggregate total of the pool.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is defined by the issuer. WALA is more official, not an analysis from a vendor. This changes but the values
      are relayed by the issuer on an ongoing basis. Investopedia explains Weighted Average Loan Age - WALA The weighted average
      age will change over time as some mortgages get paid off faster than others. Based on the issuer of the mortgage-backed
      securities (MBS), the WALA may be weighted on the remaining principal balance dollar figure, or the beginning notional
      value of the loan. The flip side of the WALA is the weighted average maturity (WAM), which is a dollar-weighted measure
      of the months remaining until the principal amounts are completely repaid on each loan in the pool.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ArithmeticMean
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageLoanAge
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: weighted average loan age
type: Ontology Class
---

# weighted average loan age

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageLoanAge>

## Definition

dollar-weighted average measuring the age of the individual loans in a mortgage pass-through or pooled security

## Relationships

- **Subclass of**: [ArithmeticMean](/concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md)
- **Subclass of**: [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)

## Annotations

- **label** (en): weighted average loan age
- **definition** (en): dollar-weighted average measuring the age of the individual loans in a mortgage pass-through or pooled security
- **abbreviation** (en): WALA
- **explanatoryNote** (en): A weighted average loan age (WALA) may apply to pool-backed securities such as Ginnie Mae or Freddie Mac securities. The WALA is measured as the time in months since the origination of the loans, with the weighting based on each loan's size in proportion to the aggregate total of the pool.
- **explanatoryNote** (en): This is defined by the issuer. WALA is more official, not an analysis from a vendor. This changes but the values are relayed by the issuer on an ongoing basis. Investopedia explains Weighted Average Loan Age - WALA The weighted average age will change over time as some mortgages get paid off faster than others. Based on the issuer of the mortgage-backed securities (MBS), the WALA may be weighted on the remaining principal balance dollar figure, or the beginning notional value of the loan. The flip side of the WALA is the weighted average maturity (WAM), which is a dollar-weighted measure of the months remaining until the principal amounts are completely repaid on each loan in the pool.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
