---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: convertible common share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: common share that is convertible into another security
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/CommonShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/CommonShare
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ConvertibleCommonShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: convertible common share
type: Ontology Class
---

# convertible common share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ConvertibleCommonShare>

## Definition

common share that is convertible into another security

## Relationships

- **Subclass of**: [CommonShare](/concepts/fibo/SEC/Equities/EquityInstruments/CommonShare.md)
- **Subclass of**: [ConvertibleSecurity](/concepts/fibo/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity.md)

## Annotations

- **label**: convertible common share
- **definition**: common share that is convertible into another security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
