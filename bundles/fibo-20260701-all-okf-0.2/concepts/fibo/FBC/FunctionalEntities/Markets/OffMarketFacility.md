---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: off-market facility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: facility used for reporting over-the-counter (OTC) and other direct trades that are not executed by the exchange
      but are reported through the exchange
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: off-book
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: off-facility
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OffMarketFacility
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: off-market facility
type: Ontology Class
---

# off-market facility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OffMarketFacility>

## Definition

facility used for reporting over-the-counter (OTC) and other direct trades that are not executed by the exchange but are reported through the exchange

## Relationships

- **Subclass of**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Annotations

- **label**: off-market facility
- **definition**: facility used for reporting over-the-counter (OTC) and other direct trades that are not executed by the exchange but are reported through the exchange
- **synonym**: off-book
- **synonym**: off-facility

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
