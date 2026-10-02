---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: hybrid c d o
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'A CDO which combines features both of the cash and synthetic CDO. This is a CDO with tranches of cash and tranches
      of synthetic underlying assets. Further notes: So for example an issiue of $550 million may have $500 million in an
      asset pool and an additional $50 million created via a synthetic asset.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: all_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
    value: N3b21254a807145279398ab66a50e4602
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/HybridCDO
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: hybrid c d o
type: Ontology Class
---

# hybrid c d o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/HybridCDO>

## Definition

A CDO which combines features both of the cash and synthetic CDO. This is a CDO with tranches of cash and tranches of synthetic underlying assets. Further notes: So for example an issiue of $550 million may have $500 million in an asset pool and an additional $50 million created via a synthetic asset.

## Relationships

- **Subclass of**: [CDODeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: all values from value `N3b21254a807145279398ab66a50e4602`

## Annotations

- **label** (en): hybrid c d o
- **definition** (en): A CDO which combines features both of the cash and synthetic CDO. This is a CDO with tranches of cash and tranches of synthetic underlying assets. Further notes: So for example an issiue of $550 million may have $500 million in an asset pool and an additional $50 million created via a synthetic asset.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
