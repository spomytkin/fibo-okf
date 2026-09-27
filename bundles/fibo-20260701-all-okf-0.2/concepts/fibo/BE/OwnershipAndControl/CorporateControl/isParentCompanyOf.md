---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is parent company of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a controlled affiliate that it owns at least 50 percent of
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate
  inverse_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/isSubsidiaryOf.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isSubsidiaryOf
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/Subsidiary.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Subsidiary
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/isControllingAffiliateOf.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isControllingAffiliateOf
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isParentCompanyOf
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: is parent company of
type: Ontology Property
---

# is parent company of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isParentCompanyOf>

## Definition

indicates a controlled affiliate that it owns at least 50 percent of

## Relationships

- **Domain**: [ControllingAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md)
- **Inverse of**: [isSubsidiaryOf](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/isSubsidiaryOf.md)
- **Range**: [Subsidiary](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/Subsidiary.md)
- **Subproperty of**: [isControllingAffiliateOf](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/isControllingAffiliateOf.md)

## Annotations

- **label**: is parent company of
- **definition**: indicates a controlled affiliate that it owns at least 50 percent of

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
