---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has observed value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a collection of values over which some analysis is performed
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For certain calculations, such as certain measures of dispersion, date value pairs are expected as input, in other
      words, a dated structured collection.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Collections/StructuredCollection
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasObservedValue
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has observed value
type: Ontology Property
---

# has observed value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasObservedValue>

## Definition

specifies a collection of values over which some analysis is performed

## Relationships

- **Range**: [StructuredCollection](<https://www.omg.org/spec/Commons/Collections/StructuredCollection>)
- **Subproperty of**: [hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)

## Annotations

- **label**: has observed value
- **definition**: specifies a collection of values over which some analysis is performed
- **explanatoryNote**: For certain calculations, such as certain measures of dispersion, date value pairs are expected as input, in other words, a dated structured collection.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
