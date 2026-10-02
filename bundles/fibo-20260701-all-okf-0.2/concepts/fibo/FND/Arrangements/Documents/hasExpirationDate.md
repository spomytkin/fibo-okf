---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has expiration date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links something, typically an agreement, contract, document, or perishable item, with an expiration date
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasExpirationDate
sources:
- id: fibo-source-2c96776dff
  resource: references/fibo/FND/Arrangements/Documents.rdf
  sha256: 2c96776dff29d1955d3d578e07bfed955f6c287acc775b1159190f62e9d82ef3
  title: FIBO source FND/Arrangements/Documents.rdf
title: has expiration date
type: Ontology Property
---

# has expiration date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasExpirationDate>

## Definition

links something, typically an agreement, contract, document, or perishable item, with an expiration date

## Relationships

- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **Subproperty of**: [hasEndDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate>)

## Annotations

- **label**: has expiration date
- **definition**: links something, typically an agreement, contract, document, or perishable item, with an expiration date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
