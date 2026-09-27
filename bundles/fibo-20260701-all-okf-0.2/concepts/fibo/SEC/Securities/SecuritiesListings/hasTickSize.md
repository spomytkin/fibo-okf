---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has tick size
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a minimum price movement for the security with respect to an exchange
  domain:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/Listing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasTickSize
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: has tick size
type: Ontology Property
---

# has tick size

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasTickSize>

## Definition

specifies a minimum price movement for the security with respect to an exchange

## Relationships

- **Domain**: [Listing](/concepts/fibo/SEC/Securities/SecuritiesListings/Listing.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label** (en): has tick size
- **definition** (en): specifies a minimum price movement for the security with respect to an exchange

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
