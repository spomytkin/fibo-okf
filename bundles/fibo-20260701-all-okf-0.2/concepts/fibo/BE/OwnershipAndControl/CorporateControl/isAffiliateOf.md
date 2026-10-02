---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is affiliate of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a party which directly, or indirectly through one or more intermediaries, controls, or is controlled by,
      or is under common control by another party to that party
  characteristics:
  - symmetric
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/Affiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Affiliate
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/Affiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Affiliate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  - http://www.w3.org/2002/07/owl#SymmetricProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isAffiliateOf
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: is affiliate of
type: Ontology Property
---

# is affiliate of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isAffiliateOf>

## Definition

relates a party which directly, or indirectly through one or more intermediaries, controls, or is controlled by, or is under common control by another party to that party

## Relationships

- **Domain**: [Affiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/Affiliate.md)
- **Range**: [Affiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/Affiliate.md)

## Annotations

- **label**: is affiliate of
- **definition**: relates a party which directly, or indirectly through one or more intermediaries, controls, or is controlled by, or is under common control by another party to that party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
