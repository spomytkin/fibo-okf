---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial exposure
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the extent to which an individual or organization is open to risk of suffering a loss in a transaction, or with
      respect to some investment or set of investments, e.g., some holding; the amount one stands to lose in that transaction
      or investment
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples in banking include the total amount of unsecured loans, the amount of loans advanced to a single borrower,
      group, industry, or country, and the probability of loss from devaluation, revaluation, or foreign exchange fluctuations.
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: Financial exposure may be related to a holding, involving ownership, or may involve rights or obligations related
      to borrowing or derivatives.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialExposure
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: financial exposure
type: Ontology Class
---

# financial exposure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialExposure>

## Definition

the extent to which an individual or organization is open to risk of suffering a loss in a transaction, or with respect to some investment or set of investments, e.g., some holding; the amount one stands to lose in that transaction or investment

## Relationships

- **Subclass of**: [Exposure](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure.md)

## Annotations

- **label**: financial exposure
- **definition**: the extent to which an individual or organization is open to risk of suffering a loss in a transaction, or with respect to some investment or set of investments, e.g., some holding; the amount one stands to lose in that transaction or investment
- **example**: Examples in banking include the total amount of unsecured loans, the amount of loans advanced to a single borrower, group, industry, or country, and the probability of loss from devaluation, revaluation, or foreign exchange fluctuations.
- **note**: Financial exposure may be related to a holding, involving ownership, or may involve rights or obligations related to borrowing or derivatives.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
