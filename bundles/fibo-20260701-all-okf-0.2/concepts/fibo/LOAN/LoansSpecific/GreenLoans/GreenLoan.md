---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: green loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) made available
      exclusively to finance, re-finance or guarantee, in whole or in part, new and/or existing eligible green projects that
      are aligned to the four core components of the Green Loan Principles (GLP)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Example categories of eligibility contained in the LMA's Green Loan Principles (GLP) include loans designed to
      facilitate renewable energy, energy efficiency, climate change adaptation and green buildings that meet regional, national
      or internationally recognised standards or certifications.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.addleshawgoddard.com/en/insights/insights-briefings/2020/financial-services/green-loans-and-sustainability-linked-loans-what-is-the-difference/
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lsta.org/content/sustainable-lending-glossary-of-terms/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/DisclosureProvision
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/GreenProjectUseOfProceedsProvision
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
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/GreenLoan
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: green loan
type: Ontology Class
---

# green loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/GreenLoan>

## Definition

credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) made available exclusively to finance, re-finance or guarantee, in whole or in part, new and/or existing eligible green projects that are aligned to the four core components of the Green Loan Principles (GLP)

## Relationships

- **Subclass of**: [CreditAgreementRepaidPeriodically](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [DisclosureProvision](/concepts/fibo/FND/Agreements/Contracts/DisclosureProvision.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [GreenProjectUseOfProceedsProvision](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/GreenProjectUseOfProceedsProvision.md)
- **[hasMilestoneProvision](/concepts/fibo/FND/Agreements/Contracts/hasMilestoneProvision.md)**: min qualified cardinality 0 of type [ContractMilestone](/concepts/fibo/FND/Agreements/Contracts/ContractMilestone.md)
- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: min qualified cardinality 0 of type [MilestoneSchedule](/concepts/fibo/FND/Agreements/Contracts/MilestoneSchedule.md)

## Annotations

- **label** (en): green loan
- **definition** (en): credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) made available exclusively to finance, re-finance or guarantee, in whole or in part, new and/or existing eligible green projects that are aligned to the four core components of the Green Loan Principles (GLP)
- **example** (en): Example categories of eligibility contained in the LMA's Green Loan Principles (GLP) include loans designed to facilitate renewable energy, energy efficiency, climate change adaptation and green buildings that meet regional, national or internationally recognised standards or certifications.
- **adaptedFrom** (en): https://www.addleshawgoddard.com/en/insights/insights-briefings/2020/financial-services/green-loans-and-sustainability-linked-loans-what-is-the-difference/
- **adaptedFrom** (en): https://www.lsta.org/content/sustainable-lending-glossary-of-terms/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
