---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has multiplier
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the number of underlying shares (whether multiple or fractional) represented by a single depositary receipt
  domain:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/DepositaryReceipt
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/hasMultiplier
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: has multiplier
type: Ontology Property
---

# has multiplier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/hasMultiplier>

## Definition

indicates the number of underlying shares (whether multiple or fractional) represented by a single depositary receipt

## Relationships

- **Domain**: [DepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md)
- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label** (en): has multiplier
- **definition** (en): indicates the number of underlying shares (whether multiple or fractional) represented by a single depositary receipt

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
