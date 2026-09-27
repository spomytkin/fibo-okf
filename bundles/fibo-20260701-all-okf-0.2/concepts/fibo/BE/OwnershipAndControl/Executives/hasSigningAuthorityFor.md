---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has signing authority for
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the party for which a signatory has the ability to sign agreements, access accounts and perform related
      tasks
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/Signatory.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Signatory
  inverse_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/designatesSignatory.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/designatesSignatory
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/isAuthorizedBy
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasSigningAuthorityFor
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: has signing authority for
type: Ontology Property
---

# has signing authority for

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasSigningAuthorityFor>

## Definition

indicates the party for which a signatory has the ability to sign agreements, access accounts and perform related tasks

## Relationships

- **Domain**: [Signatory](/concepts/fibo/BE/OwnershipAndControl/Executives/Signatory.md)
- **Inverse of**: [designatesSignatory](/concepts/fibo/BE/OwnershipAndControl/Executives/designatesSignatory.md)
- **Subproperty of**: [isAuthorizedBy](<https://www.omg.org/spec/Commons/BusinessAuthorizations/isAuthorizedBy>)

## Annotations

- **label**: has signing authority for
- **definition**: indicates the party for which a signatory has the ability to sign agreements, access accounts and perform related tasks

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
