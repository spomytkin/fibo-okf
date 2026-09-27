---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: spot contract
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument that settles for immediate delivery on a specified date
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A spot transaction is a transaction in which some goods or instrument(s) are exchanged for some other goods or
      instruments, including currency, with no future delivery provision, i.e., within the minimum number of days possible.
      Examples include currency spots and commodity spot transactions, whose settlement convention is determined by the relevant
      market.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/SpotContract
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: spot contract
type: Ontology Class
---

# spot contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/SpotContract>

## Definition

financial instrument that settles for immediate delivery on a specified date

## Relationships

- **Subclass of**: [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Annotations

- **label** (en): spot contract
- **definition** (en): financial instrument that settles for immediate delivery on a specified date
- **explanatoryNote** (en): A spot transaction is a transaction in which some goods or instrument(s) are exchanged for some other goods or instruments, including currency, with no future delivery provision, i.e., within the minimum number of days possible. Examples include currency spots and commodity spot transactions, whose settlement convention is determined by the relevant market.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
