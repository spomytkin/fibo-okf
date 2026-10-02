---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unsponsored depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depositary receipt that is established without the company's cooperation
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For an unsponsored ADR, a depositary entity can issue certificates when there's heavy demand from investors for
      ownership in a specific company from abroad. The issuing entity is normally a broker-dealer that owns common stock in
      the company. Because they're issued without the consent or cooperation of the foreign company, unsponsored ADRs generally
      trade over-the-counter (OTC)—rather than on a stock exchange. Also, shareholder benefits and voting rights may not be
      extended to the holders of these particular securities. Many large global corporations use unsponsored ADRs to attract
      American capital. For example, American investors can invest in Royal Mail PLC, a postal and delivery service company
      from the United Kingdom that was founded by Henry VIII. The company's unsponsored ADR trades OTC under the ticker symbol
      ROYMY.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/LevelIAmericanDepositaryReceipt
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/UnsponsoredDepositaryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: unsponsored depositary receipt
type: Ontology Class
---

# unsponsored depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/UnsponsoredDepositaryReceipt>

## Definition

depositary receipt that is established without the company's cooperation

## Relationships

- **Subclass of**: [AmericanDepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt.md)

## Constraints

- **Disjoint with**: [SponsoredDepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/LevelIAmericanDepositaryReceipt`

## Annotations

- **label** (en): unsponsored depositary receipt
- **definition** (en): depositary receipt that is established without the company's cooperation
- **explanatoryNote** (en): For an unsponsored ADR, a depositary entity can issue certificates when there's heavy demand from investors for ownership in a specific company from abroad. The issuing entity is normally a broker-dealer that owns common stock in the company. Because they're issued without the consent or cooperation of the foreign company, unsponsored ADRs generally trade over-the-counter (OTC)—rather than on a stock exchange. Also, shareholder benefits and voting rights may not be extended to the holders of these particular securities. Many large global corporations use unsponsored ADRs to attract American capital. For example, American investors can invest in Royal Mail PLC, a postal and delivery service company from the United Kingdom that was founded by Henry VIII. The company's unsponsored ADR trades OTC under the ticker symbol ROYMY.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
