---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is listed via
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the service responsible for listing the security
  domain:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
  inverse_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/lists.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/lists
  range:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/Listing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isListedVia
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: is listed via
type: Ontology Property
---

# is listed via

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isListedVia>

## Definition

identifies the service responsible for listing the security

## Relationships

- **Domain**: [ListedSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md)
- **Inverse of**: [lists](/concepts/fibo/SEC/Securities/SecuritiesListings/lists.md)
- **Range**: [Listing](/concepts/fibo/SEC/Securities/SecuritiesListings/Listing.md)

## Annotations

- **label**: is listed via
- **definition**: identifies the service responsible for listing the security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
