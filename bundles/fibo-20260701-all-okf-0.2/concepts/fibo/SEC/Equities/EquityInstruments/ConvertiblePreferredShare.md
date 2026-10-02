---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: convertible preferred share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share that includes an option for the holder to convert the shares into a fixed number of common shares
      after a predetermined date
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Most convertible preferred stock is exchanged at the request of the shareholder, but sometimes there is a provision
      that allows the company, or issuer, to force conversion. The value of a convertible preferred stock is ultimately based
      on the performance of the common stock.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ConvertiblePreferredShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: convertible preferred share
type: Ontology Class
---

# convertible preferred share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ConvertiblePreferredShare>

## Definition

preferred share that includes an option for the holder to convert the shares into a fixed number of common shares after a predetermined date

## Relationships

- **Subclass of**: [PreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md)
- **Subclass of**: [ConvertibleSecurity](/concepts/fibo/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity.md)

## Annotations

- **label**: convertible preferred share
- **definition**: preferred share that includes an option for the holder to convert the shares into a fixed number of common shares after a predetermined date
- **explanatoryNote**: Most convertible preferred stock is exchanged at the request of the shareholder, but sometimes there is a provision that allows the company, or issuer, to force conversion. The value of a convertible preferred stock is ultimately based on the performance of the common stock.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
