---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: accrued interest
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: amount of interest that has been incurred, as of a specific date, on a loan or other financial obligation but has
      not yet been paid out
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Accrued interest refers to the interest that has accumulated on a bond or other financial obligation since the
      last interest payment up to, but not including, the settlement date. This interest is earned over time but not yet paid
      out to the bondholder, for example. If this is a dirty price, this is the amount of accrued interest that is included
      in the price. This is therefore passed on to the purchaser of the bond or debt instrument.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAsOfDate
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Interest.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Interest
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/AccruedInterest
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: accrued interest
type: Ontology Class
---

# accrued interest

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/AccruedInterest>

## Definition

amount of interest that has been incurred, as of a specific date, on a loan or other financial obligation but has not yet been paid out

## Relationships

- **Subclass of**: [Interest](/concepts/fibo/FBC/DebtAndEquities/Debt/Interest.md)

## Constraints

- **[hasAsOfDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAsOfDate.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)

## Annotations

- **label** (en): accrued interest
- **definition**: amount of interest that has been incurred, as of a specific date, on a loan or other financial obligation but has not yet been paid out
- **explanatoryNote** (en): Accrued interest refers to the interest that has accumulated on a bond or other financial obligation since the last interest payment up to, but not including, the settlement date. This interest is earned over time but not yet paid out to the bondholder, for example. If this is a dirty price, this is the amount of accrued interest that is included in the price. This is therefore passed on to the purchaser of the bond or debt instrument.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
