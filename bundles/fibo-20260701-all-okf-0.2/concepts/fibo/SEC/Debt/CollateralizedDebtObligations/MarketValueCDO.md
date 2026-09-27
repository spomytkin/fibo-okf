---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market value c d o
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MarketValueStructure
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/structure.2
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MarketValueCDO
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: market value c d o
type: Ontology Class
---

# market value c d o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MarketValueCDO>

## Relationships

- **Subclass of**: [CDODeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)

## Constraints

- **[structure.2](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/structure.2.md)**: some values from of type [MarketValueStructure](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MarketValueStructure.md)

## Annotations

- **label** (en): market value c d o

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
