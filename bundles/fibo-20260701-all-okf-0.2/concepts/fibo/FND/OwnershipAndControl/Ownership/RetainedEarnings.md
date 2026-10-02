---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: retained earnings
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: net profits kept to accumulate in a business after dividends are paid
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the corporation takes a loss, then that loss is retained and called variously retained losses, accumulated losses
      or accumulated deficit. Retained earnings and losses are cumulative from year to year with losses offsetting earnings.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/OwnersEquity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/OwnersEquity
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/RetainedEarnings
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: retained earnings
type: Ontology Class
---

# retained earnings

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/RetainedEarnings>

## Definition

net profits kept to accumulate in a business after dividends are paid

## Relationships

- **Subclass of**: [OwnersEquity](/concepts/fibo/FND/OwnershipAndControl/Ownership/OwnersEquity.md)

## Annotations

- **label**: retained earnings
- **definition**: net profits kept to accumulate in a business after dividends are paid
- **explanatoryNote**: If the corporation takes a loss, then that loss is retained and called variously retained losses, accumulated losses or accumulated deficit. Retained earnings and losses are cumulative from year to year with losses offsetting earnings.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
