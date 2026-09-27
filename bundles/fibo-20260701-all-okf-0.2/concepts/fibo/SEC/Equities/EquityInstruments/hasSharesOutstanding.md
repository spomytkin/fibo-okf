---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has shares outstanding
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the number of shares currently held by shareholders, including those held by retail investors, institutional
      investors and insiders, and typically available for trading
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The number of outstanding shares is used in calculating key metrics such as a company's market capitalization,
      as well as its earnings per share (EPS) and cash flow per share (CFPS).
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasAmount
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasSharesOutstanding
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has shares outstanding
type: Ontology Property
---

# has shares outstanding

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasSharesOutstanding>

## Definition

indicates the number of shares currently held by shareholders, including those held by retail investors, institutional investors and insiders, and typically available for trading

## Relationships

- **Range**: [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **Subproperty of**: [hasAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md)

## Annotations

- **label** (en): has shares outstanding
- **definition** (en): indicates the number of shares currently held by shareholders, including those held by retail investors, institutional investors and insiders, and typically available for trading
- **explanatoryNote** (en): The number of outstanding shares is used in calculating key metrics such as a company's market capitalization, as well as its earnings per share (EPS) and cash flow per share (CFPS).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
