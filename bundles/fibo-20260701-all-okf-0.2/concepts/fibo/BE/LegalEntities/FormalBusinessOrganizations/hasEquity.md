---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has equity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates owners' equity associated with the entity
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
  range:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/OwnersEquity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/OwnersEquity
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasEquity
sources:
- id: fibo-source-9758af6c79
  resource: references/fibo/BE/LegalEntities/FormalBusinessOrganizations.rdf
  sha256: 9758af6c796f157eedb21d72cde0822cb7a2ecbd6b5a70ef23be48121c598ede
  title: FIBO source BE/LegalEntities/FormalBusinessOrganizations.rdf
title: has equity
type: Ontology Property
---

# has equity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasEquity>

## Definition

indicates owners' equity associated with the entity

## Relationships

- **Domain**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)
- **Range**: [OwnersEquity](/concepts/fibo/FND/OwnershipAndControl/Ownership/OwnersEquity.md)
- **Subproperty of**: [hasExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression>)

## Annotations

- **label**: has equity
- **definition**: indicates owners' equity associated with the entity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
