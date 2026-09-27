---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has underlying asset price
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a price for something on which the contract is based
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/hasUnderlyingAssetPrice
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: has underlying asset price
type: Ontology Property
---

# has underlying asset price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/hasUnderlyingAssetPrice>

## Definition

specifies a price for something on which the contract is based

## Relationships

- **Range**: [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **Subproperty of**: [hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)

## Annotations

- **label**: has underlying asset price
- **definition**: specifies a price for something on which the contract is based

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
