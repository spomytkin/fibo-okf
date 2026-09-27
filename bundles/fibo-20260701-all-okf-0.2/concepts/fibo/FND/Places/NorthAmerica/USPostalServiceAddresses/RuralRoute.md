---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: highway contract route address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: mail route outside the city or township limits in a rural area associated with an address
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/comprises
    value: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/RuralRouteDesignator
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/SupplementalAddressComponent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressComponent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/RuralRoute
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: highway contract route address
type: Ontology Class
---

# highway contract route address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/RuralRoute>

## Definition

mail route outside the city or township limits in a rural area associated with an address

## Relationships

- **Subclass of**: [SupplementalAddressComponent](/concepts/fibo/FND/Places/Addresses/SupplementalAddressComponent.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/RuralRouteDesignator`

## Annotations

- **label**: highway contract route address
- **definition**: mail route outside the city or township limits in a rural area associated with an address

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
