---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has initial assignment date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the date on which an identifier is first assigned to some resource
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/hasInitialAssignmentDate
sources:
- id: fibo-source-2943e244c9
  resource: references/fibo/FND/Arrangements/IdentifiersAndIndices.rdf
  sha256: 2943e244c9f1e05582f4cd0ce73c69f5f8a148d740aa66d458c621a1ad24f51c
  title: FIBO source FND/Arrangements/IdentifiersAndIndices.rdf
title: has initial assignment date
type: Ontology Property
---

# has initial assignment date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/hasInitialAssignmentDate>

## Definition

the date on which an identifier is first assigned to some resource

## Relationships

- **Range**: [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **Subproperty of**: [hasObservedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime>)

## Annotations

- **label**: has initial assignment date
- **definition**: the date on which an identifier is first assigned to some resource

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
