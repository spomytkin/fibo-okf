---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has vested in it
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the delegated legal authority that is vested in the controlling party
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority
  range:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/DelegatedLegalAuthority.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/DelegatedLegalAuthority
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/hasCapacity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/hasCapacity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasVestedInIt
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: has vested in it
type: Ontology Property
---

# has vested in it

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasVestedInIt>

## Definition

indicates the delegated legal authority that is vested in the controlling party

## Relationships

- **Domain**: [LegallyDelegatedAuthority](<https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority>)
- **Range**: [DelegatedLegalAuthority](/concepts/fibo/FND/Law/LegalCapacity/DelegatedLegalAuthority.md)
- **Subproperty of**: [hasCapacity](/concepts/fibo/FND/Law/LegalCapacity/hasCapacity.md)

## Annotations

- **label**: has vested in it
- **definition**: indicates the delegated legal authority that is vested in the controlling party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
