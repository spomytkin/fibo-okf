---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has underlier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a derivative to something on which the contract is based
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: The domain of this property can be either a derivative instrument or, in the case of a swap contract, one leg of
      the swap.
  range:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Underlier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Underlier
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: has underlier
type: Ontology Property
---

# has underlier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier>

## Definition

relates a derivative to something on which the contract is based

## Relationships

- **Range**: [Underlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Underlier.md)
- **Subproperty of**: [hasUndergoer](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer>)

## Annotations

- **label**: has underlier
- **definition**: relates a derivative to something on which the contract is based
- **usageNote**: The domain of this property can be either a derivative instrument or, in the case of a swap contract, one leg of the swap.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
