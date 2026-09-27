---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: payment obligation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legally enforceable duty to pay a sum of money according to the terms stated in a contract
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: the duty of a borrower to repay a loan, related to the legal right of a lender to enforce payment
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/isObligationOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payee
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Commitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Commitment
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Duty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Duty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation
sources:
- id: fibo-source-53130861ea
  resource: references/fibo/FND/ProductsAndServices/PaymentsAndSchedules.rdf
  sha256: 53130861eac6d2084e3ddb6496db6123d851e37aa0259feed44cd96fd48920cf
  title: FIBO source FND/ProductsAndServices/PaymentsAndSchedules.rdf
title: payment obligation
type: Ontology Class
---

# payment obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation>

## Definition

legally enforceable duty to pay a sum of money according to the terms stated in a contract

## Relationships

- **Subclass of**: [Commitment](/concepts/fibo/FND/Agreements/Agreements/Commitment.md)
- **Subclass of**: [Duty](/concepts/fibo/FND/Law/LegalCapacity/Duty.md)

## Constraints

- **[isObligationOf](/concepts/fibo/FND/Agreements/Agreements/isObligationOf.md)**: some values from of type [Payer](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md)
- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: all values from of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Payee](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payee.md)

## Annotations

- **label**: payment obligation
- **definition**: legally enforceable duty to pay a sum of money according to the terms stated in a contract
- **example**: the duty of a borrower to repay a loan, related to the legal right of a lender to enforce payment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
