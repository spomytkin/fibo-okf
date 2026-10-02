---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: p a c-1 class
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Planned Amortization Class tranche. PAC-1 is the most senior Planned Amortization Class tranche.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Principal payment must follow a certain schedule. These tranches have priority over the other tranches in the deal,
      which are then referred to as the support or companion tranches.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PAC-2Class
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/takesPrepaymentAfter
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PAC-1Class
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: p a c-1 class
type: Ontology Class
---

# p a c-1 class

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PAC-1Class>

## Definition

Planned Amortization Class tranche. PAC-1 is the most senior Planned Amortization Class tranche.

## Relationships

- **Subclass of**: [PlannedAmortizationClassBond](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond.md)

## Constraints

- **[takesPrepaymentAfter](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/takesPrepaymentAfter.md)**: all values from of type [PAC-2Class](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/PAC-2Class.md)

## Annotations

- **label** (en): p a c-1 class
- **definition** (en): Planned Amortization Class tranche. PAC-1 is the most senior Planned Amortization Class tranche.
- **explanatoryNote** (en): Principal payment must follow a certain schedule. These tranches have priority over the other tranches in the deal, which are then referred to as the support or companion tranches.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
