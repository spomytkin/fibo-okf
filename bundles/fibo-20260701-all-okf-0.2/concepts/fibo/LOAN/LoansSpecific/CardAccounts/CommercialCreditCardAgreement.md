---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commercial credit card agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit card agreement for a card issued to, or in conjunction with, a formal organization, such as a small business,
      middle market business, local, state, or national government, or large corporation
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.fdic.gov/regulations/examinations/credit_card/pdf_version/ch2.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Corporate card programs come in more than one form to serve different business needs. In general, they are contractual
      agreements between a sponsoring entity and a financial institution, in which the financial institution issues corporate
      cards to select employees of the sponsoring company.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: corporate credit card agreement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasBorrower
    value: N3f27664fb44b40c180a4d90432b6535c
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CommercialCreditCardAgreement
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: commercial credit card agreement
type: Ontology Class
---

# commercial credit card agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CommercialCreditCardAgreement>

## Definition

credit card agreement for a card issued to, or in conjunction with, a formal organization, such as a small business, middle market business, local, state, or national government, or large corporation

## Relationships

- **Subclass of**: [CreditCardAgreement](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement.md)

## Constraints

- **[hasBorrower](/concepts/fibo/FBC/DebtAndEquities/Debt/hasBorrower.md)**: some values from value `N3f27664fb44b40c180a4d90432b6535c`

## Annotations

- **label**: commercial credit card agreement
- **definition**: credit card agreement for a card issued to, or in conjunction with, a formal organization, such as a small business, middle market business, local, state, or national government, or large corporation
- **adaptedFrom**: https://www.fdic.gov/regulations/examinations/credit_card/pdf_version/ch2.pdf
- **explanatoryNote**: Corporate card programs come in more than one form to serve different business needs. In general, they are contractual agreements between a sponsoring entity and a financial institution, in which the financial institution issues corporate cards to select employees of the sponsoring company.
- **synonym**: corporate credit card agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
