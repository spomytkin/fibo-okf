---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Hong Kong depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: global depositary receipt that represents the purchase, or ownership, of foreign assets which are deposited in
      a depositary bank in Hong Kong
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: HKDR
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A Hong Kong Depositary Receipt (HDR) is a negotiable instrument issued by a depositary bank that evidences ownership
      of securities in a corporation organized outside Hong Kong. HDRs trade on the Hong Kong Stock Exchange (HKEx), thus
      enabling foreign issuers to tap the Hong Kong market and local investors to efficiently invest in quality international
      companies.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn
    value: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/EasternAsiaGovernmentEntitiesAndJurisdictions/JurisdictionOfHongKong
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/HongKongDepositaryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: Hong Kong depositary receipt
type: Ontology Class
---

# Hong Kong depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/HongKongDepositaryReceipt>

## Definition

global depositary receipt that represents the purchase, or ownership, of foreign assets which are deposited in a depositary bank in Hong Kong

## Relationships

- **Subclass of**: [GlobalDepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt.md)

## Constraints

- **[isLegallyRecordedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/EasternAsiaGovernmentEntitiesAndJurisdictions/JurisdictionOfHongKong`

## Annotations

- **label** (en): Hong Kong depositary receipt
- **definition** (en): global depositary receipt that represents the purchase, or ownership, of foreign assets which are deposited in a depositary bank in Hong Kong
- **abbreviation** (en): HKDR
- **explanatoryNote** (en): A Hong Kong Depositary Receipt (HDR) is a negotiable instrument issued by a depositary bank that evidences ownership of securities in a corporation organized outside Hong Kong. HDRs trade on the Hong Kong Stock Exchange (HKEx), thus enabling foreign issuers to tap the Hong Kong market and local investors to efficiently invest in quality international companies.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
