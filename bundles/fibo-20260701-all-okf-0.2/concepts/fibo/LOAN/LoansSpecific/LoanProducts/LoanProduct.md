---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan product
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial product that is realized as a loan that a party may acquire from a lending institution with specific
      characteristics and terms
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isExemplifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ConditionPrecedent
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/hasPreconditions
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditFacility
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProduct
sources:
- id: fibo-source-1b62e30b1c
  resource: references/fibo/LOAN/LoansSpecific/LoanProducts.rdf
  sha256: 1b62e30b1c3693cc85e718679f9b231242d1342cdfc54a4c99663db4f26a8644
  title: FIBO source LOAN/LoansSpecific/LoanProducts.rdf
title: loan product
type: Ontology Class
---

# loan product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProduct>

## Definition

financial product that is realized as a loan that a party may acquire from a lending institution with specific characteristics and terms

## Relationships

- **Subclass of**: [CreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md)
- **Subclass of**: [FinancialProduct](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md)

## Constraints

- **[isExemplifiedBy](/concepts/fibo/FND/Relations/Relations/isExemplifiedBy.md)**: min qualified cardinality 0 of type [Loan](/concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md)
- **[hasPreconditions](/concepts/fibo/LOAN/LoansSpecific/LoanProducts/hasPreconditions.md)**: min qualified cardinality 0 of type [ConditionPrecedent](/concepts/fibo/FND/Agreements/Contracts/ConditionPrecedent.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: min qualified cardinality 0 of type [Collateral](/concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md)

## Annotations

- **label**: loan product
- **definition**: financial product that is realized as a loan that a party may acquire from a lending institution with specific characteristics and terms

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
