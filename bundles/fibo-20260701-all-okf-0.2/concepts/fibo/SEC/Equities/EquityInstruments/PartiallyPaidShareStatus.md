---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: partially paid share status
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: status indicating that only a portion of the market value has been received by the company for the shares
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the case of partially paid shares, the shareholder is still required to pay the remaining amount to the company.
      Typically, partially paid shares are only issued to a shareholder if there are compelling business reasons to do so.
  different_from:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/FullyPaidShareStatus.md
    predicate: http://www.w3.org/2002/07/owl#differentFrom
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/FullyPaidShareStatus
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SharePaymentStatus
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PartiallyPaidShareStatus
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: partially paid share status
type: Ontology Individual
---

# partially paid share status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PartiallyPaidShareStatus>

## Definition

status indicating that only a portion of the market value has been received by the company for the shares

## Relationships

- **Different from**: [FullyPaidShareStatus](/concepts/fibo/SEC/Equities/EquityInstruments/FullyPaidShareStatus.md)

## Annotations

- **label**: partially paid share status
- **definition**: status indicating that only a portion of the market value has been received by the company for the shares
- **explanatoryNote**: In the case of partially paid shares, the shareholder is still required to pay the remaining amount to the company. Typically, partially paid shares are only issued to a shareholder if there are compelling business reasons to do so.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
