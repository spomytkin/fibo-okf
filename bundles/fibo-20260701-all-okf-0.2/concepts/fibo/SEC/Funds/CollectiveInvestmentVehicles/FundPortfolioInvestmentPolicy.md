---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund portfolio investment policy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: policy with respect to allocation of the portfolio that is designed to meet the stated investment strategy and
      goals
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'ISO FIBIM: Rough allocation of the portfolio.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/definesAllocations
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Policy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Policy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentPolicy
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund portfolio investment policy
type: Ontology Class
---

# fund portfolio investment policy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentPolicy>

## Definition

policy with respect to allocation of the portfolio that is designed to meet the stated investment strategy and goals

## Relationships

- **Subclass of**: [Policy](/concepts/fibo/FND/Law/LegalCapacity/Policy.md)

## Constraints

- **[definesAllocations](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/definesAllocations.md)**: some values from of type [FundPortfolioInvestmentLimitations](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md)
- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [PortfolioInvestmentStrategy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md)

## Annotations

- **label** (en): fund portfolio investment policy
- **definition** (en): policy with respect to allocation of the portfolio that is designed to meet the stated investment strategy and goals
- **explanatoryNote** (en): ISO FIBIM: Rough allocation of the portfolio.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
