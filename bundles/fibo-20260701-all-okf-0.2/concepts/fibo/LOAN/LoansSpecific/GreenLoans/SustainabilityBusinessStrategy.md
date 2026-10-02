---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sustainability business strategy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: strategy for achieving specific business objectives related to sustainability (from an environmental and/or social
      and/or governance (ESG) perspective)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lsta.org/content/sustainability-linked-loan-principles-sllp/
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An SLL borrower should clearly communicate to its lender(s) its rationale for the selection of its KPI(s) (i.e.
      relevance, materiality, whether it is core to the borrower's overall business) and the motivation for the SPT(s) (i.e.
      ambition level, benchmarking approach and how the borrower intends to reach such SPTs). Borrowers are encouraged to
      position this information within the context of their overarching objectives, sustainability strategy, policy, sustainability
      commitments and/or processes relating to sustainability.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: SLLs aim to support a borrower's efforts in improving its sustainability profile over the term of the loan. They
      do so by aligning loan terms to the borrower's performance, which is measured using one or more sustainability KPIs
      that can be internal and/or external. The KPIs must be material to the borrower's core sustainability and business strategy,
      and address relevant ESG challenges of its industry sector.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityBusinessObjective
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicator
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/BusinessStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/BusinessStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityBusinessStrategy
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: sustainability business strategy
type: Ontology Class
---

# sustainability business strategy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityBusinessStrategy>

## Definition

strategy for achieving specific business objectives related to sustainability (from an environmental and/or social and/or governance (ESG) perspective)

## Relationships

- **Subclass of**: [BusinessStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/BusinessStrategy.md)

## Constraints

- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: min qualified cardinality 0 of type [SustainabilityPerformanceTarget](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget.md)
- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: some values from of type [SustainabilityBusinessObjective](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityBusinessObjective.md)
- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: some values from of type [SustainabilityKeyPerformanceIndicator](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicator.md)

## Annotations

- **label** (en): sustainability business strategy
- **definition** (en): strategy for achieving specific business objectives related to sustainability (from an environmental and/or social and/or governance (ESG) perspective)
- **adaptedFrom** (en): https://www.lsta.org/content/sustainability-linked-loan-principles-sllp/
- **explanatoryNote** (en): An SLL borrower should clearly communicate to its lender(s) its rationale for the selection of its KPI(s) (i.e. relevance, materiality, whether it is core to the borrower's overall business) and the motivation for the SPT(s) (i.e. ambition level, benchmarking approach and how the borrower intends to reach such SPTs). Borrowers are encouraged to position this information within the context of their overarching objectives, sustainability strategy, policy, sustainability commitments and/or processes relating to sustainability.
- **explanatoryNote** (en): SLLs aim to support a borrower's efforts in improving its sustainability profile over the term of the loan. They do so by aligning loan terms to the borrower's performance, which is measured using one or more sustainability KPIs that can be internal and/or external. The KPIs must be material to the borrower's core sustainability and business strategy, and address relevant ESG challenges of its industry sector.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
