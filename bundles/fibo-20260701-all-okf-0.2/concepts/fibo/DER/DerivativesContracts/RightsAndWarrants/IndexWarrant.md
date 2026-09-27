---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: index warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that permits the holder to acquire a specified amount based on the performance of an index during a specified
      period at a specified price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N3eef70515cea4115b9bf0226a7759970
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/IndexWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: index warrant
type: Ontology Class
---

# index warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/IndexWarrant>

## Definition

warrant that permits the holder to acquire a specified amount based on the performance of an index during a specified period at a specified price

## Relationships

- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N3eef70515cea4115b9bf0226a7759970`

## Annotations

- **label** (en): index warrant
- **definition** (en): warrant that permits the holder to acquire a specified amount based on the performance of an index during a specified period at a specified price
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
