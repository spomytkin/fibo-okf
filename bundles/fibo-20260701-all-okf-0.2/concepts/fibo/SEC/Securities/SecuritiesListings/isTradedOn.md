---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is traded on
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the trading facility on which the security is traded
  domain:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
  range:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isTradedOn
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: is traded on
type: Ontology Property
---

# is traded on

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isTradedOn>

## Definition

identifies the trading facility on which the security is traded

## Relationships

- **Domain**: [ListedSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md)
- **Range**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)
- **Subproperty of**: [isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)

## Annotations

- **label**: is traded on
- **definition**: identifies the trading facility on which the security is traded

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
