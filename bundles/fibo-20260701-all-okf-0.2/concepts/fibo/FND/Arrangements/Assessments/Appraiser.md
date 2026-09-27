---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: appraiser
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that evaluates or estimates the nature, quality, ability, or value of someone or something
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraisal
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/provides
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraiser
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: appraiser
type: Ontology Class
---

# appraiser

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraiser>

## Definition

party that evaluates or estimates the nature, quality, ability, or value of someone or something

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: min cardinality 0
- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: some values from of type [Appraisal](/concepts/fibo/FND/Arrangements/Assessments/Appraisal.md)

## Annotations

- **label**: appraiser
- **definition**: party that evaluates or estimates the nature, quality, ability, or value of someone or something

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
