---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: capped option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option with an established profit cap or cap price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The cap price is equal to the option's strike price plus a cap interval for a call option or the strike price minus
      a cap interval for a put option. A capped option is automatically exercised when the underlying security closes at or
      above (for a call) or at or below (for a put) the option's cap price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasCapPrice
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/VanillaOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CappedOption
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: capped option
type: Ontology Class
---

# capped option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CappedOption>

## Definition

option with an established profit cap or cap price

## Relationships

- **Subclass of**: [VanillaOption](/concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md)

## Constraints

- **[hasCapPrice](/concepts/fibo/DER/DerivativesContracts/Options/hasCapPrice.md)**: some values from of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)

## Annotations

- **label** (en): capped option
- **definition** (en): option with an established profit cap or cap price
- **explanatoryNote** (en): The cap price is equal to the option's strike price plus a cap interval for a call option or the strike price minus a cap interval for a put option. A capped option is automatically exercised when the underlying security closes at or above (for a call) or at or below (for a put) the option's cap price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
