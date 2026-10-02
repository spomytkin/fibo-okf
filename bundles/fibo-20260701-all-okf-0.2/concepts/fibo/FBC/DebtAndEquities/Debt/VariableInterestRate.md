---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: variable interest rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an interest rate that is allowed to vary over the maturity of a loan or other debt instrument
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: adjustable rate
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  disjoint_with:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/FixedInterestRate.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/FixedInterestRate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/VariableInterestRate
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: variable interest rate
type: Ontology Class
---

# variable interest rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/VariableInterestRate>

## Definition

an interest rate that is allowed to vary over the maturity of a loan or other debt instrument

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)

## Constraints

- **Disjoint with**: [FixedInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/FixedInterestRate.md)

## Annotations

- **label**: variable interest rate
- **definition**: an interest rate that is allowed to vary over the maturity of a loan or other debt instrument
- **synonym**: adjustable rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
