---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has calculation agent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a party (role) responsible for determining the value of an instrument
  range:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CalculationAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CalculationAgent
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasCalculationAgent
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: has calculation agent
type: Ontology Property
---

# has calculation agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasCalculationAgent>

## Definition

indicates a party (role) responsible for determining the value of an instrument

## Relationships

- **Range**: [CalculationAgent](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CalculationAgent.md)
- **Subproperty of**: [isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)

## Annotations

- **label** (en): has calculation agent
- **definition**: indicates a party (role) responsible for determining the value of an instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
