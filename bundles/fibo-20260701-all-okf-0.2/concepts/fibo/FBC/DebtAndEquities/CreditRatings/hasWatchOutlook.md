---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: watch outlook
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the expected outlook for the rated entity
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditRatings/InvestmentCreditRating.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/InvestmentCreditRating
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditWatchOutlook.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditWatchOutlook
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/hasWatchOutlook
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: watch outlook
type: Ontology Property
---

# watch outlook

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/hasWatchOutlook>

## Definition

indicates the expected outlook for the rated entity

## Relationships

- **Domain**: [InvestmentCreditRating](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/InvestmentCreditRating.md)
- **Range**: [CreditWatchOutlook](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditWatchOutlook.md)

## Annotations

- **label** (en): watch outlook
- **definition** (en): indicates the expected outlook for the rated entity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
