---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: target indicator value
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: target value for a key performance indicator as of a specific date and time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TargetIndicatorValue
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: target indicator value
type: Ontology Class
---

# target indicator value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TargetIndicatorValue>

## Definition

target value for a key performance indicator as of a specific date and time

## Relationships

- **Subclass of**: [DatedCollectionConstituent](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)

## Constraints

- **[hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)**: some values from of type [ScalarQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue>)

## Annotations

- **label** (en): target indicator value
- **definition** (en): target value for a key performance indicator as of a specific date and time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
