---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has ex-dividend date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a date on which a stock 'goes ex-dividend', typically about three weeks before the dividend is paid to
      shareholders of record
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.investor.gov/introduction-investing/investing-basics/glossary/ex-dividend-dates-when-are-you-entitled-stock-and
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Once the company sets the record date, the ex-dividend date is set based on stock exchange rules. If you purchase
      a stock on its ex-dividend date or after, you will not receive the next dividend payment.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Shares listed on the New York Stock Exchange go ex-dividend four business days prior to the record date.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has ex-date
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has expected dividend date
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
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasExDividendDate
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has ex-dividend date
type: Ontology Property
---

# has ex-dividend date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasExDividendDate>

## Definition

indicates a date on which a stock 'goes ex-dividend', typically about three weeks before the dividend is paid to shareholders of record

## Relationships

- **Domain**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)
- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label**: has ex-dividend date
- **definition**: indicates a date on which a stock 'goes ex-dividend', typically about three weeks before the dividend is paid to shareholders of record
- **adaptedFrom**: https://www.investor.gov/introduction-investing/investing-basics/glossary/ex-dividend-dates-when-are-you-entitled-stock-and
- **explanatoryNote**: Once the company sets the record date, the ex-dividend date is set based on stock exchange rules. If you purchase a stock on its ex-dividend date or after, you will not receive the next dividend payment.
- **explanatoryNote**: Shares listed on the New York Stock Exchange go ex-dividend four business days prior to the record date.
- **synonym**: has ex-date
- **synonym**: has expected dividend date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
