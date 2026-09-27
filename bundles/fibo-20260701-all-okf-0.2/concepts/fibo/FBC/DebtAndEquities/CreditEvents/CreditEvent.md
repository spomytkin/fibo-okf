---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit event
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event signifying a sudden change in credit standing, such as bankruptcy or a violation of a bond indenture or loan
      agreement, that raises doubts about the party's ability to meet current or future obligations
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/CreditEvent
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: credit event
type: Ontology Class
---

# credit event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/CreditEvent>

## Definition

event signifying a sudden change in credit standing, such as bankruptcy or a violation of a bond indenture or loan agreement, that raises doubts about the party's ability to meet current or future obligations

## Relationships

- **Subclass of**: [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Annotations

- **label** (en): credit event
- **definition** (en): event signifying a sudden change in credit standing, such as bankruptcy or a violation of a bond indenture or loan agreement, that raises doubts about the party's ability to meet current or future obligations

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
