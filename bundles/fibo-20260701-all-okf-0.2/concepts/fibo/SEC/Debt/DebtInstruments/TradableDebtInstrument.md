---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tradable debt instrument
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a debt instrument that is also a security, i.e., that can be bought and sold by the holder
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Details from Ecofin: A [debt] instrument can be traded, if its features depend only on one borrower. If the instrument
      has no bilateral or multilateral obligations, the investor can easily transfer it to another investor without asking
      the borrower (except the terms prohibit this explicitly). This is simplified with securitised instruments, where the
      debt is already split into handy denominations which trade easily (e.g. in round thousands or millions as with bonds,
      commercial paper, etc.). But in principle it works also with interbank loans and similar instruments. FIBIM Definition:
      Financial instruments evidencing moneys owed by the issuer to the holder on terms as specified.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasGuarantor
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasYield
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/isSubordinatedTo
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: tradable debt instrument
type: Ontology Class
---

# tradable debt instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument>

## Definition

a debt instrument that is also a security, i.e., that can be bought and sold by the holder

## Relationships

- **Subclass of**: [DebtInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)
- **Subclass of**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Constraints

- **[hasGuarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/hasGuarantor.md)**: min qualified cardinality 0 of type [Guarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guarantor.md)
- **[hasYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/hasYield.md)**: some values from of type [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)
- **[isSubordinatedTo](/concepts/fibo/SEC/Debt/DebtInstruments/isSubordinatedTo.md)**: min qualified cardinality 0 of type [TradableDebtInstrument](/concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)

## Annotations

- **label**: tradable debt instrument
- **definition**: a debt instrument that is also a security, i.e., that can be bought and sold by the holder
- **explanatoryNote**: Details from Ecofin: A [debt] instrument can be traded, if its features depend only on one borrower. If the instrument has no bilateral or multilateral obligations, the investor can easily transfer it to another investor without asking the borrower (except the terms prohibit this explicitly). This is simplified with securitised instruments, where the debt is already split into handy denominations which trade easily (e.g. in round thousands or millions as with bonds, commercial paper, etc.). But in principle it works also with interbank loans and similar instruments. FIBIM Definition: Financial instruments evidencing moneys owed by the issuer to the holder on terms as specified.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
