---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has street suffix
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies an additional qualifier for a street or other delivery location, such as a dwelling located along a waterway
  domain:
  - concept: /concepts/fibo/FND/Places/Addresses/StreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetAddress
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/StreetSuffix.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetSuffix
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasStreetSuffix
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: has street suffix
type: Ontology Property
---

# has street suffix

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasStreetSuffix>

## Definition

specifies an additional qualifier for a street or other delivery location, such as a dwelling located along a waterway

## Relationships

- **Domain**: [StreetAddress](/concepts/fibo/FND/Places/Addresses/StreetAddress.md)
- **Range**: [StreetSuffix](/concepts/fibo/FND/Places/Addresses/StreetSuffix.md)
- **Subproperty of**: [comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)

## Annotations

- **label**: has street suffix
- **definition**: specifies an additional qualifier for a street or other delivery location, such as a dwelling located along a waterway

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
