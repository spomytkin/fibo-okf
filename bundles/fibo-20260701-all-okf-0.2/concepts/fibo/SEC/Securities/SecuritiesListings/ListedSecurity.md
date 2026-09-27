---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: listed security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registered security listed on at least one exchange
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: exchange-traded security
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: One can, as appropriate, multiply classify a share as being a common share and listed share, and, in the case whereby
      multiple securities are issued in different currencies (i.e., there are multiple listed shares corresponding to a given
      common share that have different identifiers, including more than one ISIN, CUSIP, share class FIGI), multiply classify
      the listed share individuals as individuals of the same common share.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasHomeExchange
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasOriginalPlaceOfListing
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isListedVia
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/RegisteredSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/RegisteredSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: listed security
type: Ontology Class
---

# listed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity>

## Definition

registered security listed on at least one exchange

## Relationships

- **Subclass of**: [RegisteredSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/RegisteredSecurity.md)

## Constraints

- **[hasHomeExchange](/concepts/fibo/SEC/Securities/SecuritiesListings/hasHomeExchange.md)**: exact qualified cardinality 1 of type [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)
- **[hasOriginalPlaceOfListing](/concepts/fibo/SEC/Securities/SecuritiesListings/hasOriginalPlaceOfListing.md)**: exact qualified cardinality 1 of type [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)
- **[isListedVia](/concepts/fibo/SEC/Securities/SecuritiesListings/isListedVia.md)**: some values from of type [Listing](/concepts/fibo/SEC/Securities/SecuritiesListings/Listing.md)

## Annotations

- **label**: listed security
- **definition**: registered security listed on at least one exchange
- **synonym**: exchange-traded security
- **usageNote**: One can, as appropriate, multiply classify a share as being a common share and listed share, and, in the case whereby multiple securities are issued in different currencies (i.e., there are multiple listed shares corresponding to a given common share that have different identifiers, including more than one ISIN, CUSIP, share class FIGI), multiply classify the listed share individuals as individuals of the same common share.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
