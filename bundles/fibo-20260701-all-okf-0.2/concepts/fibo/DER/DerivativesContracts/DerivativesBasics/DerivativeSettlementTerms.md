---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: derivative settlement terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: settlement terms specifying additional details with respect to what is to be delivered when, to whom, under what
      conditions at the time of settlement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/hasAdditionalCosts
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/hasUnderlyingAssetPrice
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeSettlementTerms
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: derivative settlement terms
type: Ontology Class
---

# derivative settlement terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeSettlementTerms>

## Definition

settlement terms specifying additional details with respect to what is to be delivered when, to whom, under what conditions at the time of settlement

## Relationships

- **Subclass of**: [DerivativeTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)
- **Subclass of**: [SettlementTerms](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)

## Constraints

- **[hasAdditionalCosts](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/hasAdditionalCosts.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasUnderlyingAssetPrice](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/hasUnderlyingAssetPrice.md)**: min qualified cardinality 0 of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)

## Annotations

- **label**: derivative settlement terms
- **definition**: settlement terms specifying additional details with respect to what is to be delivered when, to whom, under what conditions at the time of settlement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
