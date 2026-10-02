---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: supersedes
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a contract that was executed prior to and is replaced by this contract
  characteristics:
  - transitive
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
  range:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  - http://www.w3.org/2002/07/owl#TransitiveProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/supersedes
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: supersedes
type: Ontology Property
---

# supersedes

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/supersedes>

## Definition

indicates a contract that was executed prior to and is replaced by this contract

## Relationships

- **Domain**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **Range**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)

## Annotations

- **label**: supersedes
- **definition**: indicates a contract that was executed prior to and is replaced by this contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
