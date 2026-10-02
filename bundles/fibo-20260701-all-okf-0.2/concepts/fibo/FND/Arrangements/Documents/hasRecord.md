---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has record
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links something to a record that pertains to it
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Documents/Record
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasRecord
sources:
- id: fibo-source-2c96776dff
  resource: references/fibo/FND/Arrangements/Documents.rdf
  sha256: 2c96776dff29d1955d3d578e07bfed955f6c287acc775b1159190f62e9d82ef3
  title: FIBO source FND/Arrangements/Documents.rdf
title: has record
type: Ontology Property
---

# has record

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasRecord>

## Definition

links something to a record that pertains to it

## Relationships

- **Range**: [Record](<https://www.omg.org/spec/Commons/Documents/Record>)
- **Subproperty of**: [comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)

## Annotations

- **label**: has record
- **definition**: links something to a record that pertains to it

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
