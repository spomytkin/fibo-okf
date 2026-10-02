---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transition loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) designed
      to help a business or organization shift from carbon-intensive or environmentally harmful practices to more sustainable
      and environmentally friendly operations
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Transition loans are part of the broader sustainable finance market and are specifically tailored for companies
      in industries that are not inherently green but are committed to adopting practices that align with a low-carbon or
      sustainable economy.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Transition loans are structured to assist companies in reducing greenhouse gas (GHG) emissions, improving energy
      efficiency, adopting renewable energy sources, or meeting other sustainability targets aligned with climate transition
      goals. They support initiatives such as retrofitting fossil fuel-based systems, decarbonizing supply chains, or adopting
      cleaner production methods. Transition loans align with emerging Climate Transition Finance principles (developed by
      groups such as the International Capital Market Association, ICMA). Borrowers are expected to demonstrate that the loan
      aligns with long-term, science-based climate goals, such as those outlined in the Paris Agreement (e.g., limiting global
      warming to well below 2°C).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/DisclosureProvision
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionUseOfProceedsProvision
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractMilestone
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasMilestoneProvision
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MilestoneSchedule
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionStrategy
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically
  - concept: /concepts/fibo/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/CommercialLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionLoan
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: transition loan
type: Ontology Class
---

# transition loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionLoan>

## Definition

credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) designed to help a business or organization shift from carbon-intensive or environmentally harmful practices to more sustainable and environmentally friendly operations

## Relationships

- **Subclass of**: [CreditAgreementRepaidPeriodically](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)
- **Subclass of**: [CommercialLoan](/concepts/fibo/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [DisclosureProvision](/concepts/fibo/FND/Agreements/Contracts/DisclosureProvision.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [TransitionUseOfProceedsProvision](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/TransitionUseOfProceedsProvision.md)
- **[hasMilestoneProvision](/concepts/fibo/FND/Agreements/Contracts/hasMilestoneProvision.md)**: min qualified cardinality 0 of type [ContractMilestone](/concepts/fibo/FND/Agreements/Contracts/ContractMilestone.md)
- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: min qualified cardinality 0 of type [MilestoneSchedule](/concepts/fibo/FND/Agreements/Contracts/MilestoneSchedule.md)
- **[hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)**: some values from of type [TransitionStrategy](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/TransitionStrategy.md)

## Annotations

- **label** (en): transition loan
- **definition** (en): credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) designed to help a business or organization shift from carbon-intensive or environmentally harmful practices to more sustainable and environmentally friendly operations
- **explanatoryNote** (en): Transition loans are part of the broader sustainable finance market and are specifically tailored for companies in industries that are not inherently green but are committed to adopting practices that align with a low-carbon or sustainable economy.
- **explanatoryNote** (en): Transition loans are structured to assist companies in reducing greenhouse gas (GHG) emissions, improving energy efficiency, adopting renewable energy sources, or meeting other sustainability targets aligned with climate transition goals. They support initiatives such as retrofitting fossil fuel-based systems, decarbonizing supply chains, or adopting cleaner production methods. Transition loans align with emerging Climate Transition Finance principles (developed by groups such as the International Capital Market Association, ICMA). Borrowers are expected to demonstrate that the loan aligns with long-term, science-based climate goals, such as those outlined in the Paris Agreement (e.g., limiting global warming to well below 2°C).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
