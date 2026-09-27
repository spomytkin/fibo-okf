---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has declaration date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a date on which an organization states that a dividend payment may be anticipated, including the the
      dividend amount and the ex-dividend and payment dates
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has announcement date
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividendDeclarationDate
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has declaration date
type: Ontology Property
---

# has declaration date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividendDeclarationDate>

## Definition

indicates a date on which an organization states that a dividend payment may be anticipated, including the the dividend amount and the ex-dividend and payment dates

## Relationships

- **Domain**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)
- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label**: has declaration date
- **definition**: indicates a date on which an organization states that a dividend payment may be anticipated, including the the dividend amount and the ex-dividend and payment dates
- **synonym**: has announcement date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
