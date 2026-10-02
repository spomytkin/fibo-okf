---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit card agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: account-specific credit facility that specifies the terms and conditions under which the credit card is offered
      to the cardholder by the issuer
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/Cardholder
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasBorrower
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/IssuingFinancialInstitution
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasLender
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCard
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAccount
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CommittedCreditFacility
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: credit card agreement
type: Ontology Class
---

# credit card agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement>

## Definition

account-specific credit facility that specifies the terms and conditions under which the credit card is offered to the cardholder by the issuer

## Relationships

- **Subclass of**: [CommittedCreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md)
- **Subclass of**: [PaymentCardAgreement](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement.md)

## Constraints

- **[hasBorrower](/concepts/fibo/FBC/DebtAndEquities/Debt/hasBorrower.md)**: some values from of type [Cardholder](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/Cardholder.md)
- **[hasLender](/concepts/fibo/FBC/DebtAndEquities/Debt/hasLender.md)**: some values from of type [IssuingFinancialInstitution](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/IssuingFinancialInstitution.md)
- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: some values from of type [CreditCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCard.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [CreditCardAccount](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardAccount.md)

## Annotations

- **label**: credit card agreement
- **definition**: account-specific credit facility that specifies the terms and conditions under which the credit card is offered to the cardholder by the issuer

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
