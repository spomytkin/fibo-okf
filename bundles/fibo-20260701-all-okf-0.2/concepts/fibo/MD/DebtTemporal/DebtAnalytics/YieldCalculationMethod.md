---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: yield calculation method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'The method by which the yield is calculated. This includes a formula for calculation and a specific day count
      convention and compounding. You would apply this calculation method on top of the underlying terms and conditions, do
      for example the holiday calenders and so on, are used in these formulae. For final cash flow: Japanese yield will round
      down accrued interest. Add: The actual underlying math. Wall Street uses the same ICMA formula.'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Initial reviewer notes 18 Nov: this uses the combination of the day count and the compounding gives you the name
      of the yield calculation method. Names are associated with algorithms. What yield you use to determining the present
      value. These are typically defined in a prospectus (for exchange traded) or Info Memorandum if it''s traded in an OTC
      market. where it also defines the method itself. Action: look at some prospecti or get this from a vendor. Additional
      features 25 nov: Question - maybe Holiday calendar? Also date roll rules and roll back rules. These all apply. YC feeds
      in to Yield itself.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasCompoundingFrequency
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationFormula
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasFormula
  - filler: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Variable
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Formula.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Formula
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: yield calculation method
type: Ontology Class
---

# yield calculation method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod>

## Definition

The method by which the yield is calculated. This includes a formula for calculation and a specific day count convention and compounding. You would apply this calculation method on top of the underlying terms and conditions, do for example the holiday calenders and so on, are used in these formulae. For final cash flow: Japanese yield will round down accrued interest. Add: The actual underlying math. Wall Street uses the same ICMA formula.

## Relationships

- **Subclass of**: [Formula](/concepts/fibo/FND/Utilities/Analytics/Formula.md)

## Constraints

- **[hasCompoundingFrequency](/concepts/fibo/FBC/DebtAndEquities/Debt/hasCompoundingFrequency.md)**: all values from of type [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- **[hasFormula](/concepts/fibo/FND/Utilities/Analytics/hasFormula.md)**: some values from of type [YieldCalculationFormula](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationFormula.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: all values from of type [Variable](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Variable>)

## Annotations

- **label** (en): yield calculation method
- **definition** (en): The method by which the yield is calculated. This includes a formula for calculation and a specific day count convention and compounding. You would apply this calculation method on top of the underlying terms and conditions, do for example the holiday calenders and so on, are used in these formulae. For final cash flow: Japanese yield will round down accrued interest. Add: The actual underlying math. Wall Street uses the same ICMA formula.
- **editorialNote** (en): Initial reviewer notes 18 Nov: this uses the combination of the day count and the compounding gives you the name of the yield calculation method. Names are associated with algorithms. What yield you use to determining the present value. These are typically defined in a prospectus (for exchange traded) or Info Memorandum if it's traded in an OTC market. where it also defines the method itself. Action: look at some prospecti or get this from a vendor. Additional features 25 nov: Question - maybe Holiday calendar? Also date roll rules and roll back rules. These all apply. YC feeds in to Yield itself.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
