---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: static c d o
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A CDO where collateral is fixed through the life of the CDO. The reference assets are bought and then are kept
      untouched for the term of the product.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Investors can assess the various tranches of the CDO with full knowledge of what the collateral will be. The primary
      risk they face is credit risk. A deal that starts off managed can become static if the performance is too poor. Also,
      some deals are static but allow managers to sell out poorly performing assets subject to certain conditions, but do
      not allow purchase of new assets, so are semi-static.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/StaticManagementStyle
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/managementStyle.1
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/StaticCDO
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: static c d o
type: Ontology Class
---

# static c d o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/StaticCDO>

## Definition

A CDO where collateral is fixed through the life of the CDO. The reference assets are bought and then are kept untouched for the term of the product.

## Relationships

- **Subclass of**: [CDODeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)

## Constraints

- **[managementStyle.1](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/managementStyle.1.md)**: some values from of type [StaticManagementStyle](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/StaticManagementStyle.md)

## Annotations

- **label** (en): static c d o
- **definition** (en): A CDO where collateral is fixed through the life of the CDO. The reference assets are bought and then are kept untouched for the term of the product.
- **explanatoryNote** (en): Investors can assess the various tranches of the CDO with full knowledge of what the collateral will be. The primary risk they face is credit risk. A deal that starts off managed can become static if the performance is too poor. Also, some deals are static but allow managers to sell out poorly performing assets subject to certain conditions, but do not allow purchase of new assets, so are semi-static.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
