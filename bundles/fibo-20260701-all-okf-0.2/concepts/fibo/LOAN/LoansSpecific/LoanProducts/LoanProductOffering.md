---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan offering
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: offering related to a loan product that may be a tailored to particular circumstances, aimed at a group of borrowers
      or individual borrower
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LineItem
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProduct
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Offering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Offering
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProductOffering
sources:
- id: fibo-source-1b62e30b1c
  resource: references/fibo/LOAN/LoansSpecific/LoanProducts.rdf
  sha256: 1b62e30b1c3693cc85e718679f9b231242d1342cdfc54a4c99663db4f26a8644
  title: FIBO source LOAN/LoansSpecific/LoanProducts.rdf
title: loan offering
type: Ontology Class
---

# loan offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProductOffering>

## Definition

offering related to a loan product that may be a tailored to particular circumstances, aimed at a group of borrowers or individual borrower

## Relationships

- **Subclass of**: [Offering](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Offering.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: min qualified cardinality 0 of type [LineItem](/concepts/fibo/LOAN/LoansSpecific/LoanProducts/LineItem.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [LoanProduct](/concepts/fibo/LOAN/LoansSpecific/LoanProducts/LoanProduct.md)

## Annotations

- **label**: loan offering
- **definition**: offering related to a loan product that may be a tailored to particular circumstances, aimed at a group of borrowers or individual borrower

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
