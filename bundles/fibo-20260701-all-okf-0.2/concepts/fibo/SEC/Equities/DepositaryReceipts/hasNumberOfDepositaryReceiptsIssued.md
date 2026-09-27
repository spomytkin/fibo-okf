---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has number of depositary receipts issued
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the number of receipts issued to the general public
  domain:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/DepositaryReceipt
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#positiveInteger
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/hasNumberOfDepositaryReceiptsIssued
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: has number of depositary receipts issued
type: Ontology Property
---

# has number of depositary receipts issued

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/hasNumberOfDepositaryReceiptsIssued>

## Definition

indicates the number of receipts issued to the general public

## Relationships

- **Domain**: [DepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md)
- **Range**: [positiveInteger](<http://www.w3.org/2001/XMLSchema#positiveInteger>)

## Annotations

- **label** (en): has number of depositary receipts issued
- **definition** (en): indicates the number of receipts issued to the general public

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
