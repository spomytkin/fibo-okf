---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: majority controlling party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: controlling party that possesses, either directly or indirectly, the power to direct or cause the direction of
      the management and policies of a legal person, whether through the ownership of a majority of voting securities, by
      contract, or otherwise
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Electronic Code of Federal Regulations, Title 17, Chapter 1, Section 49.2
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/EntityControllingParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/MajorityControllingParty
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: majority controlling party
type: Ontology Class
---

# majority controlling party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/MajorityControllingParty>

## Definition

controlling party that possesses, either directly or indirectly, the power to direct or cause the direction of the management and policies of a legal person, whether through the ownership of a majority of voting securities, by contract, or otherwise

## Relationships

- **Subclass of**: [EntityControllingParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md)

## Annotations

- **label**: majority controlling party
- **definition**: controlling party that possesses, either directly or indirectly, the power to direct or cause the direction of the management and policies of a legal person, whether through the ownership of a majority of voting securities, by contract, or otherwise
- **adaptedFrom**: Electronic Code of Federal Regulations, Title 17, Chapter 1, Section 49.2

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
