---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: master agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract between named parties that outlines the terms and conditions designed to apply to a number of accounts,
      transactions, or other activities between the parties, and that consolidates and provides overarching terms for separate
      but related agreements
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: A master services agreement governs the terms between a service provider and client. Typically, clients will use
      Statements of Work that point back to the master agreement so they don't have to recreate a new contract with new terms
      each time there is a new project, or to cover common terms across services, warranties, and deliveries.
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Some credit facilities and many brokerage arrangements are master agreements.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A master agreement can be used to set out standard terms and conditions so that any new agreements don't need to
      cover the same information again.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: master contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MasterAgreement
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: master agreement
type: Ontology Class
---

# master agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MasterAgreement>

## Definition

contract between named parties that outlines the terms and conditions designed to apply to a number of accounts, transactions, or other activities between the parties, and that consolidates and provides overarching terms for separate but related agreements

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: min qualified cardinality 0 of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)

## Annotations

- **label**: master agreement
- **definition**: contract between named parties that outlines the terms and conditions designed to apply to a number of accounts, transactions, or other activities between the parties, and that consolidates and provides overarching terms for separate but related agreements
- **example**: A master services agreement governs the terms between a service provider and client. Typically, clients will use Statements of Work that point back to the master agreement so they don't have to recreate a new contract with new terms each time there is a new project, or to cover common terms across services, warranties, and deliveries.
- **example**: Some credit facilities and many brokerage arrangements are master agreements.
- **explanatoryNote**: A master agreement can be used to set out standard terms and conditions so that any new agreements don't need to cover the same information again.
- **synonym**: master contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
