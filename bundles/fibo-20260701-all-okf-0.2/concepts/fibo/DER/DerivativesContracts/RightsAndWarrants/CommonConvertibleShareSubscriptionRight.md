---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: common convertible share subscription right
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subscription right entitling existing common convertible shareholders to subscribe to new securities at a price
      normally lower than the prevailing market price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nc451034455d741db8a9895389dbede84
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/SubscriptionRight.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/SubscriptionRight
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CommonConvertibleShareSubscriptionRight
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: common convertible share subscription right
type: Ontology Class
---

# common convertible share subscription right

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CommonConvertibleShareSubscriptionRight>

## Definition

subscription right entitling existing common convertible shareholders to subscribe to new securities at a price normally lower than the prevailing market price

## Relationships

- **Subclass of**: [SubscriptionRight](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/SubscriptionRight.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nc451034455d741db8a9895389dbede84`

## Annotations

- **label** (en): common convertible share subscription right
- **definition** (en): subscription right entitling existing common convertible shareholders to subscribe to new securities at a price normally lower than the prevailing market price
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
