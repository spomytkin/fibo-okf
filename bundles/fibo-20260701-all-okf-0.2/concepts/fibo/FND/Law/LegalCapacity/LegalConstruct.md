---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal construct
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: something which is conferred by way of law or contract, such as a right
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Obligations are an aspect of this category of thing, as are rights.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isConferredOn
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalConstruct
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: legal construct
type: Ontology Class
---

# legal construct

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalConstruct>

## Definition

something which is conferred by way of law or contract, such as a right

## Constraints

- **[isConferredOn](/concepts/fibo/FND/Law/LegalCapacity/isConferredOn.md)**: min qualified cardinality 0 of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: min qualified cardinality 0

## Annotations

- **label**: legal construct
- **definition**: something which is conferred by way of law or contract, such as a right
- **editorialNote**: Obligations are an aspect of this category of thing, as are rights.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
