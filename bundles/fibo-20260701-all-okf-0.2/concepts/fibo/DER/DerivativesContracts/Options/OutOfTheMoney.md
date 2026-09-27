---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: out-of-the-money
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: moneyness classifier that refers to an option whose value in terms of its strike price is not favorable in comparison
      to the prevailing market price of the underlying asset
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: OTM
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An OTM call option will have a strike price that is higher than the market price of the underlying asset. Alternatively,
      an OTM put option has a strike price that is lower than the market price of the underlying asset.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Moneyness
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OutOfTheMoney
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: out-of-the-money
type: Ontology Individual
---

# out-of-the-money

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OutOfTheMoney>

## Definition

moneyness classifier that refers to an option whose value in terms of its strike price is not favorable in comparison to the prevailing market price of the underlying asset

## Annotations

- **label** (en): out-of-the-money
- **definition** (en): moneyness classifier that refers to an option whose value in terms of its strike price is not favorable in comparison to the prevailing market price of the underlying asset
- **abbreviation** (en): OTM
- **explanatoryNote** (en): An OTM call option will have a strike price that is higher than the market price of the underlying asset. Alternatively, an OTM put option has a strike price that is lower than the market price of the underlying asset.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
