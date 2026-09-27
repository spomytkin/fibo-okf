---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has share class
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the class to which the share belongs, typically differentiated by privileges, such as voting rights
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Classes of shares, including shares in a mutual fund, are designated by name or a character (letter), such as A,
      B, C, etc. In the case of a mutual fund, different classes of shares may incur different fees and expenses.
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasShareClass
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has share class
type: Ontology Property
---

# has share class

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasShareClass>

## Definition

indicates the class to which the share belongs, typically differentiated by privileges, such as voting rights

## Relationships

- **Domain**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): has share class
- **definition** (en): indicates the class to which the share belongs, typically differentiated by privileges, such as voting rights
- **explanatoryNote** (en): Classes of shares, including shares in a mutual fund, are designated by name or a character (letter), such as A, B, C, etc. In the case of a mutual fund, different classes of shares may incur different fees and expenses.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
