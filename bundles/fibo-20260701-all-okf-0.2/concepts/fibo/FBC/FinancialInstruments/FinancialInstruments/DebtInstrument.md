---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt instrument
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument and credit agreement evidencing monies owed by the issuer to the holder on terms as specified
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth
      edition, 2019-10.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Borrower
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasBorrower
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Lender
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasLender
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasRedemptionProvision
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/DebtOffering
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasOffering
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasCallFeature
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasInterestPaymentTerms
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutFeature
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasPutFeature
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRepaymentTerms
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: debt instrument
type: Ontology Class
---

# debt instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument>

## Definition

financial instrument and credit agreement evidencing monies owed by the issuer to the holder on terms as specified

## Relationships

- **Subclass of**: [CreditAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- **Subclass of**: [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Constraints

- **[hasBorrower](/concepts/fibo/FBC/DebtAndEquities/Debt/hasBorrower.md)**: some values from of type [Borrower](/concepts/fibo/FBC/DebtAndEquities/Debt/Borrower.md)
- **[hasLender](/concepts/fibo/FBC/DebtAndEquities/Debt/hasLender.md)**: some values from of type [Lender](/concepts/fibo/FBC/DebtAndEquities/Debt/Lender.md)
- **[hasRedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasRedemptionProvision.md)**: min qualified cardinality 0 of type [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- **[hasOffering](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/hasOffering.md)**: min qualified cardinality 0 of type [DebtOffering](/concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md)
- **[hasCallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/hasCallFeature.md)**: min qualified cardinality 0 of type [CallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md)
- **[hasInterestPaymentTerms](/concepts/fibo/SEC/Debt/DebtInstruments/hasInterestPaymentTerms.md)**: some values from of type [InterestPaymentTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md)
- **[hasPutFeature](/concepts/fibo/SEC/Debt/DebtInstruments/hasPutFeature.md)**: min qualified cardinality 0 of type [PutFeature](/concepts/fibo/SEC/Debt/DebtInstruments/PutFeature.md)
- **[hasRepaymentTerms](/concepts/fibo/SEC/Debt/DebtInstruments/hasRepaymentTerms.md)**: some values from of type [PrincipalRepaymentTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md)

## Annotations

- **label**: debt instrument
- **definition**: financial instrument and credit agreement evidencing monies owed by the issuer to the holder on terms as specified
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth edition, 2019-10.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
