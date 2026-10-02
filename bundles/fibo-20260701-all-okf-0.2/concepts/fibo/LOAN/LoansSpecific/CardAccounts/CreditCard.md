---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit card
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: card issued by a financial service provider that enables the cardholder to borrow funds
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.fdic.gov/regulations/examinations/credit_card/pdf_version/ch2.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In its non-physical form, a credit card represents a payment mechanism which facilitates both consumer and commercial
      business transactions, including purchases and cash advances. A credit card generally operates as a substitute for cash
      or a check and most often provides an unsecured revolving line of credit. The borrower is required to pay at least part
      of the card's outstanding balance each billing cycle, depending on the terms as set forth in the cardholder agreement.
      As the debt reduces, the available credit increases for accounts in good standing. These complex financial arrangements
      have ever-shifting terms and prices. A charge card differs from a credit card in that the charge card must be paid in
      full each month.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In physical form, a credit card traditionally is a thin, rectangular plastic card. The front of the card contains
      a series of numbers that are representative of various items such as the applicable network, bank, and account.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Issuance of credit cards has the condition that the cardholder will pay back the original, borrowed amount plus
      any additional agreed-upon charges. The credit company provider may also grant a line of credit (LOC) to the cardholder
      which allows the holder to borrow money in the form of a cash advance. The issuer pre-sets borrowing limits which have
      a basis on the individual's credit rating.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAccount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidenceFor
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardProduct
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCard
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: credit card
type: Ontology Class
---

# credit card

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCard>

## Definition

card issued by a financial service provider that enables the cardholder to borrow funds

## Relationships

- **Subclass of**: [PaymentCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md)

## Constraints

- **[isEvidenceFor](/concepts/fibo/FND/Agreements/Contracts/isEvidenceFor.md)**: exact qualified cardinality 1 of type [CreditCardAccount](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardAccount.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [CreditCardProduct](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardProduct.md)

## Annotations

- **label**: credit card
- **definition**: card issued by a financial service provider that enables the cardholder to borrow funds
- **adaptedFrom**: https://www.fdic.gov/regulations/examinations/credit_card/pdf_version/ch2.pdf
- **explanatoryNote**: In its non-physical form, a credit card represents a payment mechanism which facilitates both consumer and commercial business transactions, including purchases and cash advances. A credit card generally operates as a substitute for cash or a check and most often provides an unsecured revolving line of credit. The borrower is required to pay at least part of the card's outstanding balance each billing cycle, depending on the terms as set forth in the cardholder agreement. As the debt reduces, the available credit increases for accounts in good standing. These complex financial arrangements have ever-shifting terms and prices. A charge card differs from a credit card in that the charge card must be paid in full each month.
- **explanatoryNote**: In physical form, a credit card traditionally is a thin, rectangular plastic card. The front of the card contains a series of numbers that are representative of various items such as the applicable network, bank, and account.
- **explanatoryNote**: Issuance of credit cards has the condition that the cardholder will pay back the original, borrowed amount plus any additional agreed-upon charges. The credit company provider may also grant a line of credit (LOC) to the cardholder which allows the holder to borrow money in the form of a cash advance. The issuer pre-sets borrowing limits which have a basis on the individual's credit rating.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
