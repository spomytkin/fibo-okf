---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is owned and controlled by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something to the party that owns, influences, manages and directs it
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/isOwnedBy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isOwnedBy
  - concept: /concepts/fibo/FND/Relations/Relations/isControlledBy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isControlledBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/isOwnedAndControlledBy
sources:
- id: fibo-source-e6e2018aa7
  resource: references/fibo/FND/OwnershipAndControl/OwnershipAndControl.rdf
  sha256: e6e2018aa7f8cb7c2fab2505906a5311b9e6a797e599133ddfb4fac1365a432f
  title: FIBO source FND/OwnershipAndControl/OwnershipAndControl.rdf
title: is owned and controlled by
type: Ontology Property
---

# is owned and controlled by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/isOwnedAndControlledBy>

## Definition

relates something to the party that owns, influences, manages and directs it

## Relationships

- **Range**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Subproperty of**: [isOwnedBy](/concepts/fibo/FND/OwnershipAndControl/Ownership/isOwnedBy.md)
- **Subproperty of**: [isControlledBy](/concepts/fibo/FND/Relations/Relations/isControlledBy.md)

## Annotations

- **label**: is owned and controlled by
- **definition**: relates something to the party that owns, influences, manages and directs it

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
