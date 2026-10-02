---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has relative comparative date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a date against which the value of a scoped measure is compared (e.g., one month prior, three months prior,
      etc., and typically against a prior release or average over prior releases)
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/RelativeDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RelativeDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasRelativeComparativeDate
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has relative comparative date
type: Ontology Property
---

# has relative comparative date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasRelativeComparativeDate>

## Definition

specifies a date against which the value of a scoped measure is compared (e.g., one month prior, three months prior, etc., and typically against a prior release or average over prior releases)

## Relationships

- **Range**: [RelativeDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RelativeDate.md)
- **Subproperty of**: [hasDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDate>)

## Annotations

- **label**: has relative comparative date
- **definition**: specifies a date against which the value of a scoped measure is compared (e.g., one month prior, three months prior, etc., and typically against a prior release or average over prior releases)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
