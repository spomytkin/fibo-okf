---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: owns and controls
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: directs and exercises authoritative or dominating influence over some thing that is also owned
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'basic rule: if x controls y and x owns y then x owns and controls y

      SWRL rule: controls(?x, ?y), owns(?x, ?y) -> ownsAndControls(?x, ?y)'
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  inverse_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/OwnershipAndControl/isOwnedAndControlledBy.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/isOwnedAndControlledBy
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/owns.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/owns
  - concept: /concepts/fibo/FND/Relations/Relations/controls.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/controls
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/ownsAndControls
sources:
- id: fibo-source-e6e2018aa7
  resource: references/fibo/FND/OwnershipAndControl/OwnershipAndControl.rdf
  sha256: e6e2018aa7f8cb7c2fab2505906a5311b9e6a797e599133ddfb4fac1365a432f
  title: FIBO source FND/OwnershipAndControl/OwnershipAndControl.rdf
title: owns and controls
type: Ontology Property
---

# owns and controls

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/ownsAndControls>

## Definition

directs and exercises authoritative or dominating influence over some thing that is also owned

## Relationships

- **Domain**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Inverse of**: [isOwnedAndControlledBy](/concepts/fibo/FND/OwnershipAndControl/OwnershipAndControl/isOwnedAndControlledBy.md)
- **Subproperty of**: [owns](/concepts/fibo/FND/OwnershipAndControl/Ownership/owns.md)
- **Subproperty of**: [controls](/concepts/fibo/FND/Relations/Relations/controls.md)

## Annotations

- **label**: owns and controls
- **definition**: directs and exercises authoritative or dominating influence over some thing that is also owned
- **editorialNote**: basic rule: if x controls y and x owns y then x owns and controls y SWRL rule: controls(?x, ?y), owns(?x, ?y) -> ownsAndControls(?x, ?y)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
