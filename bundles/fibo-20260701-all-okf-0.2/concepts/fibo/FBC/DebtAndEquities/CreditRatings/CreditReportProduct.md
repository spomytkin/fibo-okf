---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit report product
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: branded credit report offered in the marketplace
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isProducedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/OffTheShelfProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/OffTheShelfProduct
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReportProduct
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: credit report product
type: Ontology Class
---

# credit report product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReportProduct>

## Definition

branded credit report offered in the marketplace

## Relationships

- **Subclass of**: [FinancialProduct](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md)
- **Subclass of**: [OffTheShelfProduct](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/OffTheShelfProduct.md)

## Constraints

- **[isProducedBy](/concepts/fibo/FND/Relations/Relations/isProducedBy.md)**: some values from of type [CreditRatingAgency](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md)

## Annotations

- **label**: credit report product
- **definition**: branded credit report offered in the marketplace

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
