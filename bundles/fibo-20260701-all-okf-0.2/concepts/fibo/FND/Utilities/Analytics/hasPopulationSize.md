---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has population size
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the number of elements in a given population
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Arrangements/Arrangements/hasCollectionSize.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Arrangements/hasCollectionSize
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasPopulationSize
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has population size
type: Ontology Property
---

# has population size

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasPopulationSize>

## Definition

indicates the number of elements in a given population

## Relationships

- **Range**: [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **Subproperty of**: [hasCollectionSize](/concepts/fibo/FND/Arrangements/Arrangements/hasCollectionSize.md)

## Annotations

- **label**: has population size
- **definition**: indicates the number of elements in a given population

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
