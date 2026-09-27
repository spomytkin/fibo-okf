---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund portfolio
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An account containing a number of financial instruments along with cash positions in one or more currencies and
      belonging to a Fund
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Balance
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioBenchmark
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/assessedAgainst
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasInvestmentStrategy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentPolicy
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/implementsFundPolicy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Portfolio
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Portfolio.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Portfolio
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund portfolio
type: Ontology Class
---

# fund portfolio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio>

## Definition

An account containing a number of financial instruments along with cash positions in one or more currencies and belonging to a Fund

## Relationships

- **Subclass of**: [Portfolio](/concepts/fibo/FND/OwnershipAndControl/Ownership/Portfolio.md)

## Constraints

- **[hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)**: some values from of type [Balance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- **[assessedAgainst](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/assessedAgainst.md)**: some values from of type [PortfolioBenchmark](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/PortfolioBenchmark.md)
- **[hasInvestmentStrategy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasInvestmentStrategy.md)**: some values from of type [PortfolioInvestmentStrategy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md)
- **[implementsFundPolicy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/implementsFundPolicy.md)**: some values from of type [FundPortfolioInvestmentPolicy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentPolicy.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [Portfolio](/concepts/fibo/FND/OwnershipAndControl/Ownership/Portfolio.md)

## Annotations

- **label** (en): fund portfolio
- **definition** (en): An account containing a number of financial instruments along with cash positions in one or more currencies and belonging to a Fund

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
