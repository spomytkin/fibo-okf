---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: principal repayment terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms that specify requirements for repayment of the principal
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Principal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/governsPaymentOf
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInitialPrincipalPaymentDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/DayOfMonth
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasPrincipalPaymentDay
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasPrincipalPaymentFrequency
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasPrincipalRepaymentDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ExtensionProvision
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasExtensionProvision
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasBalloonPayment
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/isInitiallyPayable
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/DebtTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DebtTerms
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: principal repayment terms
type: Ontology Class
---

# principal repayment terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms>

## Definition

contract terms that specify requirements for repayment of the principal

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [DebtTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/DebtTerms.md)

## Constraints

- **[governsPaymentOf](/concepts/fibo/FBC/DebtAndEquities/Debt/governsPaymentOf.md)**: some values from of type [Principal](/concepts/fibo/FBC/DebtAndEquities/Debt/Principal.md)
- **[hasInitialPrincipalPaymentDate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInitialPrincipalPaymentDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasPrincipalPaymentDay](/concepts/fibo/FBC/DebtAndEquities/Debt/hasPrincipalPaymentDay.md)**: min qualified cardinality 0 of type [DayOfMonth](/concepts/fibo/FND/DatesAndTimes/BusinessDates/DayOfMonth.md)
- **[hasPrincipalPaymentFrequency](/concepts/fibo/FBC/DebtAndEquities/Debt/hasPrincipalPaymentFrequency.md)**: min qualified cardinality 0 of type [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- **[hasPrincipalRepaymentDate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasPrincipalRepaymentDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasExtensionProvision](/concepts/fibo/FND/Agreements/Contracts/hasExtensionProvision.md)**: max qualified cardinality 1 of type [ExtensionProvision](/concepts/fibo/FND/Agreements/Contracts/ExtensionProvision.md)
- **[hasBalloonPayment](/concepts/fibo/LOAN/LoansGeneral/Loans/hasBalloonPayment.md)**: min qualified cardinality 0 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[isInitiallyPayable](/concepts/fibo/LOAN/LoansGeneral/Loans/isInitiallyPayable.md)**: min qualified cardinality 0 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: principal repayment terms
- **definition**: contract terms that specify requirements for repayment of the principal

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
