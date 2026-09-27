---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund investment policy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: policy that the fund implements in order to achieve the stated fund objectives
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'EFAMA Note: Model distinguishes between strategy (what you intend to invest in) and portfolio structure (what
      is held). This semantics matches the EFAMA DD "Fund Investment Policy" No stated definition in EFAMA DD ("Further discussion
      required").'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/stipulatesBenchmark
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Policy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Policy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentPolicy
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund investment policy
type: Ontology Class
---

# fund investment policy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentPolicy>

## Definition

policy that the fund implements in order to achieve the stated fund objectives

## Relationships

- **Subclass of**: [Policy](/concepts/fibo/FND/Law/LegalCapacity/Policy.md)

## Constraints

- **[stipulatesBenchmark](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/stipulatesBenchmark.md)**: max qualified cardinality 1 of type [MarketRate](/concepts/fibo/IND/Indicators/Indicators/MarketRate.md)
- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [InvestmentRestriction](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction.md)
- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [PortfolioInvestmentStrategy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md)

## Annotations

- **label** (en): fund investment policy
- **definition** (en): policy that the fund implements in order to achieve the stated fund objectives
- **explanatoryNote** (en): EFAMA Note: Model distinguishes between strategy (what you intend to invest in) and portfolio structure (what is held). This semantics matches the EFAMA DD "Fund Investment Policy" No stated definition in EFAMA DD ("Further discussion required").

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
