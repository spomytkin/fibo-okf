---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has contract duration
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the period of time during which a contract is intended to be in force once it has been executed
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the duration may be relative or explicit, depending on the nature of the contract, and may be extended
      if the provisions of the contract permit extension.
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasTerm.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasTerm
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractDuration
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has contract duration
type: Ontology Property
---

# has contract duration

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractDuration>

## Definition

indicates the period of time during which a contract is intended to be in force once it has been executed

## Relationships

- **Domain**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **Range**: [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)
- **Subproperty of**: [hasTerm](/concepts/fibo/FND/Agreements/Contracts/hasTerm.md)

## Annotations

- **label** (en): has contract duration
- **definition**: indicates the period of time during which a contract is intended to be in force once it has been executed
- **explanatoryNote**: Note that the duration may be relative or explicit, depending on the nature of the contract, and may be extended if the provisions of the contract permit extension.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
