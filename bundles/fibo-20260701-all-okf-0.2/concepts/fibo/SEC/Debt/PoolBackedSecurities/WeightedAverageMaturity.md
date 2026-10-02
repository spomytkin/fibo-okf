---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: weighted average maturity
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: weighted average amount of time until the maturities on mortgages in a mortgage-backed security (MBS)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: WAM
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The measure is calculated by totaling each mortgage value represented by the MBS. The weights of each mortgage
      is found by dividing the value of each into the total of all. To arrive at the WAM number the weight of each security
      is multiplied by the time until maturity of each mortgage, and then all the values are added together. For example say
      an MBS has three mortgages valued at $1,000, $2,000 and $3,000 (a total of $6,000) and mature in one, two and three
      years respectively. The weights of these are 1/6 (1,000/6,000), 1/3 (2,000/6,000) and 1/2 (3,000/6,000). The WAM is
      2 1/3 years (1/6 x 1 year + 1/3 x 2 years + 1/2 x 3 years). Note that this calculation would need to be adjusted if
      there are multiple pools behind the MBS.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This term is used more broadly to describe maturities in a portfolio of debt securities, including corporate debt
      and municipal bonds. The higher the WAM, the longer it takes for all of the mortgages or bonds in the portfolio to mature.
      WAM is used to manage debt portfolios and to assess the performance of debt portfolio managers.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ArithmeticMean
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageMaturity
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: weighted average maturity
type: Ontology Class
---

# weighted average maturity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageMaturity>

## Definition

weighted average amount of time until the maturities on mortgages in a mortgage-backed security (MBS)

## Relationships

- **Subclass of**: [ArithmeticMean](/concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md)
- **Subclass of**: [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)

## Annotations

- **label** (en): weighted average maturity
- **definition** (en): weighted average amount of time until the maturities on mortgages in a mortgage-backed security (MBS)
- **abbreviation** (en): WAM
- **explanatoryNote** (en): The measure is calculated by totaling each mortgage value represented by the MBS. The weights of each mortgage is found by dividing the value of each into the total of all. To arrive at the WAM number the weight of each security is multiplied by the time until maturity of each mortgage, and then all the values are added together. For example say an MBS has three mortgages valued at $1,000, $2,000 and $3,000 (a total of $6,000) and mature in one, two and three years respectively. The weights of these are 1/6 (1,000/6,000), 1/3 (2,000/6,000) and 1/2 (3,000/6,000). The WAM is 2 1/3 years (1/6 x 1 year + 1/3 x 2 years + 1/2 x 3 years). Note that this calculation would need to be adjusted if there are multiple pools behind the MBS.
- **explanatoryNote** (en): This term is used more broadly to describe maturities in a portfolio of debt securities, including corporate debt and municipal bonds. The higher the WAM, the longer it takes for all of the mortgages or bonds in the portfolio to mature. WAM is used to manage debt portfolios and to assess the performance of debt portfolio managers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
