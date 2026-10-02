---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has last trading date and time
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the last date and time that the security was traded on the exchange
  domain:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/Listing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDateTime
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasLastTradingDateTime
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: has last trading date and time
type: Ontology Property
---

# has last trading date and time

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasLastTradingDateTime>

## Definition

specifies the last date and time that the security was traded on the exchange

## Relationships

- **Domain**: [Listing](/concepts/fibo/SEC/Securities/SecuritiesListings/Listing.md)
- **Range**: [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)
- **Subproperty of**: [hasDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDateTime>)

## Annotations

- **label**: has last trading date and time
- **definition**: specifies the last date and time that the security was traded on the exchange

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
