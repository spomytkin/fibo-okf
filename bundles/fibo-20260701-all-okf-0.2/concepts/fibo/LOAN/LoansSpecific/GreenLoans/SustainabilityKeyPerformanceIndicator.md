---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sustainability key performance indicator
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measurable performance indicator that is sustainability specific
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lsta.org/content/sustainability-linked-loan-principles-sllp/
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'A sustainability KPI must be: (a) relevant, core and material to the borrower''s overall business, and of high
      strategic significance to the borrower''s current and/or future operations; (b) measurable or quantifiable on a consistent
      methodological basis; and (c) able to be benchmarked (i.e. as much as possible using an external reference or definitions
      to facilitate the assessment of the SPT''s level of ambition). A clear definition of the KPI(s) should be provided by
      the borrower and should include the applicable scope or parameters, as well as the calculation methodology, a definition
      of a baseline and be benchmarked against an industry standard and/or industry peers where feasible.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValueStructure
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasObservedValue
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasTargetValue
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicatorIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/KeyPerformanceIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/KeyPerformanceIndicator
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicator
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: sustainability key performance indicator
type: Ontology Class
---

# sustainability key performance indicator

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicator>

## Definition

measurable performance indicator that is sustainability specific

## Relationships

- **Subclass of**: [KeyPerformanceIndicator](/concepts/fibo/FND/Utilities/Analytics/KeyPerformanceIndicator.md)

## Constraints

- **[hasObservedValue](/concepts/fibo/FND/Utilities/Analytics/hasObservedValue.md)**: min qualified cardinality 0 of type [ObservedIndicatorValueStructure](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValueStructure.md)
- **[hasTargetValue](/concepts/fibo/FND/Utilities/Analytics/hasTargetValue.md)**: min qualified cardinality 0 of type [SustainabilityPerformanceTarget](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [SustainabilityKeyPerformanceIndicatorIdentifier](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicatorIdentifier.md)

## Annotations

- **label** (en): sustainability key performance indicator
- **definition** (en): measurable performance indicator that is sustainability specific
- **adaptedFrom** (en): https://www.lsta.org/content/sustainability-linked-loan-principles-sllp/
- **explanatoryNote** (en): A sustainability KPI must be: (a) relevant, core and material to the borrower's overall business, and of high strategic significance to the borrower's current and/or future operations; (b) measurable or quantifiable on a consistent methodological basis; and (c) able to be benchmarked (i.e. as much as possible using an external reference or definitions to facilitate the assessment of the SPT's level of ambition). A clear definition of the KPI(s) should be provided by the borrower and should include the applicable scope or parameters, as well as the calculation methodology, a definition of a baseline and be benchmarked against an industry standard and/or industry peers where feasible.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
