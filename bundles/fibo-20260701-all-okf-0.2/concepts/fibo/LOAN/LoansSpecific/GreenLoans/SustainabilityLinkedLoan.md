---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sustainability-linked loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) for which
      the economic characteristics can vary depending on whether the borrower achieves ambitious, material and quantifiable
      predetermined sustainability performance objectives aligned with Sustainability-Linked Loan Principles (SSLP)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: The use of proceeds in relation to a SLL is not a determinant in its categorisation and, in most instances, SLLs
      will be used for general corporate purposes. Instead, SLLs look to support a borrower in improving its sustainability
      performance.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SLL
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.addleshawgoddard.com/en/insights/insights-briefings/2020/financial-services/green-loans-and-sustainability-linked-loans-what-is-the-difference/
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lsta.org/content/sustainable-lending-glossary-of-terms/
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A borrower's sustainability performance is measured using sustainability performance targets (SPTs), which include
      key performance indicators, external ratings and/or equivalent metrics that measure improvements in the borrower's sustainability
      profile.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/DisclosureProvision
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
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityBusinessStrategy
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically
  - concept: /concepts/fibo/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/CommercialLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityLinkedLoan
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: sustainability-linked loan
type: Ontology Class
---

# sustainability-linked loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityLinkedLoan>

## Definition

credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) for which the economic characteristics can vary depending on whether the borrower achieves ambitious, material and quantifiable predetermined sustainability performance objectives aligned with Sustainability-Linked Loan Principles (SSLP)

## Relationships

- **Subclass of**: [CreditAgreementRepaidPeriodically](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)
- **Subclass of**: [CommercialLoan](/concepts/fibo/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [DisclosureProvision](/concepts/fibo/FND/Agreements/Contracts/DisclosureProvision.md)
- **[hasMilestoneProvision](/concepts/fibo/FND/Agreements/Contracts/hasMilestoneProvision.md)**: min qualified cardinality 0 of type [ContractMilestone](/concepts/fibo/FND/Agreements/Contracts/ContractMilestone.md)
- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: min qualified cardinality 0 of type [MilestoneSchedule](/concepts/fibo/FND/Agreements/Contracts/MilestoneSchedule.md)
- **[hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)**: some values from of type [SustainabilityBusinessStrategy](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityBusinessStrategy.md)

## Annotations

- **label** (en): sustainability-linked loan
- **definition** (en): credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) for which the economic characteristics can vary depending on whether the borrower achieves ambitious, material and quantifiable predetermined sustainability performance objectives aligned with Sustainability-Linked Loan Principles (SSLP)
- **example** (en): The use of proceeds in relation to a SLL is not a determinant in its categorisation and, in most instances, SLLs will be used for general corporate purposes. Instead, SLLs look to support a borrower in improving its sustainability performance.
- **abbreviation** (en): SLL
- **adaptedFrom** (en): https://www.addleshawgoddard.com/en/insights/insights-briefings/2020/financial-services/green-loans-and-sustainability-linked-loans-what-is-the-difference/
- **adaptedFrom** (en): https://www.lsta.org/content/sustainable-lending-glossary-of-terms/
- **explanatoryNote** (en): A borrower's sustainability performance is measured using sustainability performance targets (SPTs), which include key performance indicators, external ratings and/or equivalent metrics that measure improvements in the borrower's sustainability profile.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
