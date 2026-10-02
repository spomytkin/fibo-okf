---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is an instrument of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an instrumentality of some government to the government that it supports
  domain:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Instrumentality.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Instrumentality
  range:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Government.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Government
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/isInstrumentOf
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: is an instrument of
type: Ontology Property
---

# is an instrument of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/isInstrumentOf>

## Definition

relates an instrumentality of some government to the government that it supports

## Relationships

- **Domain**: [Instrumentality](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Instrumentality.md)
- **Range**: [Government](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Government.md)

## Annotations

- **label**: is an instrument of
- **definition**: relates an instrumentality of some government to the government that it supports

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
