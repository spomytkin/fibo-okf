---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has record date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date on which the issuer checks to determine whether a party was on the company's books as a shareholder
      when required (i.e., they must have been on the books prior to the ex-dividend date), to identify who is eligible to
      receive the next dividend
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.investor.gov/introduction-investing/investing-basics/glossary/ex-dividend-dates-when-are-you-entitled-stock-and
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Companies also use this date to determine who is sent proxy statements, financial reports, and other information.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has date of record
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
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasRecordDate
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has record date
type: Ontology Property
---

# has record date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasRecordDate>

## Definition

indicates the date on which the issuer checks to determine whether a party was on the company's books as a shareholder when required (i.e., they must have been on the books prior to the ex-dividend date), to identify who is eligible to receive the next dividend

## Relationships

- **Domain**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)
- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label**: has record date
- **definition**: indicates the date on which the issuer checks to determine whether a party was on the company's books as a shareholder when required (i.e., they must have been on the books prior to the ex-dividend date), to identify who is eligible to receive the next dividend
- **adaptedFrom**: https://www.investor.gov/introduction-investing/investing-basics/glossary/ex-dividend-dates-when-are-you-entitled-stock-and
- **explanatoryNote**: Companies also use this date to determine who is sent proxy statements, financial reports, and other information.
- **synonym**: has date of record

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
