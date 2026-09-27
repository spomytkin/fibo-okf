---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: home equity line of credit pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt pool consisting of home equity loans
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgagePool.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgagePool
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/HomeEquityLineOfCredit
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasPart
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/DebtPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/HomeEquityLineOfCreditPool
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: home equity line of credit pool
type: Ontology Class
---

# home equity line of credit pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/HomeEquityLineOfCreditPool>

## Definition

debt pool consisting of home equity loans

## Relationships

- **Subclass of**: [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)

## Constraints

- **Disjoint with**: [MortgagePool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgagePool.md)
- **[hasPart](<https://www.omg.org/spec/Commons/Collections/hasPart>)**: some values from of type [HomeEquityLineOfCredit](/concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/HomeEquityLineOfCredit.md)

## Annotations

- **label** (en): home equity line of credit pool
- **definition** (en): debt pool consisting of home equity loans

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
