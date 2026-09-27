---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has interest rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something, such as an agreement, or debt instrument, to the rate (typically annual) of interest that is
      to be paid by the debtor to the creditor on the debt
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has interest rate
type: Ontology Property
---

# has interest rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate>

## Definition

relates something, such as an agreement, or debt instrument, to the rate (typically annual) of interest that is to be paid by the debtor to the creditor on the debt

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Range**: [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)
- **Subproperty of**: [hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)

## Annotations

- **label**: has interest rate
- **definition**: relates something, such as an agreement, or debt instrument, to the rate (typically annual) of interest that is to be paid by the debtor to the creditor on the debt

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
