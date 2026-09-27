---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exercise terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms specific to the conditions, conventions and other stipulations related to the exercise of an option
      or entitlement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/ExerciseConvention
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/uses
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/ExerciseTerms
sources:
- id: fibo-source-b0549059cf
  resource: references/fibo/SEC/Debt/ExerciseConventions.rdf
  sha256: b0549059cf085c65a45ceb8097c6a5d1580392da9215ca35ca9afe213b18f5e4
  title: FIBO source SEC/Debt/ExerciseConventions.rdf
title: exercise terms
type: Ontology Class
---

# exercise terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/ExerciseTerms>

## Definition

contract terms specific to the conditions, conventions and other stipulations related to the exercise of an option or entitlement

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Constraints

- **[uses](<https://www.omg.org/spec/Commons/ContextualDesignators/uses>)**: some values from of type [ExerciseConvention](/concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseConvention.md)

## Annotations

- **label** (en): exercise terms
- **definition** (en): contract terms specific to the conditions, conventions and other stipulations related to the exercise of an option or entitlement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
