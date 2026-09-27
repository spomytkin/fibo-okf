---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: listed share
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: share that is listed on at least one platform
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Listing requirements vary by exchange and include minimum stockholder's equity, a minimum share price and a minimum
      number of shareholders. Exchanges have listing requirements to ensure that only high quality securities are traded on
      them and to uphold the exchange's reputation among investors.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.investopedia.com/terms/l/listedsecurity.asp
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ListedShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: listed share
type: Ontology Class
---

# listed share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ListedShare>

## Definition

share that is listed on at least one platform

## Relationships

- **See also**: [listedsecurity.asp](<https://www.investopedia.com/terms/l/listedsecurity.asp>)
- **Subclass of**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)
- **Subclass of**: [ListedSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md)

## Annotations

- **label** (en): listed share
- **definition** (en): share that is listed on at least one platform
- **explanatoryNote** (en): Listing requirements vary by exchange and include minimum stockholder's equity, a minimum share price and a minimum number of shareholders. Exchanges have listing requirements to ensure that only high quality securities are traded on them and to uphold the exchange's reputation among investors.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
