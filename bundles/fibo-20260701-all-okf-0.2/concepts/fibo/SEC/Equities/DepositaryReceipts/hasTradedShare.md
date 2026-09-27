---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has traded share
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a depositary receipt to the instrument (equity or exchange-traded fund) that it represents
  domain:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/DepositaryReceipt
  range:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/hasTradedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/hasTradedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/hasTradedShare
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: has traded share
type: Ontology Property
---

# has traded share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/hasTradedShare>

## Definition

links a depositary receipt to the instrument (equity or exchange-traded fund) that it represents

## Relationships

- **Domain**: [DepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md)
- **Range**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)
- **Subproperty of**: [hasTradedSecurity](/concepts/fibo/SEC/Equities/DepositaryReceipts/hasTradedSecurity.md)

## Annotations

- **label** (en): has traded share
- **definition** (en): links a depositary receipt to the instrument (equity or exchange-traded fund) that it represents

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
