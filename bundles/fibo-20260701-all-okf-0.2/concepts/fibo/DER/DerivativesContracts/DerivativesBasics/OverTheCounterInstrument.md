---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: over-the-counter instrument
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument and bilateral contract that is not listed on an organized exchange
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: OTC instrument
  disjoint_with:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/OverTheCounterInstrument
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: over-the-counter instrument
type: Ontology Class
---

# over-the-counter instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/OverTheCounterInstrument>

## Definition

financial instrument and bilateral contract that is not listed on an organized exchange

## Relationships

- **Subclass of**: [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Constraints

- **Disjoint with**: [ListedSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md)

## Annotations

- **label**: over-the-counter instrument
- **definition**: financial instrument and bilateral contract that is not listed on an organized exchange
- **abbreviation**: OTC instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
