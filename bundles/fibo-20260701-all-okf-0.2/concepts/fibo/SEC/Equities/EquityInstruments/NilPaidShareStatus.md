---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: nil paid share status
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: status indicating that none of the market value has been received by the company for the shares
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Unpaid shares may be issued, for example, for convenience by a start-up company.
  different_from:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/FullyPaidShareStatus.md
    predicate: http://www.w3.org/2002/07/owl#differentFrom
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/FullyPaidShareStatus
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PartiallyPaidShareStatus.md
    predicate: http://www.w3.org/2002/07/owl#differentFrom
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PartiallyPaidShareStatus
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SharePaymentStatus
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NilPaidShareStatus
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: nil paid share status
type: Ontology Individual
---

# nil paid share status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NilPaidShareStatus>

## Definition

status indicating that none of the market value has been received by the company for the shares

## Relationships

- **Different from**: [FullyPaidShareStatus](/concepts/fibo/SEC/Equities/EquityInstruments/FullyPaidShareStatus.md)
- **Different from**: [PartiallyPaidShareStatus](/concepts/fibo/SEC/Equities/EquityInstruments/PartiallyPaidShareStatus.md)

## Annotations

- **label**: nil paid share status
- **definition**: status indicating that none of the market value has been received by the company for the shares
- **example**: Unpaid shares may be issued, for example, for convenience by a start-up company.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
