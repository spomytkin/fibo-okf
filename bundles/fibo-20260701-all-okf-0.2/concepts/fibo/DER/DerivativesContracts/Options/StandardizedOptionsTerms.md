---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: standardized options terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: standardized contract terms established by a securities or options exchange or by an options clearing entity
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Such terms may relate to the underlying instruments, exercise price, expiration date, and contract size, for example.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher
    value: N3cbaf36bed3f4b82acc7830efc88aeba
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/VanillaOption
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StandardizedOptionsTerms
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: standardized options terms
type: Ontology Class
---

# standardized options terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StandardizedOptionsTerms>

## Definition

standardized contract terms established by a securities or options exchange or by an options clearing entity

## Relationships

- **Subclass of**: [StandardizedTerms](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md)

## Constraints

- **[hasPublisher](/concepts/fibo/BE/FunctionalEntities/Publishers/hasPublisher.md)**: some values from value `N3cbaf36bed3f4b82acc7830efc88aeba`
- **[hasPriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod.md)**: some values from of type [PriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [VanillaOption](/concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md)

## Annotations

- **label** (en): standardized options terms
- **definition** (en): standardized contract terms established by a securities or options exchange or by an options clearing entity
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.
- **explanatoryNote** (en): Such terms may relate to the underlying instruments, exercise price, expiration date, and contract size, for example.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
