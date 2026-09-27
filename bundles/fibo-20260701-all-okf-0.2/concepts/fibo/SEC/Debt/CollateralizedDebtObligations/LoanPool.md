---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt pool whose consituents are loans
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/DebtPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/LoanPool
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: loan pool
type: Ontology Class
---

# loan pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/LoanPool>

## Definition

debt pool whose consituents are loans

## Relationships

- **Subclass of**: [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [Loan](/concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md)

## Annotations

- **label** (en): loan pool
- **definition** (en): debt pool whose consituents are loans

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
