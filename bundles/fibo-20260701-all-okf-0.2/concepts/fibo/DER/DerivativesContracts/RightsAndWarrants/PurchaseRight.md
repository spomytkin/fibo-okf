---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: purchase right
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: anti-takeover device that gives a prospective acquiree's shareholders the right to buy shares of the firm or shares
      of anyone who acquires the firm at a deep discount to their fair market value
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The underlying is usually shares but this not necessarily the case. Also known as "Poison Pill".
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Entitlement
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PurchaseRight
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: purchase right
type: Ontology Class
---

# purchase right

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PurchaseRight>

## Definition

anti-takeover device that gives a prospective acquiree's shareholders the right to buy shares of the firm or shares of anyone who acquires the firm at a deep discount to their fair market value

## Relationships

- **Subclass of**: [Entitlement](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md)

## Annotations

- **label** (en): purchase right
- **definition** (en): anti-takeover device that gives a prospective acquiree's shareholders the right to buy shares of the firm or shares of anyone who acquires the firm at a deep discount to their fair market value
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): The underlying is usually shares but this not necessarily the case. Also known as "Poison Pill".

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
