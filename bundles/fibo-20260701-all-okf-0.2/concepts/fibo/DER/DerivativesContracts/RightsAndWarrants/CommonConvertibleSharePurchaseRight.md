---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: common convertible share purchase right
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: purchase right that gives a prospective acquiree's common, convertible shareholders the right to buy common, convertible
      shares of the firm or common, convertible shares of anyone who acquires the firm at a deep discount to their fair market
      value
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N10f2e518f9a541da9c419a100832f0c5
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/PurchaseRight.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PurchaseRight
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CommonConvertibleSharePurchaseRight
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: common convertible share purchase right
type: Ontology Class
---

# common convertible share purchase right

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CommonConvertibleSharePurchaseRight>

## Definition

purchase right that gives a prospective acquiree's common, convertible shareholders the right to buy common, convertible shares of the firm or common, convertible shares of anyone who acquires the firm at a deep discount to their fair market value

## Relationships

- **Subclass of**: [PurchaseRight](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/PurchaseRight.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N10f2e518f9a541da9c419a100832f0c5`

## Annotations

- **label** (en): common convertible share purchase right
- **definition** (en): purchase right that gives a prospective acquiree's common, convertible shareholders the right to buy common, convertible shares of the firm or common, convertible shares of anyone who acquires the firm at a deep discount to their fair market value
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
