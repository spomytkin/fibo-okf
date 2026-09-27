---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mortgage product
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isExemplifiedBy
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/LoanProducts/LoanProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProduct
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/MortgageProduct
sources:
- id: fibo-source-1b62e30b1c
  resource: references/fibo/LOAN/LoansSpecific/LoanProducts.rdf
  sha256: 1b62e30b1c3693cc85e718679f9b231242d1342cdfc54a4c99663db4f26a8644
  title: FIBO source LOAN/LoansSpecific/LoanProducts.rdf
title: mortgage product
type: Ontology Class
---

# mortgage product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/MortgageProduct>

## Relationships

- **Subclass of**: [LoanProduct](/concepts/fibo/LOAN/LoansSpecific/LoanProducts/LoanProduct.md)

## Constraints

- **[isExemplifiedBy](/concepts/fibo/FND/Relations/Relations/isExemplifiedBy.md)**: min qualified cardinality 0 of type [LoanSecuredByRealEstate](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)

## Annotations

- **label** (en): mortgage product

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
