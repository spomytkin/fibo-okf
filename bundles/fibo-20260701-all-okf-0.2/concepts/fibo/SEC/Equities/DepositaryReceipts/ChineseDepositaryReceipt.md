---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Chinese depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: global depositary receipt that represents ownership in the securities of a non-Chinese company that trades on a
      public exchange in China
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CDR
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: It refers to shares in non-Chinese companies that trade in China the same way that American depositary receipts
      (ADRs) allow non-U.S. company shares to trade on American exchanges.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn
    value: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/EasternAsiaGovernmentEntitiesAndJurisdictions/JurisdictionOfTheRepublicOfChina
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/ChineseDepositaryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: Chinese depositary receipt
type: Ontology Class
---

# Chinese depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/ChineseDepositaryReceipt>

## Definition

global depositary receipt that represents ownership in the securities of a non-Chinese company that trades on a public exchange in China

## Relationships

- **Subclass of**: [GlobalDepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt.md)

## Constraints

- **[isLegallyRecordedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/EasternAsiaGovernmentEntitiesAndJurisdictions/JurisdictionOfTheRepublicOfChina`

## Annotations

- **label** (en): Chinese depositary receipt
- **definition** (en): global depositary receipt that represents ownership in the securities of a non-Chinese company that trades on a public exchange in China
- **abbreviation** (en): CDR
- **explanatoryNote** (en): It refers to shares in non-Chinese companies that trade in China the same way that American depositary receipts (ADRs) allow non-U.S. company shares to trade on American exchanges.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
