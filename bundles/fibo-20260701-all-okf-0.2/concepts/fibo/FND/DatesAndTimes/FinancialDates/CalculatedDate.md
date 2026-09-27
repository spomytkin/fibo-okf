---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: calculated date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: date that is or will be determined based on some formula
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The hasDateValue property of a CalculatedDate is not set until the Date is calculated. Since the calculation may
      depend upon future events that may or may not ever happen, the hasDateValue property may never be set.
  disjoint_with:
  - predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayConvention
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculatedDate
sources:
- id: fibo-source-7e287b0092
  resource: references/fibo/FND/DatesAndTimes/BusinessDates.rdf
  sha256: 7e287b0092247d35e3e8e12b9c1c29cba3b2b4f94d06a6b0c06e85f6c1cc2f62
  title: FIBO source FND/DatesAndTimes/BusinessDates.rdf
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: calculated date
type: Ontology Class
---

# calculated date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculatedDate>

## Definition

date that is or will be determined based on some formula

## Relationships

- **Subclass of**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Constraints

- **Disjoint with**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasBusinessDayConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention.md)**: max qualified cardinality 1 of type [BusinessDayConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessDayConvention.md)

## Annotations

- **label**: calculated date
- **definition**: date that is or will be determined based on some formula
- **explanatoryNote**: The hasDateValue property of a CalculatedDate is not set until the Date is calculated. Since the calculation may depend upon future events that may or may not ever happen, the hasDateValue property may never be set.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
