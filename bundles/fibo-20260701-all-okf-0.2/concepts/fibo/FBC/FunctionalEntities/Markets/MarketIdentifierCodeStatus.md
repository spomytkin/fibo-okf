---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market indicator code status
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: lifecycle stage indicating the status of the MIC code, as specified by the registration authority
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/market-identifier-codes
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketIdentifierCodeStatus
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: market indicator code status
type: Ontology Class
---

# market indicator code status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketIdentifierCodeStatus>

## Definition

lifecycle stage indicating the status of the MIC code, as specified by the registration authority

## Relationships

- **Subclass of**: [LifecycleStage](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md)

## Annotations

- **label**: market indicator code status
- **definition**: lifecycle stage indicating the status of the MIC code, as specified by the registration authority
- **adaptedFrom**: https://www.iso20022.org/market-identifier-codes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
