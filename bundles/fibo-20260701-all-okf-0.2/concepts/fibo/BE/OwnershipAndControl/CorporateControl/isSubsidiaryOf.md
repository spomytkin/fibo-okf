---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is subsidiary of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: is controlled directly, or indirectly through one or more intermediaries and owned at least 50 percent by
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/Subsidiary.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Subsidiary
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/hasControllingAffiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasControllingAffiliate
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isSubsidiaryOf
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: is subsidiary of
type: Ontology Property
---

# is subsidiary of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isSubsidiaryOf>

## Definition

is controlled directly, or indirectly through one or more intermediaries and owned at least 50 percent by

## Relationships

- **Domain**: [Subsidiary](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/Subsidiary.md)
- **Range**: [ControllingAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md)
- **Subproperty of**: [hasControllingAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/hasControllingAffiliate.md)

## Annotations

- **label**: is subsidiary of
- **definition**: is controlled directly, or indirectly through one or more intermediaries and owned at least 50 percent by

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
