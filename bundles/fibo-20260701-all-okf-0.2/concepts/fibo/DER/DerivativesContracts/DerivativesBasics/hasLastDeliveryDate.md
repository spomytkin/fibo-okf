---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has last delivery date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the final date in a range of dates by which the underlying asset (or some portion thereof) must be delivered
      in order for the terms of the contract to be fulfilled
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/hasLastDeliveryDate
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: has last delivery date
type: Ontology Property
---

# has last delivery date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/hasLastDeliveryDate>

## Definition

specifies the final date in a range of dates by which the underlying asset (or some portion thereof) must be delivered in order for the terms of the contract to be fulfilled

## Relationships

- **Domain**: [SettlementTerms](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasEndDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label** (en): has last delivery date
- **definition** (en): specifies the final date in a range of dates by which the underlying asset (or some portion thereof) must be delivered in order for the terms of the contract to be fulfilled

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
