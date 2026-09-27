---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: private warrant
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that is not tradable
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/NonNegotiableSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/NonNegotiableSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PrivateWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: private warrant
type: Ontology Class
---

# private warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PrivateWarrant>

## Definition

warrant that is not tradable

## Relationships

- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)
- **Subclass of**: [NonNegotiableSecurity](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/NonNegotiableSecurity.md)

## Annotations

- **label**: private warrant
- **definition**: warrant that is not tradable

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
