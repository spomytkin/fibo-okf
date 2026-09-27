---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has subtrahend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the quantity value that is subtracted from something
  domain:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Difference.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Difference
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasSubtrahend
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has subtrahend
type: Ontology Property
---

# has subtrahend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasSubtrahend>

## Definition

specifies the quantity value that is subtracted from something

## Relationships

- **Domain**: [Difference](/concepts/fibo/FND/Utilities/Analytics/Difference.md)
- **Subproperty of**: [hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)

## Annotations

- **label**: has subtrahend
- **definition**: specifies the quantity value that is subtracted from something

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
