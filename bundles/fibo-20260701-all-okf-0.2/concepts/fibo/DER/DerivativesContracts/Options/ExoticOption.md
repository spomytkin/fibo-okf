---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exotic option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option that has a non-standard payout structure or other feature
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Commodity Futures Trading Commission (CFTC) glossary, https://www.cftc.gov/LearnAndProtect/EducationCenter/CFTCGlossary/glossary_e.html
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Exotic options include Asian options and lookback options, and are mostly traded in the over-the-counter market.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: exotic option
type: Ontology Class
---

# exotic option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption>

## Definition

option that has a non-standard payout structure or other feature

## Relationships

- **Subclass of**: [OverTheCounterDerivativeInstrument](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md)
- **Subclass of**: [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)

## Annotations

- **label** (en): exotic option
- **definition** (en): option that has a non-standard payout structure or other feature
- **adaptedFrom** (en): Commodity Futures Trading Commission (CFTC) glossary, https://www.cftc.gov/LearnAndProtect/EducationCenter/CFTCGlossary/glossary_e.html
- **explanatoryNote** (en): Exotic options include Asian options and lookback options, and are mostly traded in the over-the-counter market.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
