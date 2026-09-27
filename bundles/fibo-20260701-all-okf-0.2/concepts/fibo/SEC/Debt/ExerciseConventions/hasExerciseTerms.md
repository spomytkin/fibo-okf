---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has exercise terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a derivative, such as an option or entitlement, to any exercise terms that are specified therein
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
  range:
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/ExerciseTerms
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/hasExerciseTerms
sources:
- id: fibo-source-b0549059cf
  resource: references/fibo/SEC/Debt/ExerciseConventions.rdf
  sha256: b0549059cf085c65a45ceb8097c6a5d1580392da9215ca35ca9afe213b18f5e4
  title: FIBO source SEC/Debt/ExerciseConventions.rdf
title: has exercise terms
type: Ontology Property
---

# has exercise terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/hasExerciseTerms>

## Definition

links a derivative, such as an option or entitlement, to any exercise terms that are specified therein

## Relationships

- **Domain**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)
- **Range**: [ExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseTerms.md)
- **Subproperty of**: [hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)

## Annotations

- **label** (en): has exercise terms
- **definition** (en): links a derivative, such as an option or entitlement, to any exercise terms that are specified therein

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
