---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cumulative preferred share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share whose dividends, if not paid on time, accumulate until paid out
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These dividends have precedence over ordinary dividends which cannot be paid until any cumulative dividend obligations
      have been paid. Dividends are typically deferred due to insufficient earnings or other business reasons.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/CumulativePreferredShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: cumulative preferred share
type: Ontology Class
---

# cumulative preferred share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/CumulativePreferredShare>

## Definition

preferred share whose dividends, if not paid on time, accumulate until paid out

## Relationships

- **Subclass of**: [PreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md)

## Annotations

- **label**: cumulative preferred share
- **definition**: preferred share whose dividends, if not paid on time, accumulate until paid out
- **explanatoryNote**: These dividends have precedence over ordinary dividends which cannot be paid until any cumulative dividend obligations have been paid. Dividends are typically deferred due to insufficient earnings or other business reasons.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
