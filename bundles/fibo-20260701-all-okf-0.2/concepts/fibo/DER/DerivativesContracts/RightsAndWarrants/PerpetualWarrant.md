---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: perpetual warrant
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant without an expiration date, giving the holder the right, but not the obligation, to buy (call warrant)
      or to sell (put warrant) an underlying asset at a certain strike price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The strike price, in the case of a perpetual warrant, is usually higher than the market value of the underlying
      asset at the time of issue.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PerpetualWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: perpetual warrant
type: Ontology Class
---

# perpetual warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PerpetualWarrant>

## Definition

warrant without an expiration date, giving the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant) an underlying asset at a certain strike price

## Relationships

- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)

## Annotations

- **label**: perpetual warrant
- **definition**: warrant without an expiration date, giving the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant) an underlying asset at a certain strike price
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): The strike price, in the case of a perpetual warrant, is usually higher than the market value of the underlying asset at the time of issue.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
