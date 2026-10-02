---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: moneyness
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for a derivative relating its strike price to the price of its underlying asset
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Moneyness describes the intrinsic value of an option in its current state. The term moneyness is most commonly
      used with put and call options and is an indicator as to the comparative value of the option with respect to its exercise/strike
      price. Moneyness can be measured with respect to the underlying stock or other asset's current/spot price or its future
      price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Moneyness
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: moneyness
type: Ontology Class
---

# moneyness

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Moneyness>

## Definition

classifier for a derivative relating its strike price to the price of its underlying asset

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)

## Annotations

- **label** (en): moneyness
- **definition** (en): classifier for a derivative relating its strike price to the price of its underlying asset
- **explanatoryNote** (en): Moneyness describes the intrinsic value of an option in its current state. The term moneyness is most commonly used with put and call options and is an indicator as to the comparative value of the option with respect to its exercise/strike price. Moneyness can be measured with respect to the underlying stock or other asset's current/spot price or its future price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
