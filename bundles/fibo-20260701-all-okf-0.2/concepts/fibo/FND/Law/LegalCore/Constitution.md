---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: constitution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: set of basic principles by which an organization is governed, especially in relation to the rights of the people
      it governs
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A constitution is an aggregate of fundamental principles or established precedents that constitute the legal basis
      of a polity, organisation or other type of entity and commonly determine how that entity is to be governed.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/Law
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/Constitution
sources:
- id: fibo-source-31fe191c06
  resource: references/fibo/FND/Law/LegalCore.rdf
  sha256: 31fe191c06f11a104ba752303784bfd17673c9e515a6e3d3ed538b19a5da37e9
  title: FIBO source FND/Law/LegalCore.rdf
title: constitution
type: Ontology Class
---

# constitution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/Constitution>

## Definition

set of basic principles by which an organization is governed, especially in relation to the rights of the people it governs

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Constraints

- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [Law](/concepts/fibo/FND/Law/LegalCore/Law.md)

## Annotations

- **label**: constitution
- **definition**: set of basic principles by which an organization is governed, especially in relation to the rights of the people it governs
- **explanatoryNote**: A constitution is an aggregate of fundamental principles or established precedents that constitute the legal basis of a polity, organisation or other type of entity and commonly determine how that entity is to be governed.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
