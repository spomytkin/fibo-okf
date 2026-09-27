---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a share to a dividend that applies to that share, or that the share may pay
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
  range:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Dividend
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has dividend
type: Ontology Property
---

# has dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividend>

## Definition

relates a share to a dividend that applies to that share, or that the share may pay

## Relationships

- **Domain**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)
- **Range**: [Dividend](/concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md)
- **Subproperty of**: [isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)

## Annotations

- **label**: has dividend
- **definition**: relates a share to a dividend that applies to that share, or that the share may pay

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
