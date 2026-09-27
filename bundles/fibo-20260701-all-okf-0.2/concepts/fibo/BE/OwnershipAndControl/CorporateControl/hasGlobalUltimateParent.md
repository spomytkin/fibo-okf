---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has global ultimate parent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an organization to another recognized as its ultimate parent, if it has one
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: In the case of companies that are subsidiaries of another company that itself has a parent, this identifies the
      organization at the top of the hierarchy, world-wide. Adapted from consensus definition of Ultimate Parent, now that
      this is split into national and global parent.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: consensus definition of ultimate parent, with the split between domestic and global parent
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/GlobalUltimateParent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/GlobalUltimateParent
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/hasMajorityControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/hasMajorityControllingParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasGlobalUltimateParent
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: has global ultimate parent
type: Ontology Property
---

# has global ultimate parent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasGlobalUltimateParent>

## Definition

relates an organization to another recognized as its ultimate parent, if it has one

## Relationships

- **Range**: [GlobalUltimateParent](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/GlobalUltimateParent.md)
- **Subproperty of**: [hasMajorityControllingParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/hasMajorityControllingParty.md)

## Annotations

- **label**: has global ultimate parent
- **definition**: relates an organization to another recognized as its ultimate parent, if it has one
- **editorialNote**: In the case of companies that are subsidiaries of another company that itself has a parent, this identifies the organization at the top of the hierarchy, world-wide. Adapted from consensus definition of Ultimate Parent, now that this is split into national and global parent.
- **adaptedFrom**: consensus definition of ultimate parent, with the split between domestic and global parent

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
