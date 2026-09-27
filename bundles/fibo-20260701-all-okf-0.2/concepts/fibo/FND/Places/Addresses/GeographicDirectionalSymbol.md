---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: geographic directional symbol
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: code element that gives directional information for postal delivery
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: In the United States, these include N, S, E, W, NE, NW, SE, SW.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/GeographicDirectionalSymbol
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: geographic directional symbol
type: Ontology Class
---

# geographic directional symbol

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/GeographicDirectionalSymbol>

## Definition

code element that gives directional information for postal delivery

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)

## Constraints

- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: geographic directional symbol
- **definition**: code element that gives directional information for postal delivery
- **example**: In the United States, these include N, S, E, W, NE, NW, SE, SW.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
