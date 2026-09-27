---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: strangle
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option trading strategy in which the investor holds a position in both a call and a put option with different strike
      prices, but with the same expiration date and underlying asset
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A strangle is a good strategy if you think the underlying security will experience a large price movement in the
      near future but are unsure of the direction. However, it is profitable mainly if the asset swings sharply in price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CallOption
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/PutOption
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionTradingStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Strangle
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: strangle
type: Ontology Class
---

# strangle

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Strangle>

## Definition

option trading strategy in which the investor holds a position in both a call and a put option with different strike prices, but with the same expiration date and underlying asset

## Relationships

- **Subclass of**: [OptionTradingStrategy](/concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [CallOption](/concepts/fibo/DER/DerivativesContracts/Options/CallOption.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [PutOption](/concepts/fibo/DER/DerivativesContracts/Options/PutOption.md)

## Annotations

- **label** (en): strangle
- **definition** (en): option trading strategy in which the investor holds a position in both a call and a put option with different strike prices, but with the same expiration date and underlying asset
- **explanatoryNote** (en): A strangle is a good strategy if you think the underlying security will experience a large price movement in the near future but are unsure of the direction. However, it is profitable mainly if the asset swings sharply in price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
