---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: downgrade
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit event triggered when the credit rating of a party or obligation is lowered
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: On October 17, 2013, Dagong Global Credit Rating downgraded the United States from A to A- and maintained a negative
      outlook on the country's credit.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/CreditEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/CreditEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/Downgrade
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: downgrade
type: Ontology Class
---

# downgrade

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/Downgrade>

## Definition

credit event triggered when the credit rating of a party or obligation is lowered

## Relationships

- **Subclass of**: [CreditEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/CreditEvent.md)

## Annotations

- **label** (en): downgrade
- **definition** (en): credit event triggered when the credit rating of a party or obligation is lowered
- **example** (en): On October 17, 2013, Dagong Global Credit Rating downgraded the United States from A to A- and maintained a negative outlook on the country's credit.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
