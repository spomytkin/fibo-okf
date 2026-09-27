---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest calculation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event reflecting the calculation of interest
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Calculation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Calculation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestCalculation
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: interest calculation
type: Ontology Class
---

# interest calculation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestCalculation>

## Definition

event reflecting the calculation of interest

## Relationships

- **Subclass of**: [ContractLifecycleEventOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md)
- **Subclass of**: [Calculation](/concepts/fibo/FND/DatesAndTimes/Occurrences/Calculation.md)

## Constraints

- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: exact qualified cardinality 1 of type [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)
- **[hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)**: exact qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: interest calculation
- **definition**: event reflecting the calculation of interest

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
