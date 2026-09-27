---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has counterparty
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a party to a contract, typically not the contract principal
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
  range:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Counterparty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasCounterparty
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has counterparty
type: Ontology Property
---

# has counterparty

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasCounterparty>

## Definition

identifies a party to a contract, typically not the contract principal

## Relationships

- **Domain**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **Range**: [Counterparty](/concepts/fibo/FND/Agreements/Contracts/Counterparty.md)
- **Subproperty of**: [hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)
- **Subproperty of**: [hasUndergoer](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer>)

## Annotations

- **label**: has counterparty
- **definition**: identifies a party to a contract, typically not the contract principal

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
