---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract principal
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that originates a contract and is identified as the first party to that contract, in the event that the contract
      distinguishes any party as such
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The principal to a contract is typically the originator and, in the case of a security, the issuer. In law, the
      principal is the party that has the primary responsibility in a liability or obligation, as opposed to an endorser,
      guarantor, or surety.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractPrincipal
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: contract principal
type: Ontology Class
---

# contract principal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractPrincipal>

## Definition

party that originates a contract and is identified as the first party to that contract, in the event that the contract distinguishes any party as such

## Relationships

- **Subclass of**: [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)

## Annotations

- **label**: contract principal
- **definition**: party that originates a contract and is identified as the first party to that contract, in the event that the contract distinguishes any party as such
- **explanatoryNote**: The principal to a contract is typically the originator and, in the case of a security, the issuer. In law, the principal is the party that has the primary responsibility in a liability or obligation, as opposed to an endorser, guarantor, or surety.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
