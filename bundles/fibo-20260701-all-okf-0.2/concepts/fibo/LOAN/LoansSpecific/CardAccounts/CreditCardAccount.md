---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit card account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: card account whose terms and conditions are defined in a credit card agreement that is represented by a credit
      card
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/PaymentDueDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasPaymentDueDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardProduct
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCard
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isSignifiedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAccount
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAccount
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: credit card account
type: Ontology Class
---

# credit card account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAccount>

## Definition

card account whose terms and conditions are defined in a credit card agreement that is represented by a credit card

## Relationships

- **Subclass of**: [LoanOrCreditAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md)
- **Subclass of**: [CardAccount](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardAccount.md)

## Constraints

- **[hasPaymentDueDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasPaymentDueDate.md)**: some values from of type [PaymentDueDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/PaymentDueDate.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: some values from of type [CreditCardProduct](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardProduct.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [CreditCardAgreement](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement.md)
- **[isSignifiedBy](<https://www.omg.org/spec/Commons/Designators/isSignifiedBy>)**: some values from of type [CreditCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCard.md)

## Annotations

- **label**: credit card account
- **definition**: card account whose terms and conditions are defined in a credit card agreement that is represented by a credit card

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
