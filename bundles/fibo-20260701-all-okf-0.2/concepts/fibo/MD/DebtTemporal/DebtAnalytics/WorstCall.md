---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: worst call
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: call event representing the worst case with respect to when the instrument might be called
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Note that the actual date associated with an occurrence of a worst call event might be calculated or explicit.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: We should refine what we mean by worst here - soonest, or most distant?
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallEvent
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/WorstCall
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: worst call
type: Ontology Class
---

# worst call

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/WorstCall>

## Definition

call event representing the worst case with respect to when the instrument might be called

## Relationships

- **Subclass of**: [CallEvent](/concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md)

## Annotations

- **label** (en): worst call
- **definition** (en): call event representing the worst case with respect to when the instrument might be called
- **editorialNote** (en): Note that the actual date associated with an occurrence of a worst call event might be calculated or explicit.
- **editorialNote** (en): We should refine what we mean by worst here - soonest, or most distant?

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
