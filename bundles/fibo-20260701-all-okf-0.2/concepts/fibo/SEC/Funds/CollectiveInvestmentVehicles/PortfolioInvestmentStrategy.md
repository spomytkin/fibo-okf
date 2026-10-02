---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: portfolio investment strategy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The manner in which the portfolio manager tries to reach the funds objectives.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Describes how you get there. E.g fully invested v not fully invested. MB Note: The terms labeled "Strategy" in
      EFAMA and in FIBIM are more like dictionary definition of policy, while "How you get there" is a dictionary definition
      of Strategy. Therefore original labels may be reversed from dictionary definition of the global semantics these are
      derived from.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/InvestmentStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/InvestmentStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: portfolio investment strategy
type: Ontology Class
---

# portfolio investment strategy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy>

## Definition

The manner in which the portfolio manager tries to reach the funds objectives.

## Relationships

- **Subclass of**: [InvestmentStrategy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/InvestmentStrategy.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [FundPortfolioInvestmentLimitations](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md)

## Annotations

- **label** (en): portfolio investment strategy
- **definition** (en): The manner in which the portfolio manager tries to reach the funds objectives.
- **explanatoryNote** (en): Describes how you get there. E.g fully invested v not fully invested. MB Note: The terms labeled "Strategy" in EFAMA and in FIBIM are more like dictionary definition of policy, while "How you get there" is a dictionary definition of Strategy. Therefore original labels may be reversed from dictionary definition of the global semantics these are derived from.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
