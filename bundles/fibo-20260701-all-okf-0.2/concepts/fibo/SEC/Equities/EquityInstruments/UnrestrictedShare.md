---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unrestricted share
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: share whose ownership/transfer/sale is not subject to special conditions including country-specific restrictions
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/UnrestrictedShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: unrestricted share
type: Ontology Class
---

# unrestricted share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/UnrestrictedShare>

## Definition

share whose ownership/transfer/sale is not subject to special conditions including country-specific restrictions

## Relationships

- **Subclass of**: [NegotiableSecurity](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity.md)
- **Subclass of**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Annotations

- **label** (en): unrestricted share
- **definition** (en): share whose ownership/transfer/sale is not subject to special conditions including country-specific restrictions

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
