---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund investment objective
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The aim of a Fund e.g outperfom a given benchmark.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'This could be broken down into other terms that can be itemised here, that are not in the EFAMA DD explicitly.
      Examples may include: - Risk level - Return - Exposure to different markets'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/RiskLevel
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasIntendedRiskLevel
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/Prospectus
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/statedIn
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/InvestmentObjective.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/InvestmentObjective
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentObjective
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund investment objective
type: Ontology Class
---

# fund investment objective

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentObjective>

## Definition

The aim of a Fund e.g outperfom a given benchmark.

## Relationships

- **Subclass of**: [InvestmentObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/InvestmentObjective.md)

## Constraints

- **[hasIntendedRiskLevel](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasIntendedRiskLevel.md)**: some values from of type [RiskLevel](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/RiskLevel.md)
- **[statedIn](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/statedIn.md)**: some values from of type [Prospectus](/concepts/fibo/SEC/Securities/SecuritiesIssuance/Prospectus.md)

## Annotations

- **label** (en): fund investment objective
- **definition** (en): The aim of a Fund e.g outperfom a given benchmark.
- **editorialNote** (en): This could be broken down into other terms that can be itemised here, that are not in the EFAMA DD explicitly. Examples may include: - Risk level - Return - Exposure to different markets

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
