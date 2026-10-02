---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: de facto control
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: control that exists informally and is accepted, although not formally recognized
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For example, de facto acquisition or change of control means the acquisition, directly or indirectly, by any person
      or group of persons acting jointly or in concert, of beneficial ownership of, or control or direction over, sufficient
      voting shares of some legal entity to permit such person or persons to exercise, or to control or direct the voting
      of, 50 percent or more of the total number of votes in that entity.
  disjoint_with:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/DeJureControl.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeJureControl
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/Control.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeFactoControl
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: de facto control
type: Ontology Class
---

# de facto control

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeFactoControl>

## Definition

control that exists informally and is accepted, although not formally recognized

## Relationships

- **Subclass of**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control/Control.md)

## Constraints

- **Disjoint with**: [DeJureControl](/concepts/fibo/FND/OwnershipAndControl/Control/DeJureControl.md)

## Annotations

- **label**: de facto control
- **definition**: control that exists informally and is accepted, although not formally recognized
- **explanatoryNote**: For example, de facto acquisition or change of control means the acquisition, directly or indirectly, by any person or group of persons acting jointly or in concert, of beneficial ownership of, or control or direction over, sufficient voting shares of some legal entity to permit such person or persons to exercise, or to control or direct the voting of, 50 percent or more of the total number of votes in that entity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
