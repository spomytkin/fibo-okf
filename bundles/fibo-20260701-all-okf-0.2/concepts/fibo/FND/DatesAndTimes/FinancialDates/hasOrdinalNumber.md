---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has ordinal number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a number designating place in an ordered sequence, i.e., 1st, 2nd, 3rd, etc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Negative ordinal numbers mean 1st before, 2nd before, etc.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#integer
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasOrdinalNumber
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: has ordinal number
type: Ontology Property
---

# has ordinal number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasOrdinalNumber>

## Definition

specifies a number designating place in an ordered sequence, i.e., 1st, 2nd, 3rd, etc.

## Relationships

- **Range**: [integer](<http://www.w3.org/2001/XMLSchema#integer>)

## Annotations

- **label**: has ordinal number
- **definition**: specifies a number designating place in an ordered sequence, i.e., 1st, 2nd, 3rd, etc.
- **explanatoryNote**: Negative ordinal numbers mean 1st before, 2nd before, etc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
