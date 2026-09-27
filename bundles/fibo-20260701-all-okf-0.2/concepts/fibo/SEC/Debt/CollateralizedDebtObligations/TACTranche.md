---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: t a c tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Targeted Amortization Class. This is related to a PAC tranche and has a payment schedule geared towards a specified
      prepayment speed (called the pricing speed). Agency CMO
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'The main difference between TAC and PAC is that the PAC schedule remains under a certain prepayment range (such
      as 50-150 PSA) while the TAC tranche is geared from the outset at a specified prepayment speed (such as 150 PSA). Math
      note: Originally specified in PSAin the examples. What is PSA? Review how we have modeled "Payment Speed" as a concept.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TACTrancheAmortizationSchedule
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/specifies.1
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyCMO
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TACTranche
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: t a c tranche
type: Ontology Class
---

# t a c tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TACTranche>

## Definition

Targeted Amortization Class. This is related to a PAC tranche and has a payment schedule geared towards a specified prepayment speed (called the pricing speed). Agency CMO

## Relationships

- **Subclass of**: [AgencyCMO](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md)
- **Subclass of**: [TranchedMBSInstrument](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md)

## Constraints

- **[specifies.1](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/specifies.1.md)**: some values from of type [TACTrancheAmortizationSchedule](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TACTrancheAmortizationSchedule.md)

## Annotations

- **label** (en): t a c tranche
- **definition** (en): Targeted Amortization Class. This is related to a PAC tranche and has a payment schedule geared towards a specified prepayment speed (called the pricing speed). Agency CMO
- **editorialNote** (en): The main difference between TAC and PAC is that the PAC schedule remains under a certain prepayment range (such as 50-150 PSA) while the TAC tranche is geared from the outset at a specified prepayment speed (such as 150 PSA). Math note: Originally specified in PSAin the examples. What is PSA? Review how we have modeled "Payment Speed" as a concept.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
