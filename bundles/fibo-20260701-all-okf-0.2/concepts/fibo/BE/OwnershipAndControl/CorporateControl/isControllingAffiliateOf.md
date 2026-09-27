---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is controlling affiliate of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: controls directly, or indirectly through one or more intermediaries
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate
  inverse_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/hasControllingAffiliate.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasControllingAffiliate
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/isAffiliateOf.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isAffiliateOf
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isControllingAffiliateOf
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: is controlling affiliate of
type: Ontology Property
---

# is controlling affiliate of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isControllingAffiliateOf>

## Definition

controls directly, or indirectly through one or more intermediaries

## Relationships

- **Domain**: [ControllingAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md)
- **Inverse of**: [hasControllingAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/hasControllingAffiliate.md)
- **Range**: [ControlledAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate.md)
- **Subproperty of**: [isAffiliateOf](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/isAffiliateOf.md)
- **Subproperty of**: [actsOn](<https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn>)

## Annotations

- **label**: is controlling affiliate of
- **definition**: controls directly, or indirectly through one or more intermediaries

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
