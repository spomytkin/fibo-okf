---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: policy
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system of principles, rules and guidelines, adopted by an organization to guide decision making with respect to
      particular situations and implemented via procedures or protocols to achieve stated goals
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/implements
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Strategy
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Policy
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: policy
type: Ontology Class
---

# policy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Policy>

## Definition

system of principles, rules and guidelines, adopted by an organization to guide decision making with respect to particular situations and implemented via procedures or protocols to achieve stated goals

## Constraints

- **[implements](/concepts/fibo/FND/Law/LegalCapacity/implements.md)**: min qualified cardinality 0
- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [Strategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Strategy.md)

## Annotations

- **label**: policy
- **definition**: system of principles, rules and guidelines, adopted by an organization to guide decision making with respect to particular situations and implemented via procedures or protocols to achieve stated goals

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
