---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ZIP+4 Code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: nine-digit number consisting of five digits, a hyphen, and four digits, which the USPS describes by its trademark
      ZIP+4
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The correct format for a numeric ZIP+4 code is five digits, a hyphen, and four digits. The first five digits represent
      the 5-digit ZIP Code; the sixth and seventh digits (the first two after the hyphen) identify an area known as a sector;
      the eighth and ninth digits identify a smaller area known as a segment. Together, the final four digits identify geographic
      units such as a side of a street between intersections, both sides of a street between intersections, a building, a
      floor or group of floors in a building, a firm within a building, a span of boxes on a rural route, or a group of Post
      Office boxes to which a single USPS employee makes delivery.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/Postcode.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Postcode
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/ZIPPlus4Code
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: ZIP+4 Code
type: Ontology Class
---

# ZIP+4 Code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/ZIPPlus4Code>

## Definition

nine-digit number consisting of five digits, a hyphen, and four digits, which the USPS describes by its trademark ZIP+4

## Relationships

- **Subclass of**: [Postcode](/concepts/fibo/FND/Places/Addresses/Postcode.md)

## Annotations

- **label**: ZIP+4 Code
- **definition**: nine-digit number consisting of five digits, a hyphen, and four digits, which the USPS describes by its trademark ZIP+4
- **explanatoryNote**: The correct format for a numeric ZIP+4 code is five digits, a hyphen, and four digits. The first five digits represent the 5-digit ZIP Code; the sixth and seventh digits (the first two after the hyphen) identify an area known as a sector; the eighth and ninth digits identify a smaller area known as a segment. Together, the final four digits identify geographic units such as a side of a street between intersections, both sides of a street between intersections, a building, a floor or group of floors in a building, a firm within a building, a span of boxes on a rural route, or a group of Post Office boxes to which a single USPS employee makes delivery.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
