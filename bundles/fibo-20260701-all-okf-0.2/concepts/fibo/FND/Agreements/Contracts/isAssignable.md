---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is assignable
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the contract and the rights thereunder may be assigned by one of the signatories to some other
      party
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: This is believed to be the basis on which transferable contracts such as financial securities and software licences
      may be bought and sold on some market, and also the basis on which a bilateral contract such as an over the counter
      derivative may be novated so that a new party becomes one of the parties. There are subtle distinctions between these
      three concepts which are not yet represented here.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An assignment (Latin cessio) is a term used with similar meanings in the law of contracts and in the law of real
      estate. In both instances, it encompasses the transfer of rights held by one party, the assignor, to another party,
      the assignee. The details of the assignment determines some additional rights and liabilities (or duties). Typically
      a third-party is involved in a contract with the assignor, and the contract is in effect transferred to the assignee.
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isAssignable
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: is assignable
type: Ontology Property
---

# is assignable

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isAssignable>

## Definition

indicates whether the contract and the rights thereunder may be assigned by one of the signatories to some other party

## Relationships

- **Domain**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is assignable
- **definition**: indicates whether the contract and the rights thereunder may be assigned by one of the signatories to some other party
- **editorialNote**: This is believed to be the basis on which transferable contracts such as financial securities and software licences may be bought and sold on some market, and also the basis on which a bilateral contract such as an over the counter derivative may be novated so that a new party becomes one of the parties. There are subtle distinctions between these three concepts which are not yet represented here.
- **explanatoryNote**: An assignment (Latin cessio) is a term used with similar meanings in the law of contracts and in the law of real estate. In both instances, it encompasses the transfer of rights held by one party, the assignor, to another party, the assignee. The details of the assignment determines some additional rights and liabilities (or duties). Typically a third-party is involved in a contract with the assignor, and the contract is in effect transferred to the assignee.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
