---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is controlled by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: is influenced, managed, or directed by
  inverse_of:
  - concept: /concepts/fibo/FND/Relations/Relations/controls.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/controls
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/experiencesDirectly
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isControlledBy
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
- id: fibo-source-5bd2fc8cf9
  resource: references/fibo/FND/Relations/Relations.rdf
  sha256: 5bd2fc8cf9713fc293309a78a9ec760e0eacc6a4c5e9499bbbb29b4f8a172fa2
  title: FIBO source FND/Relations/Relations.rdf
title: is controlled by
type: Ontology Property
---

# is controlled by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isControlledBy>

## Definition

is influenced, managed, or directed by

## Relationships

- **Inverse of**: [controls](/concepts/fibo/FND/Relations/Relations/controls.md)
- **Range**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Subproperty of**: [experiencesDirectly](<https://www.omg.org/spec/Commons/PartiesAndSituations/experiencesDirectly>)

## Annotations

- **label**: is controlled by
- **definition**: is influenced, managed, or directed by

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
