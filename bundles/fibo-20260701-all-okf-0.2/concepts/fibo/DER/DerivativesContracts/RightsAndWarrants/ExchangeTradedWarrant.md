---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exchange-traded warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that is listed on a securities exchange
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/PublicWarrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PublicWarrant
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/ExchangeTradedWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: exchange-traded warrant
type: Ontology Class
---

# exchange-traded warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/ExchangeTradedWarrant>

## Definition

warrant that is listed on a securities exchange

## Relationships

- **Subclass of**: [PublicWarrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/PublicWarrant.md)
- **Subclass of**: [ListedSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md)

## Annotations

- **label** (en): exchange-traded warrant
- **definition** (en): warrant that is listed on a securities exchange

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
