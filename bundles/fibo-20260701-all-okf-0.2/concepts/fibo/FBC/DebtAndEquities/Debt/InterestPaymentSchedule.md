---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest payment schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: regular, contract-specific schedule including the dates on which interest is due to be paid
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The dates may be fixed, or expressed as an offset of the calculation dates. Typically the payment dates are fixed
      and calculation dates are expressed as an offset, however.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPayment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOccurrence
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentSchedule
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: interest payment schedule
type: Ontology Class
---

# interest payment schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentSchedule>

## Definition

regular, contract-specific schedule including the dates on which interest is due to be paid

## Relationships

- **Subclass of**: [ProjectedContractEventSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md)
- **Subclass of**: [PaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)

## Constraints

- **[hasOccurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOccurrence.md)**: some values from of type [InterestPayment](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestPayment.md)

## Annotations

- **label**: interest payment schedule
- **definition**: regular, contract-specific schedule including the dates on which interest is due to be paid
- **explanatoryNote**: The dates may be fixed, or expressed as an offset of the calculation dates. Typically the payment dates are fixed and calculation dates are expressed as an offset, however.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
