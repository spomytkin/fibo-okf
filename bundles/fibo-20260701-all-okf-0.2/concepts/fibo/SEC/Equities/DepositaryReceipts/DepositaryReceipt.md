---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: negotiable financial instrument issued by a trust company, security depositary, or bank that is evidence of the
      deposit of publicly traded securities and that facilitates the ownership of securities traded in other jurisdictions
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: DR
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Depositary receipts are widely used in order to allow the trading of securities in jurisdictions other than

      the one where the original securities were issued, such as in a local market. Depositary receipts facilitate buying
      securities in foreign companies, because the securities do not have to leave the home country. They enable domestic
      investors to buy securities of foreign companies without the accompanying risks or inconveniences of cross-border and
      cross-currency transactions.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: depositary receipt
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/hasMultiplier
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/hasTradedSecurity
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/DepositaryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: depositary receipt
type: Ontology Class
---

# depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/DepositaryReceipt>

## Definition

negotiable financial instrument issued by a trust company, security depositary, or bank that is evidence of the deposit of publicly traded securities and that facilitates the ownership of securities traded in other jurisdictions

## Relationships

- **Subclass of**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Constraints

- **[hasMultiplier](/concepts/fibo/SEC/Equities/DepositaryReceipts/hasMultiplier.md)**: min qualified cardinality 0 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[hasTradedSecurity](/concepts/fibo/SEC/Equities/DepositaryReceipts/hasTradedSecurity.md)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label** (en): depositary receipt
- **definition** (en): negotiable financial instrument issued by a trust company, security depositary, or bank that is evidence of the deposit of publicly traded securities and that facilitates the ownership of securities traded in other jurisdictions
- **abbreviation** (en): DR
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): Depositary receipts are widely used in order to allow the trading of securities in jurisdictions other than the one where the original securities were issued, such as in a local market. Depositary receipts facilitate buying securities in foreign companies, because the securities do not have to leave the home country. They enable domestic investors to buy securities of foreign companies without the accompanying risks or inconveniences of cross-border and cross-currency transactions.
- **synonym** (en): depositary receipt

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
