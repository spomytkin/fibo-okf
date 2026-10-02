---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: relative date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: calculated date that is some duration before or after another date
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'A settlement date, defined as T+3: three days after the trade date. The ''hasRelativeDuration'' property is set
      to ''3D''.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: When the 'hasRelativeDuration' property is negative, the RelativeDate is before the 'isRelativeTo' Date; otherwise
      the RelativeDate is after the 'isRelativeTo' Date.
  disjoint_with:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/SpecifiedDate.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/SpecifiedDate
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceBasedDate.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceBasedDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasRelativeDuration
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/isRelativeTo
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculatedDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RelativeDate
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
- id: fibo-source-406cc745cc
  resource: references/fibo/FND/DatesAndTimes/Occurrences.rdf
  sha256: 406cc745cc7d791f79c22e8e117f06460564cc81d90a6349ea20adeb5766198c
  title: FIBO source FND/DatesAndTimes/Occurrences.rdf
title: relative date
type: Ontology Class
---

# relative date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RelativeDate>

## Definition

calculated date that is some duration before or after another date

## Relationships

- **Subclass of**: [CalculatedDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md)

## Constraints

- **Disjoint with**: [SpecifiedDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/SpecifiedDate.md)
- **Disjoint with**: [OccurrenceBasedDate](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceBasedDate.md)
- **[hasRelativeDuration](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasRelativeDuration.md)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[isRelativeTo](/concepts/fibo/FND/DatesAndTimes/FinancialDates/isRelativeTo.md)**: exact qualified cardinality 1 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label**: relative date
- **definition**: calculated date that is some duration before or after another date
- **example**: A settlement date, defined as T+3: three days after the trade date. The 'hasRelativeDuration' property is set to '3D'.
- **explanatoryNote**: When the 'hasRelativeDuration' property is negative, the RelativeDate is before the 'isRelativeTo' Date; otherwise the RelativeDate is after the 'isRelativeTo' Date.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
