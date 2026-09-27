---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: payment card agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: account-specific credit agreement that specifies the terms and conditions under which the payment card is offered
      to the cardholder by the issuer
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/Cardholder
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/IssuingFinancialInstitution
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAccount
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountSpecificServiceAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountSpecificServiceAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: payment card agreement
type: Ontology Class
---

# payment card agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement>

## Definition

account-specific credit agreement that specifies the terms and conditions under which the payment card is offered to the cardholder by the issuer

## Relationships

- **Subclass of**: [CreditAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- **Subclass of**: [AccountSpecificServiceAgreement](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountSpecificServiceAgreement.md)

## Constraints

- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [Cardholder](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/Cardholder.md)
- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [IssuingFinancialInstitution](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/IssuingFinancialInstitution.md)
- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: some values from of type [PaymentCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [CardAccount](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardAccount.md)

## Annotations

- **label**: payment card agreement
- **definition**: account-specific credit agreement that specifies the terms and conditions under which the payment card is offered to the cardholder by the issuer

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
