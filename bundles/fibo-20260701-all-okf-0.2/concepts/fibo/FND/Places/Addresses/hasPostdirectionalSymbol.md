---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has postdirectional symbol
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a geographic directional symbol that follows the street name and street suffix in a street address
  domain:
  - concept: /concepts/fibo/FND/Places/Addresses/StreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetAddress
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/PostdirectionalSymbol.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostdirectionalSymbol
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostdirectionalSymbol
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: has postdirectional symbol
type: Ontology Property
---

# has postdirectional symbol

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostdirectionalSymbol>

## Definition

specifies a geographic directional symbol that follows the street name and street suffix in a street address

## Relationships

- **Domain**: [StreetAddress](/concepts/fibo/FND/Places/Addresses/StreetAddress.md)
- **Range**: [PostdirectionalSymbol](/concepts/fibo/FND/Places/Addresses/PostdirectionalSymbol.md)
- **Subproperty of**: [comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)

## Annotations

- **label**: has postdirectional symbol
- **definition**: specifies a geographic directional symbol that follows the street name and street suffix in a street address

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
