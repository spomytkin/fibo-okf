---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: amortization schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: schedule of periodic payments (repayment installments) that specify changes in the balance of the debt over time
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Payments are divided into equal amounts for the duration of the loan or debt instrument, making it the simplest
      repayment model. A greater amount of the payment is applied to interest at the beginning of the amortization schedule,
      while more money is applied to principal at the end.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Amortization
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/embodies
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentSchedule
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PrincipalPaymentSchedule
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/AmortizationSchedule
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: amortization schedule
type: Ontology Class
---

# amortization schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/AmortizationSchedule>

## Definition

schedule of periodic payments (repayment installments) that specify changes in the balance of the debt over time

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [ProjectedContractEventSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md)
- **Subclass of**: [PaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)

## Constraints

- **[embodies](/concepts/fibo/FND/Relations/Relations/embodies.md)**: some values from of type [Amortization](/concepts/fibo/FBC/DebtAndEquities/Debt/Amortization.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [InterestPaymentSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentSchedule.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [PrincipalPaymentSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/PrincipalPaymentSchedule.md)

## Annotations

- **label**: amortization schedule
- **definition**: schedule of periodic payments (repayment installments) that specify changes in the balance of the debt over time
- **explanatoryNote**: Payments are divided into equal amounts for the duration of the loan or debt instrument, making it the simplest repayment model. A greater amount of the payment is applied to interest at the beginning of the amortization schedule, while more money is applied to principal at the end.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
