---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sustainability performance target
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collection of quantitative target values used to calibrate the level of achievement a borrower makes with respect
      to a key performance indicator, by date, including, but not limited to, the methodology used to calculate its value
      at any point over the lifetime of a loan
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SPT
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lsta.org/content/sustainability-linked-loan-principles-sllp/
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An SLL borrower should clearly communicate to its lenders its rationale for the selection of its KPI(s) (i.e. relevance,
      materiality, whether it is core to the borrower’s overall business) and the motivation for the SPT(s) (i.e. ambition
      level, benchmarking approach and how the borrower intends to reach such SPTs). Borrowers are encouraged to position
      this information within the context of their overarching objectives, sustainability strategy, policy, sustainability
      commitments and/or processes relating to sustainability.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The process for calibration of the SPT(s) per KPI is key to the structuring of SLLs, since it will be the expression
      of the level of ambition the borrower is ready to commit to. The SPTs must be set in good faith and remain relevant
      (so long as they apply) and ambitious throughout the life of the loan.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/isCalculatedViaMethodology
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TargetIndicatorValue
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculationPeriod
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTargetIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: sustainability performance target
type: Ontology Class
---

# sustainability performance target

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget>

## Definition

collection of quantitative target values used to calibrate the level of achievement a borrower makes with respect to a key performance indicator, by date, including, but not limited to, the methodology used to calculate its value at any point over the lifetime of a loan

## Relationships

- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Constraints

- **[isCalculatedViaMethodology](/concepts/fibo/FND/Utilities/Analytics/isCalculatedViaMethodology.md)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [TargetIndicatorValue](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/TargetIndicatorValue.md)
- **[hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)**: some values from of type [CalculationPeriod](/concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculationPeriod.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [SustainabilityPerformanceTargetIdentifier](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTargetIdentifier.md)

## Annotations

- **label** (en): sustainability performance target
- **definition** (en): collection of quantitative target values used to calibrate the level of achievement a borrower makes with respect to a key performance indicator, by date, including, but not limited to, the methodology used to calculate its value at any point over the lifetime of a loan
- **abbreviation** (en): SPT
- **adaptedFrom** (en): https://www.lsta.org/content/sustainability-linked-loan-principles-sllp/
- **explanatoryNote** (en): An SLL borrower should clearly communicate to its lenders its rationale for the selection of its KPI(s) (i.e. relevance, materiality, whether it is core to the borrower’s overall business) and the motivation for the SPT(s) (i.e. ambition level, benchmarking approach and how the borrower intends to reach such SPTs). Borrowers are encouraged to position this information within the context of their overarching objectives, sustainability strategy, policy, sustainability commitments and/or processes relating to sustainability.
- **explanatoryNote** (en): The process for calibration of the SPT(s) per KPI is key to the structuring of SLLs, since it will be the expression of the level of ambition the borrower is ready to commit to. The SPTs must be set in good faith and remain relevant (so long as they apply) and ambitious throughout the life of the loan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
