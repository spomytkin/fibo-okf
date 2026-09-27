---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: student loan pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt pool consisting of student loans
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/StudentLoan
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasPart
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/DebtPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/StudentLoanPool
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
title: student loan pool
type: Ontology Class
---

# student loan pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/StudentLoanPool>

## Definition

debt pool consisting of student loans

## Relationships

- **Subclass of**: [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)

## Constraints

- **[hasPart](<https://www.omg.org/spec/Commons/Collections/hasPart>)**: some values from of type [StudentLoan](/concepts/fibo/LOAN/LoansSpecific/StudentLoans/StudentLoan.md)

## Annotations

- **label** (en): student loan pool
- **definition** (en): debt pool consisting of student loans

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
