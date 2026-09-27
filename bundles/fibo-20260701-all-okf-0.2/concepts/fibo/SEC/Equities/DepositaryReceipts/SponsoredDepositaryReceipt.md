---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sponsored depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depositary receipt that is issued in collaboration with the foreign company enabling them to tap into international
      capital markets directly
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Although a sponsored ADR would be listed in the United States, the issuing company still has its revenue and profit
      denominated in its home currency.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: sponsored depositary receipt
type: Ontology Class
---

# sponsored depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt>

## Definition

depositary receipt that is issued in collaboration with the foreign company enabling them to tap into international capital markets directly

## Relationships

- **Subclass of**: [AmericanDepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt.md)

## Annotations

- **label** (en): sponsored depositary receipt
- **definition** (en): depositary receipt that is issued in collaboration with the foreign company enabling them to tap into international capital markets directly
- **explanatoryNote** (en): Although a sponsored ADR would be listed in the United States, the issuing company still has its revenue and profit denominated in its home currency.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
