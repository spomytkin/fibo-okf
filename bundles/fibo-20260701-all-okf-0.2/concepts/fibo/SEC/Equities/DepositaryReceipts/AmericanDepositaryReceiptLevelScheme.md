---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: American depositary receipt level scheme
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for American depositary receipts that categorizes ADRs into levels based on the extent to which the
      foreign company has access to the U.S. market
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ADR level
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevel
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevelScheme
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: American depositary receipt level scheme
type: Ontology Class
---

# American depositary receipt level scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevelScheme>

## Definition

classifier for American depositary receipts that categorizes ADRs into levels based on the extent to which the foreign company has access to the U.S. market

## Relationships

- **Subclass of**: [FinancialInstrumentClassificationScheme](/concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme.md)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [AmericanDepositaryReceiptLevel](/concepts/fibo/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevel.md)

## Annotations

- **label** (en): American depositary receipt level scheme
- **definition** (en): classifier for American depositary receipts that categorizes ADRs into levels based on the extent to which the foreign company has access to the U.S. market
- **abbreviation** (en): ADR level

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
