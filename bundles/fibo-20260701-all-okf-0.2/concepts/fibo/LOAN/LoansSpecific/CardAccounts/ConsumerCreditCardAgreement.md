---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: consumer credit card agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit card agreement for a card issued for household, family, or other personal expenditures that is accessed
      by a borrower's use of a credit card
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.law.cornell.edu/cfr/text/12/228.12
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Consumer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasBorrower
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement
  - concept: /concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/UnsecuredConsumerLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/UnsecuredConsumerLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/ConsumerCreditCardAgreement
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: consumer credit card agreement
type: Ontology Class
---

# consumer credit card agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/ConsumerCreditCardAgreement>

## Definition

credit card agreement for a card issued for household, family, or other personal expenditures that is accessed by a borrower's use of a credit card

## Relationships

- **Subclass of**: [CreditCardAgreement](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement.md)
- **Subclass of**: [UnsecuredConsumerLoan](/concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/UnsecuredConsumerLoan.md)

## Constraints

- **[hasBorrower](/concepts/fibo/FBC/DebtAndEquities/Debt/hasBorrower.md)**: some values from of type [Consumer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Consumer.md)

## Annotations

- **label**: consumer credit card agreement
- **definition**: credit card agreement for a card issued for household, family, or other personal expenditures that is accessed by a borrower's use of a credit card
- **adaptedFrom**: https://www.law.cornell.edu/cfr/text/12/228.12

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
