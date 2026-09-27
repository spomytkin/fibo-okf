---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit facility
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit agreement that allows the borrower to periodically take out money over an extended period of time rather
      than reapplying for a loan every time they need funds
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Credit facilities include revolving loans/lines of credit, committed facilities, letters of credit, and most retail
      credit accounts. They may define sub-facilities to which the lender is prepared to commit for specific purposes.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: master commitment
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ConditionPrecedent
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/SubFacility
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditFacility
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: credit facility
type: Ontology Class
---

# credit facility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditFacility>

## Definition

credit agreement that allows the borrower to periodically take out money over an extended period of time rather than reapplying for a loan every time they need funds

## Relationships

- **Subclass of**: [CreditAgreementRepaidPeriodically](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)

## Constraints

- **[hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: min qualified cardinality 0 of type [ConditionPrecedent](/concepts/fibo/FND/Agreements/Contracts/ConditionPrecedent.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: min qualified cardinality 0 of type [SubFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/SubFacility.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [PromissoryNote](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md)

## Annotations

- **label** (en): credit facility
- **definition** (en): credit agreement that allows the borrower to periodically take out money over an extended period of time rather than reapplying for a loan every time they need funds
- **explanatoryNote** (en): Credit facilities include revolving loans/lines of credit, committed facilities, letters of credit, and most retail credit accounts. They may define sub-facilities to which the lender is prepared to commit for specific purposes.
- **synonym** (en): master commitment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
