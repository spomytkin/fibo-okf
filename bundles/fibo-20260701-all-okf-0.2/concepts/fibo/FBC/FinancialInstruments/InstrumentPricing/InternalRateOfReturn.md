---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: internal rate of return
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: discount rate that results in a net present value (NPV) of zero for a series of future cash flows
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This concept is central to many definitions of debt instrument analytics, and is the inverse of net present value.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/RateOfReturn.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/RateOfReturn
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/InternalRateOfReturn
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: internal rate of return
type: Ontology Class
---

# internal rate of return

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/InternalRateOfReturn>

## Definition

discount rate that results in a net present value (NPV) of zero for a series of future cash flows

## Relationships

- **Subclass of**: [RateOfReturn](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/RateOfReturn.md)

## Annotations

- **label** (en): internal rate of return
- **definition** (en): discount rate that results in a net present value (NPV) of zero for a series of future cash flows
- **explanatoryNote** (en): This concept is central to many definitions of debt instrument analytics, and is the inverse of net present value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
