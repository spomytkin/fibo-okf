---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: c d o portfolio manager
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The portfolio manager for a managed CDO or arbitrage CDO (also called an asset manager). This assumes that the
      role is the same in both cases.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/manages
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: c d o portfolio manager
type: Ontology Class
---

# c d o portfolio manager

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager>

## Definition

The portfolio manager for a managed CDO or arbitrage CDO (also called an asset manager). This assumes that the role is the same in both cases.

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[manages](<https://www.omg.org/spec/Commons/Organizations/manages>)**: some values from of type [CDOPortfolio](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio.md)

## Annotations

- **label** (en): c d o portfolio manager
- **definition** (en): The portfolio manager for a managed CDO or arbitrage CDO (also called an asset manager). This assumes that the role is the same in both cases.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
