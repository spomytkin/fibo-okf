---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: nil paid share
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: share whose payment status indicates that none of the market value has been received by the company for the shares
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasSharePaymentStatus
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NilPaidShareStatus
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NilPaidShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: nil paid share
type: Ontology Class
---

# nil paid share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NilPaidShare>

## Definition

share whose payment status indicates that none of the market value has been received by the company for the shares

## Relationships

- **Subclass of**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Constraints

- **[hasSharePaymentStatus](/concepts/fibo/SEC/Equities/EquityInstruments/hasSharePaymentStatus.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NilPaidShareStatus`

## Annotations

- **label** (en): nil paid share
- **definition** (en): share whose payment status indicates that none of the market value has been received by the company for the shares

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
