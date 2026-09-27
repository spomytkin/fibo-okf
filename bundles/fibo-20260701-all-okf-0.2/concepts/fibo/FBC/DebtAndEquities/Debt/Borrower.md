---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: borrower
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party to a credit agreement that is obligated to repay the amount borrowed (principal) with interest and other
      fees according to the terms of the instrument
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debt
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/owes
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nc65c502e1fdd40d38c26f4699ad2daf9
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Debtor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debtor
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Customer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Customer
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Borrower
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: borrower
type: Ontology Class
---

# borrower

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Borrower>

## Definition

party to a credit agreement that is obligated to repay the amount borrowed (principal) with interest and other fees according to the terms of the instrument

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [Debtor](/concepts/fibo/FBC/DebtAndEquities/Debt/Debtor.md)
- **Subclass of**: [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)
- **Subclass of**: [Customer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Customer.md)

## Constraints

- **[owes](/concepts/fibo/FBC/DebtAndEquities/Debt/owes.md)**: some values from of type [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt/Debt.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nc65c502e1fdd40d38c26f4699ad2daf9`

## Annotations

- **label**: borrower
- **definition**: party to a credit agreement that is obligated to repay the amount borrowed (principal) with interest and other fees according to the terms of the instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
