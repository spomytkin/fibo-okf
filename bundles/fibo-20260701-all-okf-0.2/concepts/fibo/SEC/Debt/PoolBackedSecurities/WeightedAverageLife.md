---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: weighted average life
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: weighted average of the times of the principal repayments Average life is calculated using the weighted average
      time to the receipt of all future cash flows.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: WAL
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Average life is calculated using the weighted average time to the receipt of all future cash flows of an amortizing
      loan or amortizing bond. it's the average time until a dollar of principal is repaid.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The time weightings used in weighted average life calculations are based on payments to the principal. In many
      loans, such as mortgages, each payment consists of payments to principal and payments to interest. In WAL, only the
      principal payments are considered and these payments tend to get larger over time, with early payments of a mortgage
      going mostly to interest, while payments made towards the end of the loan are applied mostly to the principal balance
      of the loan.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Where it refers to pre-payment above, if the bond does not include prepayment then this is not included. However,
      analytics that refer to this e.g. Yield to Average Life, then this figure is relevant. It is not relevant for other
      types of bond where e.g. you would use yield to next call, yield to worst etc. Average Life used in place of Maturity
      for Yield Calculation. This is not only used for Yield calculations though. It is referred to as an analytic figure
      in its own right. Average Life uses one of a number of standard pre-payment models (for structured finance at least).
      For MBS, the average life includes some calculations to take account of pre-payments on the underlying mortgages. This
      takes account of the possibillity of borrowers paying early. This has to be modeled or forecast (not given) as it''s
      a function of market conditions and interest rate. You would not see this in a market data feed. When you model MBS
      you calculate Average Life as part of the model i.e. you estimate the percentage of prepayment in the next x length
      of time and factor this into the Average Life. Refers to Weighted Average Time to receipt of future cash flows. For
      MBS, early payments will shorten the Average Life. For Student Loans, Credit Card, Loan etc, i.e. all Pool Backed (any
      bond that has securitized debt). Other bonds: Sinking Funds etc., also Early Payment - partial Call for a corporate
      / regular bond. Early Payment for pass through has the same effect. Sinking Fund: Each payment is part principal and
      part interest, this is implicit in the overall definition of "Early payment".'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: average life
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ArithmeticMean
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageLife
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: weighted average life
type: Ontology Class
---

# weighted average life

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageLife>

## Definition

weighted average of the times of the principal repayments Average life is calculated using the weighted average time to the receipt of all future cash flows.

## Relationships

- **Subclass of**: [ArithmeticMean](/concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md)
- **Subclass of**: [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)

## Constraints

- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: min qualified cardinality 0 of type [PrepaymentSpeed](/concepts/fibo/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed.md)

## Annotations

- **label** (en): weighted average life
- **definition** (en): weighted average of the times of the principal repayments Average life is calculated using the weighted average time to the receipt of all future cash flows.
- **abbreviation** (en): WAL
- **explanatoryNote** (en): Average life is calculated using the weighted average time to the receipt of all future cash flows of an amortizing loan or amortizing bond. it's the average time until a dollar of principal is repaid.
- **explanatoryNote** (en): The time weightings used in weighted average life calculations are based on payments to the principal. In many loans, such as mortgages, each payment consists of payments to principal and payments to interest. In WAL, only the principal payments are considered and these payments tend to get larger over time, with early payments of a mortgage going mostly to interest, while payments made towards the end of the loan are applied mostly to the principal balance of the loan.
- **explanatoryNote** (en): Where it refers to pre-payment above, if the bond does not include prepayment then this is not included. However, analytics that refer to this e.g. Yield to Average Life, then this figure is relevant. It is not relevant for other types of bond where e.g. you would use yield to next call, yield to worst etc. Average Life used in place of Maturity for Yield Calculation. This is not only used for Yield calculations though. It is referred to as an analytic figure in its own right. Average Life uses one of a number of standard pre-payment models (for structured finance at least). For MBS, the average life includes some calculations to take account of pre-payments on the underlying mortgages. This takes account of the possibillity of borrowers paying early. This has to be modeled or forecast (not given) as it's a function of market conditions and interest rate. You would not see this in a market data feed. When you model MBS you calculate Average Life as part of the model i.e. you estimate the percentage of prepayment in the next x length of time and factor this into the Average Life. Refers to Weighted Average Time to receipt of future cash flows. For MBS, early payments will shorten the Average Life. For Student Loans, Credit Card, Loan etc, i.e. all Pool Backed (any bond that has securitized debt). Other bonds: Sinking Funds etc., also Early Payment - partial Call for a corporate / regular bond. Early Payment for pass through has the same effect. Sinking Fund: Each payment is part principal and part interest, this is implicit in the overall definition of "Early payment".
- **synonym** (en): average life

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
