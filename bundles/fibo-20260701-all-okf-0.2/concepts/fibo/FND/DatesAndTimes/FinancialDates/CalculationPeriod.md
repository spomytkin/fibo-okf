---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: calculation period
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: explicit period from the start to the end of a specific interval or range within which a computational process
      or operation occurs
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculationPeriodLength
    kind: max_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculationPeriod
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: calculation period
type: Ontology Class
---

# calculation period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculationPeriod>

## Definition

explicit period from the start to the end of a specific interval or range within which a computational process or operation occurs

## Relationships

- **Subclass of**: [ExplicitDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod>)

## Constraints

- **[hasDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration>)**: max qualified cardinality 1 of type [CalculationPeriodLength](/concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculationPeriodLength.md)

## Annotations

- **label**: calculation period
- **definition**: explicit period from the start to the end of a specific interval or range within which a computational process or operation occurs

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
