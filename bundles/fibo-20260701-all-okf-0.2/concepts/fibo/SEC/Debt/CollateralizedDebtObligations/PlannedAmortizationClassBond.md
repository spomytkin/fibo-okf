---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: planned amortization class bond
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Planned Amortization Class tranche.This is a tranche where the principal payment must follow a certain schedule.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These tranches have priority over the other tranches in the deal, which are then referred to as the support or
      companion tranches. There are usually several PAC tranches created. PAC-1, PAC-2, PAC-3 -- this requires some more explanation.
      PAC-2 refers to a support tranche that is given a scheduled payment structure like a PAC bond. For example, let's say
      you have a deal with a PAC tranche and a support tranche (i.e., a tranche that is a support tranche and is therefore
      subordinate to the PAC tranche) that has a scheduled payment structure like you did with the PAC bond. That support
      bond then is called the PAC-2 bond. If you continue, and create another support tranche that also has scheduled payments,
      that would become the PAC-3 bond. Prospectus will cover each class. Prospectus is at the level of an issue.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/providesPrepaymentSupportFor
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PACTrancheAmortizationSchedule
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/specifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/supportedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyCMO
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: planned amortization class bond
type: Ontology Class
---

# planned amortization class bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond>

## Definition

Planned Amortization Class tranche.This is a tranche where the principal payment must follow a certain schedule.

## Relationships

- **Subclass of**: [AgencyCMO](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md)

## Constraints

- **[providesPrepaymentSupportFor](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/providesPrepaymentSupportFor.md)**: all values from of type [PlannedAmortizationClassBond](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond.md)
- **[specifies](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/specifies.md)**: some values from of type [PACTrancheAmortizationSchedule](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/PACTrancheAmortizationSchedule.md)
- **[supportedBy](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/supportedBy.md)**: all values from of type [PlannedAmortizationClassBond](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond.md)

## Annotations

- **label** (en): planned amortization class bond
- **definition** (en): Planned Amortization Class tranche.This is a tranche where the principal payment must follow a certain schedule.
- **explanatoryNote** (en): These tranches have priority over the other tranches in the deal, which are then referred to as the support or companion tranches. There are usually several PAC tranches created. PAC-1, PAC-2, PAC-3 -- this requires some more explanation. PAC-2 refers to a support tranche that is given a scheduled payment structure like a PAC bond. For example, let's say you have a deal with a PAC tranche and a support tranche (i.e., a tranche that is a support tranche and is therefore subordinate to the PAC tranche) that has a scheduled payment structure like you did with the PAC bond. That support bond then is called the PAC-2 bond. If you continue, and create another support tranche that also has scheduled payments, that would become the PAC-3 bond. Prospectus will cover each class. Prospectus is at the level of an issue.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
