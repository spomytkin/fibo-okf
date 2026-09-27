---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: participatory note
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: tradable debt instrument that facilitates the ownership of securities traded in other jurisdictions
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Participation notes are required by investors or hedge funds to invest in Indian securities without having to register
      with the Securities and Exchange Board of India (SEBI). P-Notes are among the group of investments considered to be
      Offshore Derivative Investments (ODIs) in Indian markets.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: P-Note
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: PN
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Depository receipts are widely used in order to allow the trading of debt instruments in

      jurisdictions other than the one where the original debt instruments were issued'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Typically P-Notes are SPVs that are created to allow participation from outside that market. The SPV purchases
      a security on shore and issues a note that represents that security to offshore investors. They are similar to an ADR
      but always a debt security.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: participation note
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/hasTradedSecurity
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/DepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/ParticipatoryNote
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: participatory note
type: Ontology Class
---

# participatory note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/ParticipatoryNote>

## Definition

tradable debt instrument that facilitates the ownership of securities traded in other jurisdictions

## Relationships

- **Subclass of**: [TradableDebtInstrument](/concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)
- **Subclass of**: [DepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md)

## Constraints

- **[hasTradedSecurity](/concepts/fibo/SEC/Equities/DepositaryReceipts/hasTradedSecurity.md)**: some values from of type [TradableDebtInstrument](/concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)

## Annotations

- **label** (en): participatory note
- **definition** (en): tradable debt instrument that facilitates the ownership of securities traded in other jurisdictions
- **example** (en): Participation notes are required by investors or hedge funds to invest in Indian securities without having to register with the Securities and Exchange Board of India (SEBI). P-Notes are among the group of investments considered to be Offshore Derivative Investments (ODIs) in Indian markets.
- **abbreviation** (en): P-Note
- **abbreviation** (en): PN
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): Depository receipts are widely used in order to allow the trading of debt instruments in jurisdictions other than the one where the original debt instruments were issued
- **explanatoryNote** (en): Typically P-Notes are SPVs that are created to allow participation from outside that market. The SPV purchases a security on shore and issues a note that represents that security to offshore investors. They are similar to an ADR but always a debt security.
- **synonym** (en): participation note

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
