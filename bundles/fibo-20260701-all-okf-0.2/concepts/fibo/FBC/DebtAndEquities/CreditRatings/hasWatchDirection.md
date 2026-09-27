---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: watch direction
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates direction in which an investment credit rating is expected to move in cases where that rating is on watch
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditRatings/InvestmentCreditRating.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/InvestmentCreditRating
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditWatchDirection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditWatchDirection
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/hasWatchDirection
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: watch direction
type: Ontology Property
---

# watch direction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/hasWatchDirection>

## Definition

indicates direction in which an investment credit rating is expected to move in cases where that rating is on watch

## Relationships

- **Domain**: [InvestmentCreditRating](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/InvestmentCreditRating.md)
- **Range**: [CreditWatchDirection](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditWatchDirection.md)

## Annotations

- **label** (en): watch direction
- **definition** (en): indicates direction in which an investment credit rating is expected to move in cases where that rating is on watch

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
