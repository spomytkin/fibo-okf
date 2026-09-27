---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: swaption
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: over-the-counter option that confers the right but not the obligation, to enter into a swap transaction at some
      time in the future
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A swaption, also known as a swap option, refers to an option to enter into an interest rate swap or some other
      type of swap. In exchange for an options premium, the buyer gains the right but not the obligation to enter into a specified
      swap agreement with the issuer on a specified future date.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: swap option
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nff5e284fdbbf439ca8e63bf7aec515f6
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/Swaption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: swaption
type: Ontology Class
---

# swaption

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/Swaption>

## Definition

over-the-counter option that confers the right but not the obligation, to enter into a swap transaction at some time in the future

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nff5e284fdbbf439ca8e63bf7aec515f6`

## Annotations

- **label** (en): swaption
- **definition** (en): over-the-counter option that confers the right but not the obligation, to enter into a swap transaction at some time in the future
- **explanatoryNote** (en): A swaption, also known as a swap option, refers to an option to enter into an interest rate swap or some other type of swap. In exchange for an options premium, the buyer gains the right but not the obligation to enter into a specified swap agreement with the issuer on a specified future date.
- **synonym** (en): swap option

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
