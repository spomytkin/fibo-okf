---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: geometric mean
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: mean that indicates the central tendency or typical value of a set of numbers by using the product of their values
      (as opposed to the arithmetic mean which uses their sum)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The geometric mean is defined as the nth root of the product of n numbers. A geometric mean is often used when
      comparing different items - finding a single 'figure of merit' for these items - when each item has multiple properties
      that have different numeric ranges. For example, the geometric mean can give a meaningful 'average' to compare two companies
      which are each rated at 0 to 5 for their environmental sustainability, and are rated at 0 to 100 for their financial
      viability. If an arithmetic mean were used instead of a geometric mean, the financial viability is given more weight
      because its numeric range is larger - so a small percentage change in the financial rating (e.g. going from 80 to 90)
      makes a much larger difference in the arithmetic mean than a large percentage change in environmental sustainability
      (e.g. going from 2 to 5).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Mean.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Mean
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/GeometricMean
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: geometric mean
type: Ontology Class
---

# geometric mean

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/GeometricMean>

## Definition

mean that indicates the central tendency or typical value of a set of numbers by using the product of their values (as opposed to the arithmetic mean which uses their sum)

## Relationships

- **Subclass of**: [Mean](/concepts/fibo/FND/Utilities/Analytics/Mean.md)

## Annotations

- **label**: geometric mean
- **definition**: mean that indicates the central tendency or typical value of a set of numbers by using the product of their values (as opposed to the arithmetic mean which uses their sum)
- **explanatoryNote**: The geometric mean is defined as the nth root of the product of n numbers. A geometric mean is often used when comparing different items - finding a single 'figure of merit' for these items - when each item has multiple properties that have different numeric ranges. For example, the geometric mean can give a meaningful 'average' to compare two companies which are each rated at 0 to 5 for their environmental sustainability, and are rated at 0 to 100 for their financial viability. If an arithmetic mean were used instead of a geometric mean, the financial viability is given more weight because its numeric range is larger - so a small percentage change in the financial rating (e.g. going from 80 to 90) makes a much larger difference in the arithmetic mean than a large percentage change in environmental sustainability (e.g. going from 2 to 5).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
