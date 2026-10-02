---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Luxembourg depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: global depositary receipt that represents the purchase, or ownership, of foreign assets which are deposited in
      a Luxembourg-based account
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LDR
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A Luxembourg Depositary Receipt (LDR) is a certificate which represents the purchase, or ownership, of foreign
      assets which are deposited in a Luxembourg-based account. An LDR functions in much the same way as a global depositary
      receipt (GDR). LDRs may represent ownership of either an underlying number of shares or a notional amount of bonds.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn
    value: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions/JurisdictionOfLuxembourg
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/LuxembourgDepositaryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: Luxembourg depositary receipt
type: Ontology Class
---

# Luxembourg depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/LuxembourgDepositaryReceipt>

## Definition

global depositary receipt that represents the purchase, or ownership, of foreign assets which are deposited in a Luxembourg-based account

## Relationships

- **Subclass of**: [GlobalDepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt.md)

## Constraints

- **[isLegallyRecordedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions/JurisdictionOfLuxembourg`

## Annotations

- **label** (en): Luxembourg depositary receipt
- **definition** (en): global depositary receipt that represents the purchase, or ownership, of foreign assets which are deposited in a Luxembourg-based account
- **abbreviation** (en): LDR
- **explanatoryNote** (en): A Luxembourg Depositary Receipt (LDR) is a certificate which represents the purchase, or ownership, of foreign assets which are deposited in a Luxembourg-based account. An LDR functions in much the same way as a global depositary receipt (GDR). LDRs may represent ownership of either an underlying number of shares or a notional amount of bonds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
