---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: American depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depositary receipt that represents securities of a foreign company and allows that company's securities to trade
      in the U.S. financial markets
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, Accton Technology is traded on the Taiwanese exchange. In order for Accton Technology to be traded
      in the United States, Citibank, acting as a domestic custodian bank, purchases shares of Accton Technology and creates
      a security, ISIN US00437R1032, which can be traded on a U.S. exchange, in this case PORTAL. Note that the depositary
      shares do not have to equal the number of original shares. In the case of Accton Technology, one depositary share is
      equivalent to two original shares.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ADR
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Most ADRs are issued by a domestic custodian bank when the underlying securities are deposited in a foreign depositary
      bank, usually by a broker who has purchased the securities in the open market local to the foreign company. An ADR can
      represent a fraction of a share, a single share, or multiple shares of a foreign security. The holder of an ADR has
      the right to obtain the underlying foreign security that the ADR represents, but investors usually find it more convenient
      to own the ADR. The price of an ADR generally tracks the price of the foreign security in its home market, adjusted
      for the ratio of ADRs to foreign company shares. In the case of companies domiciled in the United Kingdom, creation
      of ADRs attracts a 1.5 percent creation fee; this creation fee is different than stamp duty reserve tax charge by the
      UK government. Depositary banks have various responsibilities to ADR holders and to the issuing foreign company the
      ADR represents.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn
    value: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevel
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/DepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: American depositary receipt
type: Ontology Class
---

# American depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt>

## Definition

depositary receipt that represents securities of a foreign company and allows that company's securities to trade in the U.S. financial markets

## Relationships

- **Subclass of**: [DepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md)

## Constraints

- **[isLegallyRecordedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction`
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: min qualified cardinality 0 of type [AmericanDepositaryReceiptLevel](/concepts/fibo/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevel.md)

## Annotations

- **label** (en): American depositary receipt
- **definition** (en): depositary receipt that represents securities of a foreign company and allows that company's securities to trade in the U.S. financial markets
- **example** (en): For example, Accton Technology is traded on the Taiwanese exchange. In order for Accton Technology to be traded in the United States, Citibank, acting as a domestic custodian bank, purchases shares of Accton Technology and creates a security, ISIN US00437R1032, which can be traded on a U.S. exchange, in this case PORTAL. Note that the depositary shares do not have to equal the number of original shares. In the case of Accton Technology, one depositary share is equivalent to two original shares.
- **abbreviation** (en): ADR
- **explanatoryNote** (en): Most ADRs are issued by a domestic custodian bank when the underlying securities are deposited in a foreign depositary bank, usually by a broker who has purchased the securities in the open market local to the foreign company. An ADR can represent a fraction of a share, a single share, or multiple shares of a foreign security. The holder of an ADR has the right to obtain the underlying foreign security that the ADR represents, but investors usually find it more convenient to own the ADR. The price of an ADR generally tracks the price of the foreign security in its home market, adjusted for the ratio of ADRs to foreign company shares. In the case of companies domiciled in the United Kingdom, creation of ADRs attracts a 1.5 percent creation fee; this creation fee is different than stamp duty reserve tax charge by the UK government. Depositary banks have various responsibilities to ADR holders and to the issuing foreign company the ADR represents.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
