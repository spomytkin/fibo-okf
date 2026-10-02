---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has affiliate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: has a party which directly, or indirectly through one or more intermediaries, controls, or is controlled by, or
      is under common control with the company
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/Affiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Affiliate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/isControlledPartyOf.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControlledPartyOf
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasAffiliate
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: has affiliate
type: Ontology Property
---

# has affiliate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasAffiliate>

## Definition

has a party which directly, or indirectly through one or more intermediaries, controls, or is controlled by, or is under common control with the company

## Relationships

- **Domain**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)
- **Range**: [Affiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/Affiliate.md)
- **Subproperty of**: [isControlledPartyOf](/concepts/fibo/FND/OwnershipAndControl/Control/isControlledPartyOf.md)

## Annotations

- **label**: has affiliate
- **definition**: has a party which directly, or indirectly through one or more intermediaries, controls, or is controlled by, or is under common control with the company

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
