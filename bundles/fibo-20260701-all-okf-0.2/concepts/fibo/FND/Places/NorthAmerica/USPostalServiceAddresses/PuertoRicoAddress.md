---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Puerto Rico address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: delivery address for a delivery point in Puerto Rico that may include a supplementary address line containing the
      abbreviation 'URB' followed by the name of the urbanization area that is appropriate for that address
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/Urbanization
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/PuertoRicoAddress
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: Puerto Rico address
type: Ontology Class
---

# Puerto Rico address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/PuertoRicoAddress>

## Definition

delivery address for a delivery point in Puerto Rico that may include a supplementary address line containing the abbreviation 'URB' followed by the name of the urbanization area that is appropriate for that address

## Relationships

- **Subclass of**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [Urbanization](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/Urbanization.md)

## Annotations

- **label**: Puerto Rico address
- **definition**: delivery address for a delivery point in Puerto Rico that may include a supplementary address line containing the abbreviation 'URB' followed by the name of the urbanization area that is appropriate for that address

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
