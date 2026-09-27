---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has book depth
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates depth of the order book to which the price refers
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An order book is the list of orders (manual or electronic) that a trading venue (in particular stock exchanges)
      uses to record the interest of buyers and sellers in a particular financial instrument. The book depth refers to the
      number of price levels available at a particular time in the book. Sometimes the book is represented to a fixed depth,
      and orders beyond that depth are ignored or rejected, and in other cases the book can contain unlimited levels.
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#integer
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasBookDepth
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: has book depth
type: Ontology Property
---

# has book depth

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasBookDepth>

## Definition

indicates depth of the order book to which the price refers

## Relationships

- **Domain**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- **Range**: [integer](<http://www.w3.org/2001/XMLSchema#integer>)

## Annotations

- **label** (en): has book depth
- **definition** (en): indicates depth of the order book to which the price refers
- **explanatoryNote** (en): An order book is the list of orders (manual or electronic) that a trading venue (in particular stock exchanges) uses to record the interest of buyers and sellers in a particular financial instrument. The book depth refers to the number of price levels available at a particular time in the book. Sometimes the book is represented to a fixed depth, and orders beyond that depth are ignored or rejected, and in other cases the book can contain unlimited levels.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
