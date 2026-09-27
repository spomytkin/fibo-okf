---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: urbanization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an area, sector, or development within a larger geographic area
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This URB descriptor, commonly used in urban areas of Puerto Rico, is an important part of the addressing format,
      as it describes the location of a given street.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Locations/CountrySubdivision
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/Urbanization
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: urbanization
type: Ontology Class
---

# urbanization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/Urbanization>

## Definition

an area, sector, or development within a larger geographic area

## Relationships

- **Subclass of**: [CountrySubdivision](<https://www.omg.org/spec/Commons/Locations/CountrySubdivision>)

## Annotations

- **label**: urbanization
- **definition**: an area, sector, or development within a larger geographic area
- **explanatoryNote**: This URB descriptor, commonly used in urban areas of Puerto Rico, is an important part of the addressing format, as it describes the location of a given street.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
