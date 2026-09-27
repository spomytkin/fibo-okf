---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has target value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a collection of values that represent planned or projected goals or objectives for some something over
      time
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasTargetValue
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has target value
type: Ontology Property
---

# has target value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasTargetValue>

## Definition

specifies a collection of values that represent planned or projected goals or objectives for some something over time

## Relationships

- **Range**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- **Subproperty of**: [hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)

## Annotations

- **label**: has target value
- **definition**: specifies a collection of values that represent planned or projected goals or objectives for some something over time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
