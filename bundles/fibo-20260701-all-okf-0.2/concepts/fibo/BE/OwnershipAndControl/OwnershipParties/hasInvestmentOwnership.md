---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has investment ownership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a legal person to the context in which it owns a formal organization
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/Organizations/LegalPerson
  inverse_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/hasOwningEntity.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwningEntity
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwnership
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/playsActiveRoleIn
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasInvestmentOwnership
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: has investment ownership
type: Ontology Property
---

# has investment ownership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasInvestmentOwnership>

## Definition

relates a legal person to the context in which it owns a formal organization

## Relationships

- **Domain**: [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)
- **Inverse of**: [hasOwningEntity](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/hasOwningEntity.md)
- **Range**: [EntityOwnership](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md)
- **Subproperty of**: [playsActiveRoleIn](<https://www.omg.org/spec/Commons/PartiesAndSituations/playsActiveRoleIn>)

## Annotations

- **label**: has investment ownership
- **definition**: relates a legal person to the context in which it owns a formal organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
