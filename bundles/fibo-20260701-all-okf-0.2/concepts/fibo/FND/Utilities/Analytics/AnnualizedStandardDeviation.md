---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: annualized standard deviation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: standard deviation for some measure over a specific reference period
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Standard deviation applied to the annual rate of return of an investment provides insights on the historical volatility
      of that investment. The greater the standard deviation of the price of a security, the greater the volatility. Multiplying
      monthly standard deviation by the square root of twelve (12) is an industry standard method of approximating annualized
      standard deviations of monthly returns.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReferencePeriod
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StandardDeviation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StandardDeviation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/AnnualizedStandardDeviation
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: annualized standard deviation
type: Ontology Class
---

# annualized standard deviation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/AnnualizedStandardDeviation>

## Definition

standard deviation for some measure over a specific reference period

## Relationships

- **Subclass of**: [StandardDeviation](/concepts/fibo/FND/Utilities/Analytics/StandardDeviation.md)

## Constraints

- **[hasReferencePeriod](/concepts/fibo/FND/Utilities/Analytics/hasReferencePeriod.md)**: exact qualified cardinality 1 of type [ExplicitRecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval.md)

## Annotations

- **label**: annualized standard deviation
- **definition**: standard deviation for some measure over a specific reference period
- **explanatoryNote**: Standard deviation applied to the annual rate of return of an investment provides insights on the historical volatility of that investment. The greater the standard deviation of the price of a security, the greater the volatility. Multiplying monthly standard deviation by the square root of twelve (12) is an industry standard method of approximating annualized standard deviations of monthly returns.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
