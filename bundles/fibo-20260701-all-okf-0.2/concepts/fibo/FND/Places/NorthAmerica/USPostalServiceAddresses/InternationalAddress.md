---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: international address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: physical address that explicitly includes a country
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Locations/Country
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasCountry
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/InternationalAddress
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: international address
type: Ontology Class
---

# international address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/InternationalAddress>

## Definition

physical address that explicitly includes a country

## Relationships

- **Subclass of**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)

## Constraints

- **[hasCountry](<https://www.omg.org/spec/Commons/Locations/hasCountry>)**: exact qualified cardinality 1 of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)

## Annotations

- **label**: international address
- **definition**: physical address that explicitly includes a country

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
