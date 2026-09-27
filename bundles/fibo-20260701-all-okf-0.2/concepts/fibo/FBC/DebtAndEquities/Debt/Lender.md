---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lender
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a party that extends credit or money to a borrower with the expectation of being repaid, usually with interest
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N3056530e27054b1da4c3325f82e1d4fc
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Creditor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Creditor
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Lender
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: lender
type: Ontology Class
---

# lender

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Lender>

## Definition

a party that extends credit or money to a borrower with the expectation of being repaid, usually with interest

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [Creditor](/concepts/fibo/FBC/DebtAndEquities/Debt/Creditor.md)
- **Subclass of**: [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N3056530e27054b1da4c3325f82e1d4fc`

## Annotations

- **label**: lender
- **definition**: a party that extends credit or money to a borrower with the expectation of being repaid, usually with interest

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
