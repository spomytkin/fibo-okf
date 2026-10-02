---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exotic warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that gives the holder the right (but not the obligation) to buy (or sometimes sell) an underlying asset
      under non-standard or complex conditions, often involving additional features not found in a plain vanilla (standard)
      warrant
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Exotic warrants may be created by investment banks as part of structured products to meet specific investor needs.
      They are often identified with an 'X' in their English stock short name.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Features of an exotic warrant may include (1) non-standard payoffs, such as path-dependent or condition-based payouts,
      (2) variations in the underlying asset(s), which may include equities, indices, currencies, interest rates, baskets
      of assets, etc., and (3) embedded optionality in terms of features such as barriers, lookbacks, digitals, or dual-currency
      terms.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/ExoticWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: exotic warrant
type: Ontology Class
---

# exotic warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/ExoticWarrant>

## Definition

warrant that gives the holder the right (but not the obligation) to buy (or sometimes sell) an underlying asset under non-standard or complex conditions, often involving additional features not found in a plain vanilla (standard) warrant

## Relationships

- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)

## Annotations

- **label** (en): exotic warrant
- **definition** (en): warrant that gives the holder the right (but not the obligation) to buy (or sometimes sell) an underlying asset under non-standard or complex conditions, often involving additional features not found in a plain vanilla (standard) warrant
- **explanatoryNote** (en): Exotic warrants may be created by investment banks as part of structured products to meet specific investor needs. They are often identified with an 'X' in their English stock short name.
- **explanatoryNote** (en): Features of an exotic warrant may include (1) non-standard payoffs, such as path-dependent or condition-based payouts, (2) variations in the underlying asset(s), which may include equities, indices, currencies, interest rates, baskets of assets, etc., and (3) embedded optionality in terms of features such as barriers, lookbacks, digitals, or dual-currency terms.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
