---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has anchor date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a fixed reference point within a series or timeline
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: With respect to a scoped measure, such as an economic indicator, the anchor date specifies the reference date against
      which the value of a numeric index for a more recent date is compared (i.e., the starting point from which it stems).
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/AnchorDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AnchorDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAnchorDate
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: has anchor date
type: Ontology Property
---

# has anchor date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAnchorDate>

## Definition

specifies a fixed reference point within a series or timeline

## Relationships

- **Range**: [AnchorDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/AnchorDate.md)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label**: has anchor date
- **definition**: specifies a fixed reference point within a series or timeline
- **example**: With respect to a scoped measure, such as an economic indicator, the anchor date specifies the reference date against which the value of a numeric index for a more recent date is compared (i.e., the starting point from which it stems).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
