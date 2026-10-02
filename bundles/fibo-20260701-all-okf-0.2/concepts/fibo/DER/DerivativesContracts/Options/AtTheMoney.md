---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: at-the-money
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: moneyness classifier that refers to an option whose value in terms of its strike price is the same or close to
      the current market price of the underlying security
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ATM
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An ATM option has a delta of ±0.50, positive if it is a call, negative for a put.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Moneyness
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/AtTheMoney
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: at-the-money
type: Ontology Individual
---

# at-the-money

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/AtTheMoney>

## Definition

moneyness classifier that refers to an option whose value in terms of its strike price is the same or close to the current market price of the underlying security

## Annotations

- **label** (en): at-the-money
- **definition** (en): moneyness classifier that refers to an option whose value in terms of its strike price is the same or close to the current market price of the underlying security
- **abbreviation** (en): ATM
- **explanatoryNote** (en): An ATM option has a delta of ±0.50, positive if it is a call, negative for a put.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
