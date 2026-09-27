---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transition strategy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: strategy for achieving specific business objectives related to sustainability in the context of long-term decarbonization
      or sustainability transitions
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that although there are similarities with sustainability business strategies, they are not the same. KPIs
      and SPTs may, however, be defined similarly for a given project.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget
    kind: some_values_from
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
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionStrategy
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: transition strategy
type: Ontology Class
---

# transition strategy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionStrategy>

## Definition

strategy for achieving specific business objectives related to sustainability in the context of long-term decarbonization or sustainability transitions

## Relationships

- **Subclass of**: [BusinessStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/BusinessStrategy.md)

## Constraints

- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: some values from of type [SustainabilityPerformanceTarget](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget.md)
- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: some values from of type [SustainabilityBusinessObjective](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityBusinessObjective.md)
- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: some values from of type [SustainabilityKeyPerformanceIndicator](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicator.md)

## Annotations

- **label** (en): transition strategy
- **definition** (en): strategy for achieving specific business objectives related to sustainability in the context of long-term decarbonization or sustainability transitions
- **explanatoryNote** (en): Note that although there are similarities with sustainability business strategies, they are not the same. KPIs and SPTs may, however, be defined similarly for a given project.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
