---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has urbanization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates area, sector, or development within a geographic area relevant to a delivery address
  range:
  - concept: /concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/Urbanization.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/Urbanization
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/hasUrbanization
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: has urbanization
type: Ontology Property
---

# has urbanization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/hasUrbanization>

## Definition

indicates area, sector, or development within a geographic area relevant to a delivery address

## Relationships

- **Range**: [Urbanization](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/Urbanization.md)
- **Subproperty of**: [comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)

## Annotations

- **label**: has urbanization
- **definition**: indicates area, sector, or development within a geographic area relevant to a delivery address

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
