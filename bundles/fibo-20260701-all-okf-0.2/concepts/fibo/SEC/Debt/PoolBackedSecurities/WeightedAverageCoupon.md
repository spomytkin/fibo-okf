---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: weighted average coupon
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: weighted-average gross interest rates of the pool of mortgages that underlie a mortgage-backed security (MBS) weighed
      by their balances at the time the securities were issued
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Provided by the Issuer (loan servicer?) along with the WALA etc. If you know the underlying loans you can calculate
      this yourself. For ABS you don''t know this so you have to get this information from the loan servicer. Investopedia
      explains Weighted Average Coupon - WAC For example, suppose a MBS is composed of two different pools of mortgages: $6
      million worth of mortgages that yield 7.5% and a pool of $4 million mortgages that yield 5%. The WAC would be 6.5%.
      The WAC on a mortgage-backed security is an important piece of information used by analysts to estimate the pre-pay
      characteristics of that security. It is an important relative value tool in MBS portfolio management and analysis.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: WAC
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The weighted average coupon (WAC) is calculated by taking the gross of the interest rates owed on the underlying
      mortgages of the MBS and weighting them according to the percentage of the security that each mortgage represents. The
      WAC represents the average interest rate of different pools of mortgages with varying interest rates. In the weighted
      average calculation, the principal balance of each underlying mortgage is used as the weighting factor. To calculate
      the WAC, the coupon rate of each mortgage or MBS is multiplied by its remaining principal balance. The results are added
      together, and the sum total is divided by the remaining balance. A mortgage-backed security's current WAC can differ
      from its original WAC as the underlying mortgages pay down at different speeds. In the weighted-average calculation,
      the principal balance of each underlying mortgage is used as the weighting factor.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ArithmeticMean
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageCoupon
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: weighted average coupon
type: Ontology Class
---

# weighted average coupon

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageCoupon>

## Definition

weighted-average gross interest rates of the pool of mortgages that underlie a mortgage-backed security (MBS) weighed by their balances at the time the securities were issued

## Relationships

- **Subclass of**: [ArithmeticMean](/concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md)
- **Subclass of**: [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)

## Annotations

- **label** (en): weighted average coupon
- **definition** (en): weighted-average gross interest rates of the pool of mortgages that underlie a mortgage-backed security (MBS) weighed by their balances at the time the securities were issued
- **editorialNote** (en): Provided by the Issuer (loan servicer?) along with the WALA etc. If you know the underlying loans you can calculate this yourself. For ABS you don't know this so you have to get this information from the loan servicer. Investopedia explains Weighted Average Coupon - WAC For example, suppose a MBS is composed of two different pools of mortgages: $6 million worth of mortgages that yield 7.5% and a pool of $4 million mortgages that yield 5%. The WAC would be 6.5%. The WAC on a mortgage-backed security is an important piece of information used by analysts to estimate the pre-pay characteristics of that security. It is an important relative value tool in MBS portfolio management and analysis.
- **abbreviation** (en): WAC
- **explanatoryNote** (en): The weighted average coupon (WAC) is calculated by taking the gross of the interest rates owed on the underlying mortgages of the MBS and weighting them according to the percentage of the security that each mortgage represents. The WAC represents the average interest rate of different pools of mortgages with varying interest rates. In the weighted average calculation, the principal balance of each underlying mortgage is used as the weighting factor. To calculate the WAC, the coupon rate of each mortgage or MBS is multiplied by its remaining principal balance. The results are added together, and the sum total is divided by the remaining balance. A mortgage-backed security's current WAC can differ from its original WAC as the underlying mortgages pay down at different speeds. In the weighted-average calculation, the principal balance of each underlying mortgage is used as the weighting factor.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
