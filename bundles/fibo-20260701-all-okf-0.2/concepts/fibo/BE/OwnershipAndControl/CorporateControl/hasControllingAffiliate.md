---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has controlling affiliate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: is directly, or indirectly through one or more intermediaries, controlled by
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/isAffiliateOf.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isAffiliateOf
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasControllingAffiliate
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: has controlling affiliate
type: Ontology Property
---

# has controlling affiliate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasControllingAffiliate>

## Definition

is directly, or indirectly through one or more intermediaries, controlled by

## Relationships

- **Domain**: [ControlledAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate.md)
- **Range**: [ControllingAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md)
- **Subproperty of**: [isAffiliateOf](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/isAffiliateOf.md)
- **Subproperty of**: [isAffectedBy](<https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy>)

## Annotations

- **label**: has controlling affiliate
- **definition**: is directly, or indirectly through one or more intermediaries, controlled by

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
