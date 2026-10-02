---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is seasoned
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates that the security has been publicly traded long enough to eliminate any short-term volume volatility
      from its initial public offering
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Short-term volatility may be with respect to price or trading volume.
  domain:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isSeasoned
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: is seasoned
type: Ontology Property
---

# is seasoned

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isSeasoned>

## Definition

indicates that the security has been publicly traded long enough to eliminate any short-term volume volatility from its initial public offering

## Relationships

- **Domain**: [ListedSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is seasoned
- **definition**: indicates that the security has been publicly traded long enough to eliminate any short-term volume volatility from its initial public offering
- **explanatoryNote**: Short-term volatility may be with respect to price or trading volume.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
