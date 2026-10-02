---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: put event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an event associated with the put schedule for a debt instrument, i.e., an event involving the 'put', or surrender
      of the instrument by the holder
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/RedemptionEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/RedemptionEvent
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutEvent
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: put event
type: Ontology Class
---

# put event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutEvent>

## Definition

an event associated with the put schedule for a debt instrument, i.e., an event involving the 'put', or surrender of the instrument by the holder

## Relationships

- **Subclass of**: [RedemptionEvent](/concepts/fibo/SEC/Debt/DebtInstruments/RedemptionEvent.md)

## Annotations

- **label**: put event
- **definition**: an event associated with the put schedule for a debt instrument, i.e., an event involving the 'put', or surrender of the instrument by the holder

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
