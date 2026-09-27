---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a means by which something (in the case of a network address) or some entity may be located or contacted
      or may receive correspondence
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/Address.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Address
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddress
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: has address
type: Ontology Property
---

# has address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddress>

## Definition

indicates a means by which something (in the case of a network address) or some entity may be located or contacted or may receive correspondence

## Relationships

- **Range**: [Address](/concepts/fibo/FND/Places/Addresses/Address.md)
- **Subproperty of**: [isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)

## Annotations

- **label**: has address
- **definition**: indicates a means by which something (in the case of a network address) or some entity may be located or contacted or may receive correspondence

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
