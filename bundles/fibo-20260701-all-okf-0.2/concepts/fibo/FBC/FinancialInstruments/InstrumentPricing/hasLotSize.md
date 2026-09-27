---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has lot size
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: magnitude of an item (i.e., total quantity)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, with respect to corn, 5000 bushels is a typical contract size. For some oil commodities trades, 1000
      barrels is considered a single contract. For equity options, the lot size is typically 100 shares of the underlying.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The lot size, referenced in offerings, listings, orders, and trades, typically refers to the number of shares or
      units in a single contract.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasLotSize
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: has lot size
type: Ontology Property
---

# has lot size

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasLotSize>

## Definition

magnitude of an item (i.e., total quantity)

## Relationships

- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **Subproperty of**: [hasNumericValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue>)

## Annotations

- **label** (en): has lot size
- **definition** (en): magnitude of an item (i.e., total quantity)
- **example** (en): For example, with respect to corn, 5000 bushels is a typical contract size. For some oil commodities trades, 1000 barrels is considered a single contract. For equity options, the lot size is typically 100 shares of the underlying.
- **explanatoryNote** (en): The lot size, referenced in offerings, listings, orders, and trades, typically refers to the number of shares or units in a single contract.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
