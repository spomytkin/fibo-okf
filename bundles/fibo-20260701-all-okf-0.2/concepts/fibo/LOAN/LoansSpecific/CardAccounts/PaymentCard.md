---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: payment card
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal document issued by a financial services provider that enables the cardholder to access the funds in the customer's
      designated bank accounts, or through a credit account and make payments by electronic funds transfer and access automated
      teller machines (ATMs)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For purposes of Payment Card Industry Data Security Standard (PCI DSS), a payment card is any payment card/device
      that bears the logo of the founding members of PCI SSC, which are American Express, Discover Financial Services, JCB
      International, MasterCard, or Visa, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The term payment card includes credit cards, debit cards, and stored-value cards, as well as payment through any
      distinctive marks of a payment card (such as a credit card number). A payment card is issued under an agreement that
      provides standards and mechanisms for settling the transactions between a merchant acquiring bank or similar entity
      and the providers who accept the cards as payment.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAccount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidenceFor
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardExpirationDate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasExpirationDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/hasCardVerificationCode
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/hasPrimaryAccountNumber
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.irs.gov/payments/payment-card-transactions-faqs
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/LegalDocument
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: payment card
type: Ontology Class
---

# payment card

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard>

## Definition

legal document issued by a financial services provider that enables the cardholder to access the funds in the customer's designated bank accounts, or through a credit account and make payments by electronic funds transfer and access automated teller machines (ATMs)

## Relationships

- **See also**: [payment-card-transactions-faqs](<https://www.irs.gov/payments/payment-card-transactions-faqs>)
- **Subclass of**: [LegalDocument](<https://www.omg.org/spec/Commons/Documents/LegalDocument>)

## Constraints

- **[isEvidenceFor](/concepts/fibo/FND/Agreements/Contracts/isEvidenceFor.md)**: some values from of type [CardAccount](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardAccount.md)
- **[hasExpirationDate](/concepts/fibo/FND/Arrangements/Documents/hasExpirationDate.md)**: exact qualified cardinality 1 of type [CardExpirationDate](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardExpirationDate.md)
- **[hasCardVerificationCode](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/hasCardVerificationCode.md)**: exact qualified cardinality 1 of type [CardVerificationCodeValue](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue.md)
- **[hasPrimaryAccountNumber](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/hasPrimaryAccountNumber.md)**: exact qualified cardinality 1 of type [PrimaryCardAccountNumber](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber.md)

## Annotations

- **label**: payment card
- **definition**: legal document issued by a financial services provider that enables the cardholder to access the funds in the customer's designated bank accounts, or through a credit account and make payments by electronic funds transfer and access automated teller machines (ATMs)
- **explanatoryNote**: For purposes of Payment Card Industry Data Security Standard (PCI DSS), a payment card is any payment card/device that bears the logo of the founding members of PCI SSC, which are American Express, Discover Financial Services, JCB International, MasterCard, or Visa, Inc.
- **explanatoryNote**: The term payment card includes credit cards, debit cards, and stored-value cards, as well as payment through any distinctive marks of a payment card (such as a credit card number). A payment card is issued under an agreement that provides standards and mechanisms for settling the transactions between a merchant acquiring bank or similar entity and the providers who accept the cards as payment.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
