---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is stage of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a stage in a product or trade lifecycle or process to the lifecycle or process that it is a stage of
  inverse_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/isPartOf
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isStageOf
sources:
- id: fibo-source-92efc72f29
  resource: references/fibo/FND/Arrangements/Lifecycles.rdf
  sha256: 92efc72f29aba7c64208722174530078a5a46ad575d7ceabbf0cd9a444ad5e0e
  title: FIBO source FND/Arrangements/Lifecycles.rdf
title: is stage of
type: Ontology Property
---

# is stage of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isStageOf>

## Definition

relates a stage in a product or trade lifecycle or process to the lifecycle or process that it is a stage of

## Relationships

- **Inverse of**: [hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)
- **Subproperty of**: [isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)

## Annotations

- **label**: is stage of
- **definition**: relates a stage in a product or trade lifecycle or process to the lifecycle or process that it is a stage of

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
