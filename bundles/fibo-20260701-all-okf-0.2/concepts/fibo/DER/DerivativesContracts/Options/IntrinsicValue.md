---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: intrinsic value
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of what an asset is worth, i.e. with respect to its current price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This measure is arrived at by means of an objective calculation or complex financial model. In financial analysis
      this term is used in conjunction with the work of identifying, as nearly as possible, the underlying value of a company
      and its cash flow. In options pricing it refers to the difference between the strike price of the option and the current
      price of the underlying asset.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/IntrinsicValue
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: intrinsic value
type: Ontology Class
---

# intrinsic value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/IntrinsicValue>

## Definition

measure of what an asset is worth, i.e. with respect to its current price

## Relationships

- **Subclass of**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label** (en): intrinsic value
- **definition** (en): measure of what an asset is worth, i.e. with respect to its current price
- **explanatoryNote** (en): This measure is arrived at by means of an objective calculation or complex financial model. In financial analysis this term is used in conjunction with the work of identifying, as nearly as possible, the underlying value of a company and its cash flow. In options pricing it refers to the difference between the strike price of the option and the current price of the underlying asset.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
