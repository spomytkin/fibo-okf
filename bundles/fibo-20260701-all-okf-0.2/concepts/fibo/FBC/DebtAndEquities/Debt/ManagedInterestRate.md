---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: managed interest rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: variable interest rate charged by a financial institution for borrowing that is not prescribed as a margin over
      base rate but is set from time to time by the institution
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/VariableInterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/VariableInterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ManagedInterestRate
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: managed interest rate
type: Ontology Class
---

# managed interest rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ManagedInterestRate>

## Definition

variable interest rate charged by a financial institution for borrowing that is not prescribed as a margin over base rate but is set from time to time by the institution

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [VariableInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/VariableInterestRate.md)

## Constraints

- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: some values from of type [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Annotations

- **label**: managed interest rate
- **definition**: variable interest rate charged by a financial institution for borrowing that is not prescribed as a margin over base rate but is set from time to time by the institution

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
