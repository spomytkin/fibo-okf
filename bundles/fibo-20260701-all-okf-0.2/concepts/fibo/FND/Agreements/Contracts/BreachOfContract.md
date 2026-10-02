---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: breach of contract
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier of events representing a violation of an express, or implied, condition of a contract to do or not to
      do something, without a legitimate excuse
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Examples of events that are considered a breach of contract include discovery of misrepresentation, not completing
      a job, not paying in full or on time, failing to deliver all the goods, substituting inferior or significantly different
      goods, not providing a bond when required, being late without excuse, or any act that demonstrates that a party will
      not complete required work ('anticipatory breach.') Breach of contract is one of the most common causes of law suits
      for damages and/or court-ordered 'specific performance' of the contract. A breach of contract frequently invalidates
      the contract.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/BreachOfContract
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: breach of contract
type: Ontology Class
---

# breach of contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/BreachOfContract>

## Definition

classifier of events representing a violation of an express, or implied, condition of a contract to do or not to do something, without a legitimate excuse

## Relationships

- **Subclass of**: [ContractLifecycleEvent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent.md)
- **Subclass of**: [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Annotations

- **label** (en): breach of contract
- **definition** (en): classifier of events representing a violation of an express, or implied, condition of a contract to do or not to do something, without a legitimate excuse
- **explanatoryNote** (en): Examples of events that are considered a breach of contract include discovery of misrepresentation, not completing a job, not paying in full or on time, failing to deliver all the goods, substituting inferior or significantly different goods, not providing a bond when required, being late without excuse, or any act that demonstrates that a party will not complete required work ('anticipatory breach.') Breach of contract is one of the most common causes of law suits for damages and/or court-ordered 'specific performance' of the contract. A breach of contract frequently invalidates the contract.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
