---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: designates signatory
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: authorizes to sign agreements, access accounts and/or perform other similar tasks
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/Signatory.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Signatory
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/authorizes
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Organizations/designates
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/designatesSignatory
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: designates signatory
type: Ontology Property
---

# designates signatory

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/designatesSignatory>

## Definition

authorizes to sign agreements, access accounts and/or perform other similar tasks

## Relationships

- **Range**: [Signatory](/concepts/fibo/BE/OwnershipAndControl/Executives/Signatory.md)
- **Subproperty of**: [authorizes](<https://www.omg.org/spec/Commons/BusinessAuthorizations/authorizes>)
- **Subproperty of**: [designates](<https://www.omg.org/spec/Commons/Organizations/designates>)

## Annotations

- **label**: designates signatory
- **definition**: authorizes to sign agreements, access accounts and/or perform other similar tasks

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
