---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contingent right
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: right that depends on a future event or the performance of an action
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Contingent means that the interest, claim, or right is conditional, realized only when and if something occurs.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentObligation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/implies
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isConferredOn
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Right.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Right
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentRight
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: contingent right
type: Ontology Class
---

# contingent right

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentRight>

## Definition

right that depends on a future event or the performance of an action

## Relationships

- **Subclass of**: [Right](/concepts/fibo/FND/Law/LegalCapacity/Right.md)

## Constraints

- **[implies](/concepts/fibo/FND/Law/LegalCapacity/implies.md)**: some values from of type [ContingentObligation](/concepts/fibo/FND/Law/LegalCapacity/ContingentObligation.md)
- **[isConferredOn](/concepts/fibo/FND/Law/LegalCapacity/isConferredOn.md)**: some values from of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)

## Annotations

- **label** (en): contingent right
- **definition**: right that depends on a future event or the performance of an action
- **explanatoryNote**: Contingent means that the interest, claim, or right is conditional, realized only when and if something occurs.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
