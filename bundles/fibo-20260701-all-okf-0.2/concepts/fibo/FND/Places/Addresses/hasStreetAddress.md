---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has street address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a fully-specified address component that consists of a primary address number, predirectional, street
      name, suffix, postdirectional, and an optional secondary unit
  domain:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/StreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasStreetAddress
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: has street address
type: Ontology Property
---

# has street address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasStreetAddress>

## Definition

indicates a fully-specified address component that consists of a primary address number, predirectional, street name, suffix, postdirectional, and an optional secondary unit

## Relationships

- **Domain**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)
- **Range**: [StreetAddress](/concepts/fibo/FND/Places/Addresses/StreetAddress.md)
- **Subproperty of**: [comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)

## Annotations

- **label**: has street address
- **definition**: indicates a fully-specified address component that consists of a primary address number, predirectional, street name, suffix, postdirectional, and an optional secondary unit

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
