---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has listing date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date on which a security is listed
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasListingDate
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: has listing date
type: Ontology Property
---

# has listing date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasListingDate>

## Definition

indicates the date on which a security is listed

## Relationships

- **Range**: [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label**: has listing date
- **definition**: indicates the date on which a security is listed

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
