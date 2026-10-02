---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contingent obligation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: obligation that depends on a future event or the performance of an action
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/isObligationOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentRight
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isImpliedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Duty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Duty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentObligation
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: contingent obligation
type: Ontology Class
---

# contingent obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentObligation>

## Definition

obligation that depends on a future event or the performance of an action

## Relationships

- **Subclass of**: [Duty](/concepts/fibo/FND/Law/LegalCapacity/Duty.md)

## Constraints

- **[isObligationOf](/concepts/fibo/FND/Agreements/Agreements/isObligationOf.md)**: some values from of type [Obligor](/concepts/fibo/FND/Agreements/Agreements/Obligor.md)
- **[isImpliedBy](/concepts/fibo/FND/Law/LegalCapacity/isImpliedBy.md)**: some values from of type [ContingentRight](/concepts/fibo/FND/Law/LegalCapacity/ContingentRight.md)

## Annotations

- **label** (en): contingent obligation
- **definition**: obligation that depends on a future event or the performance of an action

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
