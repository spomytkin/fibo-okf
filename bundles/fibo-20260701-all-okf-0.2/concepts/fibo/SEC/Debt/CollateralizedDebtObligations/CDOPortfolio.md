---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: c d o portfolio
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A portfolio in which the reference assets of the CDO are held.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Portfolio.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Portfolio
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: c d o portfolio
type: Ontology Class
---

# c d o portfolio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio>

## Definition

A portfolio in which the reference assets of the CDO are held.

## Relationships

- **Subclass of**: [Portfolio](/concepts/fibo/FND/OwnershipAndControl/Ownership/Portfolio.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [MBSInstrumentSlice](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: some values from of type [CDOPortfolioManager](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager.md)

## Annotations

- **label** (en): c d o portfolio
- **definition** (en): A portfolio in which the reference assets of the CDO are held.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
