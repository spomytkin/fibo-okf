---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has oversubscribe option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the holders of the rights instrument may get securities in the event that other right holders
      choose not to subscribe
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Entitlement
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/hasOversubscribeOption
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: has oversubscribe option
type: Ontology Property
---

# has oversubscribe option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/hasOversubscribeOption>

## Definition

indicates whether the holders of the rights instrument may get securities in the event that other right holders choose not to subscribe

## Relationships

- **Domain**: [Entitlement](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): has oversubscribe option
- **definition** (en): indicates whether the holders of the rights instrument may get securities in the event that other right holders choose not to subscribe

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
