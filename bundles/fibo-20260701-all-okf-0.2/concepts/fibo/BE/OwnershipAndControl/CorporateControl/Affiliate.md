---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: affiliate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that is related to a legal entity, directly, or indirectly through one or more intermediaries, and controls,
      or is controlled by, or is under common control with that entity, typically determined by the degree of ownership
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Affiliate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isAffiliateOf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Affiliate
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: affiliate
type: Ontology Class
---

# affiliate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Affiliate>

## Definition

party that is related to a legal entity, directly, or indirectly through one or more intermediaries, and controls, or is controlled by, or is under common control with that entity, typically determined by the degree of ownership

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[isAffiliateOf](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/isAffiliateOf.md)**: some values from of type [Affiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/Affiliate.md)

## Annotations

- **label**: affiliate
- **definition**: party that is related to a legal entity, directly, or indirectly through one or more intermediaries, and controls, or is controlled by, or is under common control with that entity, typically determined by the degree of ownership

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
