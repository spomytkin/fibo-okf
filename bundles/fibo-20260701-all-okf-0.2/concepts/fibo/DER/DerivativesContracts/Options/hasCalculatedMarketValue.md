---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has calculated market value
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a calculated price as of some relative date considered the market value of the option at that point in
      time
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has premium
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
  range:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/OptionPremium.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionPremium
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasCalculatedMarketValue
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: has calculated market value
type: Ontology Property
---

# has calculated market value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasCalculatedMarketValue>

## Definition

indicates a calculated price as of some relative date considered the market value of the option at that point in time

## Relationships

- **Domain**: [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)
- **Range**: [OptionPremium](/concepts/fibo/DER/DerivativesContracts/Options/OptionPremium.md)
- **Subproperty of**: [hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)

## Annotations

- **label** (en): has calculated market value
- **definition** (en): indicates a calculated price as of some relative date considered the market value of the option at that point in time
- **synonym** (en): has premium

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
