---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is initially controlled on
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date or date and time that some level of authority or influence was first put in place
  characteristics:
  - functional
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  - http://www.w3.org/2002/07/owl#FunctionalProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isInitiallyControlledOn
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: is initially controlled on
type: Ontology Property
---

# is initially controlled on

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isInitiallyControlledOn>

## Definition

indicates the date or date and time that some level of authority or influence was first put in place

## Relationships

- **Range**: [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **Subproperty of**: [hasObservedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime>)

## Annotations

- **label**: is initially controlled on
- **definition**: indicates the date or date and time that some level of authority or influence was first put in place

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
