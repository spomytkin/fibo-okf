---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cashflow structure
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The source of funds for the CDO is cashflow. this means that cash flows from collateral are used to pay principal
      and interest to investors.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOCashflowTreatmentStructure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOCashflowTreatmentStructure
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashflowStructure
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: cashflow structure
type: Ontology Class
---

# cashflow structure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashflowStructure>

## Definition

The source of funds for the CDO is cashflow. this means that cash flows from collateral are used to pay principal and interest to investors.

## Relationships

- **Subclass of**: [CDOCashflowTreatmentStructure](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOCashflowTreatmentStructure.md)

## Annotations

- **label** (en): cashflow structure
- **definition** (en): The source of funds for the CDO is cashflow. this means that cash flows from collateral are used to pay principal and interest to investors.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
