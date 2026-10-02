---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial record
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: record of financial information
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Financial records include accounts, agreements, trading books, etc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Record
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/FinancialRecord
sources:
- id: fibo-source-2c96776dff
  resource: references/fibo/FND/Arrangements/Documents.rdf
  sha256: 2c96776dff29d1955d3d578e07bfed955f6c287acc775b1159190f62e9d82ef3
  title: FIBO source FND/Arrangements/Documents.rdf
title: financial record
type: Ontology Class
---

# financial record

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/FinancialRecord>

## Definition

record of financial information

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)
- **Subclass of**: [Record](<https://www.omg.org/spec/Commons/Documents/Record>)

## Annotations

- **label**: financial record
- **definition**: record of financial information
- **example**: Financial records include accounts, agreements, trading books, etc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
