---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Indian depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: global depositary receipt that represents the purchase, or ownership, of foreign assets which are deposited in
      a Indian account managed by the Domestic Depository in India
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: IDR
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An Indian Depository Receipt (IDR) is an instrument denominated in Indian Rupees in the form of a depositary receipt
      created by a Domestic Depository (custodian of securities registered with the Securities and Exchange Board of India)
      against the underlying securities of issuing company to enable foreign companies to raise funds from the Indian securities
      Markets.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn
    value: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/SouthernAsiaGovernmentEntitiesAndJurisdictions/JurisdictionOfIndia
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://en.wikipedia.org/wiki/Indian_Depository_Receipt
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/IndianDepositoryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: Indian depositary receipt
type: Ontology Class
---

# Indian depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/IndianDepositoryReceipt>

## Definition

global depositary receipt that represents the purchase, or ownership, of foreign assets which are deposited in a Indian account managed by the Domestic Depository in India

## Relationships

- **See also**: [Indian_Depository_Receipt](<https://en.wikipedia.org/wiki/Indian_Depository_Receipt>)
- **Subclass of**: [GlobalDepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt.md)

## Constraints

- **[isLegallyRecordedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/SouthernAsiaGovernmentEntitiesAndJurisdictions/JurisdictionOfIndia`

## Annotations

- **label** (en): Indian depositary receipt
- **definition** (en): global depositary receipt that represents the purchase, or ownership, of foreign assets which are deposited in a Indian account managed by the Domestic Depository in India
- **abbreviation** (en): IDR
- **explanatoryNote** (en): An Indian Depository Receipt (IDR) is an instrument denominated in Indian Rupees in the form of a depositary receipt created by a Domestic Depository (custodian of securities registered with the Securities and Exchange Board of India) against the underlying securities of issuing company to enable foreign companies to raise funds from the Indian securities Markets.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
