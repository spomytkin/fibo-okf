---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has principal party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the main or principal party to a contract
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
  range:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractPrincipal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractPrincipal
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasPrincipalParty
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has principal party
type: Ontology Property
---

# has principal party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasPrincipalParty>

## Definition

identifies the main or principal party to a contract

## Relationships

- **Domain**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **Range**: [ContractPrincipal](/concepts/fibo/FND/Agreements/Contracts/ContractPrincipal.md)
- **Subproperty of**: [hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)
- **Subproperty of**: [hasActor](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor>)

## Annotations

- **label**: has principal party
- **definition**: identifies the main or principal party to a contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
