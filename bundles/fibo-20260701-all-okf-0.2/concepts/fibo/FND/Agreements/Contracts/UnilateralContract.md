---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unilateral contract
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract in which one party makes an offer that can only be accepted through performance rather than a return promise
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In a unilateral, or one-sided, contract, one party, known as the offeror, makes a promise in exchange for an act
      (or abstention from acting) by another party, known as the offeree. If the offeree acts on the offeror's promise, the
      offeror is legally obligated to fulfill the contract, but an offeree cannot be forced to act (or not act), because no
      return promise has been made to the offeror. After an offeree has performed, only one enforceable promise exists, that
      of the offeror.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/UnilateralCommitment
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/confers
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/UnilateralContract
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: unilateral contract
type: Ontology Class
---

# unilateral contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/UnilateralContract>

## Definition

contract in which one party makes an offer that can only be accepted through performance rather than a return promise

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[confers](/concepts/fibo/FND/Relations/Relations/confers.md)**: all values from of type [UnilateralCommitment](/concepts/fibo/FND/Agreements/Agreements/UnilateralCommitment.md)

## Annotations

- **label**: unilateral contract
- **definition**: contract in which one party makes an offer that can only be accepted through performance rather than a return promise
- **explanatoryNote**: In a unilateral, or one-sided, contract, one party, known as the offeror, makes a promise in exchange for an act (or abstention from acting) by another party, known as the offeree. If the offeree acts on the offeror's promise, the offeror is legally obligated to fulfill the contract, but an offeree cannot be forced to act (or not act), because no return promise has been made to the offeror. After an offeree has performed, only one enforceable promise exists, that of the offeror.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
