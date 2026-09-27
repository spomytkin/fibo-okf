---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: difference
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: quantity by which amounts differ; the remainder left after subtraction of one value from another
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    kind: exact_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasMinuend
  - cardinality: 1
    kind: exact_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasSubtrahend
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalMeasure
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Difference
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: difference
type: Ontology Class
---

# difference

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Difference>

## Definition

quantity by which amounts differ; the remainder left after subtraction of one value from another

## Relationships

- **Subclass of**: [StatisticalMeasure](/concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasMinuend](/concepts/fibo/FND/Utilities/Analytics/hasMinuend.md)**: exact cardinality 1
- **[hasSubtrahend](/concepts/fibo/FND/Utilities/Analytics/hasSubtrahend.md)**: exact cardinality 1

## Annotations

- **label**: difference
- **definition**: quantity by which amounts differ; the remainder left after subtraction of one value from another

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
