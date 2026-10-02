---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: calculation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: actual execution of some computation, computational process, or operation that was scheduled or triggered by something
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/CalculationEvent
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValueRange
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValueRange
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Calculation
sources:
- id: fibo-source-406cc745cc
  resource: references/fibo/FND/DatesAndTimes/Occurrences.rdf
  sha256: 406cc745cc7d791f79c22e8e117f06460564cc81d90a6349ea20adeb5766198c
  title: FIBO source FND/DatesAndTimes/Occurrences.rdf
title: calculation
type: Ontology Class
---

# calculation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Calculation>

## Definition

actual execution of some computation, computational process, or operation that was scheduled or triggered by something

## Relationships

- **Subclass of**: [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Constraints

- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [CalculationEvent](/concepts/fibo/FND/DatesAndTimes/Occurrences/CalculationEvent.md)
- **[hasExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression>)**: min qualified cardinality 0 of type [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)
- **[hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)**: min qualified cardinality 0 of type [ScalarQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue>)
- **[hasQuantityValueRange](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValueRange>)**: min qualified cardinality 0 of type [ScalarQuantityValueRange](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValueRange>)

## Annotations

- **label**: calculation
- **definition**: actual execution of some computation, computational process, or operation that was scheduled or triggered by something

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
