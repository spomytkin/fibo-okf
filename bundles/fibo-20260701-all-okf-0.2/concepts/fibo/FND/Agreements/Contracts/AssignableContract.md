---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: assignable contract
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract in which contract holder (assignor) may transfer some or all of their rights and obligations to another
      party (assignee)
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Many, though not all, futures contracts are assignable. This means that the original contract holder can sell the
      contract to another party in return for cash, and that party then assumes the rights, responsibilities, and benefits
      of that contract from that point onwards.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that while the assignor may divest themselves of some rights, that assignment does not necessarily eliminate
      performance obligations of the assignor to the third party. Characteristics that are important to understand with respect
      to an assignment include the circumstances in which the assignor remains obligated and any remedies available if the
      assignor does not perform.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isAssignable
    value: 'true'
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/TransferableContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/TransferableContract
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/AssignableContract
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: assignable contract
type: Ontology Class
---

# assignable contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/AssignableContract>

## Definition

contract in which contract holder (assignor) may transfer some or all of their rights and obligations to another party (assignee)

## Relationships

- **Subclass of**: [TransferableContract](/concepts/fibo/FND/Agreements/Contracts/TransferableContract.md)

## Constraints

- **[isAssignable](/concepts/fibo/FND/Agreements/Contracts/isAssignable.md)**: has value value `true`

## Annotations

- **label**: assignable contract
- **definition**: contract in which contract holder (assignor) may transfer some or all of their rights and obligations to another party (assignee)
- **example**: Many, though not all, futures contracts are assignable. This means that the original contract holder can sell the contract to another party in return for cash, and that party then assumes the rights, responsibilities, and benefits of that contract from that point onwards.
- **explanatoryNote**: Note that while the assignor may divest themselves of some rights, that assignment does not necessarily eliminate performance obligations of the assignor to the third party. Characteristics that are important to understand with respect to an assignment include the circumstances in which the assignor remains obligated and any remedies available if the assignor does not perform.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
