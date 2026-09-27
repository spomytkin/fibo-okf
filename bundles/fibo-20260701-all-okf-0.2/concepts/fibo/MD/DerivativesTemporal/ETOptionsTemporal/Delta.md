---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: delta
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: First derivative of option value with respect to theoretical price is a delta (or on a position). Theoretical price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Delta tells you what options to buy to get the equivalent price sensitivity to the underlying. How many at that
      price to get that hedge. So for example an at the money option has a delta of 50. Units
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/MD/DerivativesTemporal/ETOptionsTemporal/OptionsGreek.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionsGreek
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/Delta
sources:
- id: fibo-source-c9fb3c7ad1
  resource: references/fibo/MD/DerivativesTemporal/ETOptionsTemporal.rdf
  sha256: c9fb3c7ad151168ecfeee8fa19d4cecdedf784d117c95c63d88ddd4c69e32f13
  title: FIBO source MD/DerivativesTemporal/ETOptionsTemporal.rdf
title: delta
type: Ontology Class
---

# delta

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/Delta>

## Definition

First derivative of option value with respect to theoretical price is a delta (or on a position). Theoretical price

## Relationships

- **Subclass of**: [OptionsGreek](/concepts/fibo/MD/DerivativesTemporal/ETOptionsTemporal/OptionsGreek.md)

## Annotations

- **label** (en): delta
- **definition** (en): First derivative of option value with respect to theoretical price is a delta (or on a position). Theoretical price
- **explanatoryNote** (en): Delta tells you what options to buy to get the equivalent price sensitivity to the underlying. How many at that price to get that hedge. So for example an at the money option has a delta of 50. Units

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
