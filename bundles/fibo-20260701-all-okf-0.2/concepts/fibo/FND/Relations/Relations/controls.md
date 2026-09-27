---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: controls
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exercises authority or influence over
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/playsActiveRoleThatDirectlyAffects
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/controls
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
- id: fibo-source-5bd2fc8cf9
  resource: references/fibo/FND/Relations/Relations.rdf
  sha256: 5bd2fc8cf9713fc293309a78a9ec760e0eacc6a4c5e9499bbbb29b4f8a172fa2
  title: FIBO source FND/Relations/Relations.rdf
title: controls
type: Ontology Property
---

# controls

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/controls>

## Definition

exercises authority or influence over

## Relationships

- **Domain**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Subproperty of**: [playsActiveRoleThatDirectlyAffects](<https://www.omg.org/spec/Commons/PartiesAndSituations/playsActiveRoleThatDirectlyAffects>)

## Annotations

- **label**: controls
- **definition**: exercises authority or influence over

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
