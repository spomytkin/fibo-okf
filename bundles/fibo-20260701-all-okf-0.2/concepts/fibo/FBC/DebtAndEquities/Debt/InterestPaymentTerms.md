---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest payment terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms for payment of interest on a debt
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Interest is usually payable on any outstanding principal amount, therefore interest relates to the amount of debt
      outstanding at any given point of time, not to the principal amount advanced at the time that the loan was advanced
      or the debt security issued (aside from the initial payment).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that in most cases, the dates and payment frequencies for interest will coincide with the dates and payment
      frequencies related to the principal.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Interest
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/governsPaymentOf
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasAccrualBasis
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasCompoundingFrequency
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInitialInterestAccrualDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInitialInterestPaymentDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/DayOfMonth
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestPaymentDay
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestPaymentFrequency
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRateCap
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDuration
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasFirstRateChangeTerm
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/DebtTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DebtTerms
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentTerms
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: interest payment terms
type: Ontology Class
---

# interest payment terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentTerms>

## Definition

contract terms for payment of interest on a debt

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [DebtTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/DebtTerms.md)

## Constraints

- **[governsPaymentOf](/concepts/fibo/FBC/DebtAndEquities/Debt/governsPaymentOf.md)**: some values from of type [Interest](/concepts/fibo/FBC/DebtAndEquities/Debt/Interest.md)
- **[hasAccrualBasis](/concepts/fibo/FBC/DebtAndEquities/Debt/hasAccrualBasis.md)**: min qualified cardinality 0 of type [DayCountConvention](/concepts/fibo/FBC/DebtAndEquities/Debt/DayCountConvention.md)
- **[hasCompoundingFrequency](/concepts/fibo/FBC/DebtAndEquities/Debt/hasCompoundingFrequency.md)**: min qualified cardinality 0 of type [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- **[hasInitialInterestAccrualDate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInitialInterestAccrualDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasInitialInterestPaymentDate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInitialInterestPaymentDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasInterestPaymentDay](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestPaymentDay.md)**: min qualified cardinality 0 of type [DayOfMonth](/concepts/fibo/FND/DatesAndTimes/BusinessDates/DayOfMonth.md)
- **[hasInterestPaymentFrequency](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestPaymentFrequency.md)**: min qualified cardinality 0 of type [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: min qualified cardinality 0 of type [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)
- **[hasInterestRateCap](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRateCap.md)**: min qualified cardinality 0 of type [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)
- **[hasFirstRateChangeTerm](/concepts/fibo/LOAN/LoansGeneral/Loans/hasFirstRateChangeTerm.md)**: min qualified cardinality 0 of type [ExplicitDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDuration>)

## Annotations

- **label**: interest payment terms
- **definition**: contract terms for payment of interest on a debt
- **explanatoryNote**: Interest is usually payable on any outstanding principal amount, therefore interest relates to the amount of debt outstanding at any given point of time, not to the principal amount advanced at the time that the loan was advanced or the debt security issued (aside from the initial payment).
- **explanatoryNote**: Note that in most cases, the dates and payment frequencies for interest will coincide with the dates and payment frequencies related to the principal.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
