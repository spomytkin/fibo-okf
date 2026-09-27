---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: indexing scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system for indexing values, data, information, or knowledge
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/Index
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Arrangements/Scheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Arrangements/Scheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/IndexingScheme
sources:
- id: fibo-source-2943e244c9
  resource: references/fibo/FND/Arrangements/IdentifiersAndIndices.rdf
  sha256: 2943e244c9f1e05582f4cd0ce73c69f5f8a148d740aa66d458c621a1ad24f51c
  title: FIBO source FND/Arrangements/IdentifiersAndIndices.rdf
title: indexing scheme
type: Ontology Class
---

# indexing scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/IndexingScheme>

## Definition

system for indexing values, data, information, or knowledge

## Relationships

- **Subclass of**: [Scheme](/concepts/fibo/FND/Arrangements/Arrangements/Scheme.md)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [Index](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices/Index.md)

## Annotations

- **label**: indexing scheme
- **definition**: system for indexing values, data, information, or knowledge

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
