---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: quote-driven market
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exchange in which prices are determined from bid and ask quotations made by market makers, dealers, or specialists
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In a quote-driven market, dealers fill orders from their own inventory or by matching them with other orders. Note
      that this differs from a typical market, which is order-driven rather than quote-driven.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: price-driven market
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/QuoteDrivenMarket
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: quote-driven market
type: Ontology Class
---

# quote-driven market

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/QuoteDrivenMarket>

## Definition

exchange in which prices are determined from bid and ask quotations made by market makers, dealers, or specialists

## Relationships

- **Subclass of**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Annotations

- **label**: quote-driven market
- **definition**: exchange in which prices are determined from bid and ask quotations made by market makers, dealers, or specialists
- **explanatoryNote**: In a quote-driven market, dealers fill orders from their own inventory or by matching them with other orders. Note that this differs from a typical market, which is order-driven rather than quote-driven.
- **synonym**: price-driven market

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
