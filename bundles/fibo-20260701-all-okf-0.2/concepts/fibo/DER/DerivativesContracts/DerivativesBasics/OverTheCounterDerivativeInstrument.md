---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: ISO 4914:2021(en), Financial services - Unique product identifier (UPI)
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: over-the-counter derivative instrument
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: derivative instrument that is not listed on an organized exchange
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ISO 4914 defines an OTC derivative instrument as a financial instrument that is, or would be, identified by an
      ISIN with the prefix 'EZ' or 'ZZ'. Details regarding how the prefix of an ISIN is determined can be found in ISO 6166:2020,
      Annex A.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: OTC derivative instrument
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/OverTheCounterInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/OverTheCounterInstrument
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: over-the-counter derivative instrument
type: Ontology Class
---

# over-the-counter derivative instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument>

## Definition

derivative instrument that is not listed on an organized exchange

## Relationships

- **Subclass of**: [OverTheCounterInstrument](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/OverTheCounterInstrument.md)
- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Annotations

- **source**: ISO 4914:2021(en), Financial services - Unique product identifier (UPI)
- **label**: over-the-counter derivative instrument
- **definition**: derivative instrument that is not listed on an organized exchange
- **note**: ISO 4914 defines an OTC derivative instrument as a financial instrument that is, or would be, identified by an ISIN with the prefix 'EZ' or 'ZZ'. Details regarding how the prefix of an ISIN is determined can be found in ISO 6166:2020, Annex A.
- **abbreviation**: OTC derivative instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
