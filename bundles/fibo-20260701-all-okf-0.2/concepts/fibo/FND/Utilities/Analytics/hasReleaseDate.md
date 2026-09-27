---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has release date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the date on which something is published
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A release date is typically a date fixed in advance for the release of a film, recording, document, report, or
      product or publication.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReleaseDate
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has release date
type: Ontology Property
---

# has release date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReleaseDate>

## Definition

specifies the date on which something is published

## Relationships

- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **Subproperty of**: [hasDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDate>)

## Annotations

- **label**: has release date
- **definition**: specifies the date on which something is published
- **explanatoryNote**: A release date is typically a date fixed in advance for the release of a film, recording, document, report, or product or publication.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
