---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has conversion ratio
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the factor used to determine the number of warrants needed in order to buy or sell a specific number
      of securities or investment units
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Entitlement
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/hasConversionRatio
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: has conversion ratio
type: Ontology Property
---

# has conversion ratio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/hasConversionRatio>

## Definition

indicates the factor used to determine the number of warrants needed in order to buy or sell a specific number of securities or investment units

## Relationships

- **Domain**: [Entitlement](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md)
- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **Subproperty of**: [hasNumericValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue>)

## Annotations

- **label** (en): has conversion ratio
- **definition** (en): indicates the factor used to determine the number of warrants needed in order to buy or sell a specific number of securities or investment units

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
