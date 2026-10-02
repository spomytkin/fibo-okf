---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is default interest applicable
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether a party that defaults in the performance of any payment obligation is, to the extent permitted
      by law and the applicable agreement, required to pay interest (before as well as after judgment) on the overdue amount
      to the other party on demand in the same currency as such overdue amount, for the period from (and including) the original
      due date for payment to (but excluding) the date of actual payment
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/InterestObligationInLightOfDefault.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/InterestObligationInLightOfDefault
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/isDefaultInterestApplicable
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: is default interest applicable
type: Ontology Property
---

# is default interest applicable

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/isDefaultInterestApplicable>

## Definition

indicates whether a party that defaults in the performance of any payment obligation is, to the extent permitted by law and the applicable agreement, required to pay interest (before as well as after judgment) on the overdue amount to the other party on demand in the same currency as such overdue amount, for the period from (and including) the original due date for payment to (but excluding) the date of actual payment

## Relationships

- **Domain**: [InterestObligationInLightOfDefault](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/InterestObligationInLightOfDefault.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is default interest applicable
- **definition** (en): indicates whether a party that defaults in the performance of any payment obligation is, to the extent permitted by law and the applicable agreement, required to pay interest (before as well as after judgment) on the overdue amount to the other party on demand in the same currency as such overdue amount, for the period from (and including) the original due date for payment to (but excluding) the date of actual payment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
