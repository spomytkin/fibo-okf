---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structure or means of organizing information such as a blueprint, schema, numbering system, organization structure,
      measurement system, plan, taxonomy, or language for organizing information
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_cardinality
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Arrangement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Arrangements/Scheme
sources:
- id: fibo-source-40d4a97d42
  resource: references/fibo/FND/Arrangements/Arrangements.rdf
  sha256: 40d4a97d42efcf7a35be65975208192604f5ce601e40c41ef201dc2032c9eb79
  title: FIBO source FND/Arrangements/Arrangements.rdf
title: scheme
type: Ontology Class
---

# scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Arrangements/Scheme>

## Definition

structure or means of organizing information such as a blueprint, schema, numbering system, organization structure, measurement system, plan, taxonomy, or language for organizing information

## Relationships

- **Subclass of**: [Arrangement](<https://www.omg.org/spec/Commons/Collections/Arrangement>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: min cardinality 0

## Annotations

- **label**: scheme
- **definition**: structure or means of organizing information such as a blueprint, schema, numbering system, organization structure, measurement system, plan, taxonomy, or language for organizing information

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
