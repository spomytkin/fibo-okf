---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is wholly owned by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a legal entity to a party that has 100 percent ownership and control over it
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/TotalControllingInterestParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/TotalControllingInterestParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isWhollyOwnedBy
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: is wholly owned by
type: Ontology Property
---

# is wholly owned by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isWhollyOwnedBy>

## Definition

relates a legal entity to a party that has 100 percent ownership and control over it

## Relationships

- **Domain**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)
- **Range**: [TotalControllingInterestParty](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/TotalControllingInterestParty.md)

## Annotations

- **label**: is wholly owned by
- **definition**: relates a legal entity to a party that has 100 percent ownership and control over it

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
