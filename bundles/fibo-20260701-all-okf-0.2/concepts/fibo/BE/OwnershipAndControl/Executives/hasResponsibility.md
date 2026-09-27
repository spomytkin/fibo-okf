---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has responsibility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a commitment or obligation that an independent party has
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  range:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Duty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Duty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/hasCapacity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/hasCapacity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasResponsibility
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: has responsibility
type: Ontology Property
---

# has responsibility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasResponsibility>

## Definition

specifies a commitment or obligation that an independent party has

## Relationships

- **Domain**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Range**: [Duty](/concepts/fibo/FND/Law/LegalCapacity/Duty.md)
- **Subproperty of**: [hasCapacity](/concepts/fibo/FND/Law/LegalCapacity/hasCapacity.md)

## Annotations

- **label**: has responsibility
- **definition**: specifies a commitment or obligation that an independent party has

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
