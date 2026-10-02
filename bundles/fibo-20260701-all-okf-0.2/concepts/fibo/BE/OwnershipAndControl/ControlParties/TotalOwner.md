---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: total owner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that has 100 percent ownership some legal entity
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: By virtue of holding 100 percent of the equity ownership, the Total Owner also holds 100 percent of the controlling
      equity, if there is a difference. Therefore it is both a total owner and a total controlling party.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/TotalOwner
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: total owner
type: Ontology Class
---

# total owner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/TotalOwner>

## Definition

party that has 100 percent ownership some legal entity

## Relationships

- **Subclass of**: [ConstitutionalOwner](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner.md)

## Annotations

- **label**: total owner
- **definition**: party that has 100 percent ownership some legal entity
- **editorialNote**: By virtue of holding 100 percent of the equity ownership, the Total Owner also holds 100 percent of the controlling equity, if there is a difference. Therefore it is both a total owner and a total controlling party.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
