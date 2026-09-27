---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has capacity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies an individual or organization that has some ability and availability to carry out certain actions, or
      has certain rights or obligations
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  inverse_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/isCapacityOf.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isCapacityOf
  range:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalCapacity
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/hasCapacity
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: has capacity
type: Ontology Property
---

# has capacity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/hasCapacity>

## Definition

identifies an individual or organization that has some ability and availability to carry out certain actions, or has certain rights or obligations

## Relationships

- **Domain**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Inverse of**: [isCapacityOf](/concepts/fibo/FND/Law/LegalCapacity/isCapacityOf.md)
- **Range**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md)

## Annotations

- **label**: has capacity
- **definition**: identifies an individual or organization that has some ability and availability to carry out certain actions, or has certain rights or obligations

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
