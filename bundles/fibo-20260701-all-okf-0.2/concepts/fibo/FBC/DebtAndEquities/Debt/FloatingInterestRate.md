---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: floating interest rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: variable interest rate that is based on a specific index or benchmark rate
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Certain revolving credit, such as credit-card related debt, may adjust after a specified period of time to an absolute
      rate stated in the agreement (variable but not floating) rather than based on a benchmark rate (variable, floating).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The index used to determine the specific interest rate is generally included in the terms of the loan. In most
      cases, lenders will also charge a spread, or added percentage points on top of the established index rate. If a loan
      is billed as prime plus 2.5 percent, for a prime rate of 3.5 percent, the terms of the loan will require the borrower
      to pay off a 6 percent interest. Floating interest rates typically involve periodic reset dates for the loan, particularly
      when the index rate changes. Resets may also occur online at market predetermined intervals, with yearly adjustments
      being a common arrangement.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://recomparison.com/comparisons/100975/floating-vs-variable-vs-adjustable-interest-rate/
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/VariableInterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/VariableInterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/FloatingInterestRate
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: floating interest rate
type: Ontology Class
---

# floating interest rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/FloatingInterestRate>

## Definition

variable interest rate that is based on a specific index or benchmark rate

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **See also**: [floating-vs-variable-vs-adjustable-interest-rate](<http://recomparison.com/comparisons/100975/floating-vs-variable-vs-adjustable-interest-rate/>)
- **Subclass of**: [VariableInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/VariableInterestRate.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: exact qualified cardinality 1 of type [ReferenceInterestRate](/concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md)

## Annotations

- **label**: floating interest rate
- **definition**: variable interest rate that is based on a specific index or benchmark rate
- **example**: Certain revolving credit, such as credit-card related debt, may adjust after a specified period of time to an absolute rate stated in the agreement (variable but not floating) rather than based on a benchmark rate (variable, floating).
- **explanatoryNote**: The index used to determine the specific interest rate is generally included in the terms of the loan. In most cases, lenders will also charge a spread, or added percentage points on top of the established index rate. If a loan is billed as prime plus 2.5 percent, for a prime rate of 3.5 percent, the terms of the loan will require the borrower to pay off a 6 percent interest. Floating interest rates typically involve periodic reset dates for the loan, particularly when the index rate changes. Resets may also occur online at market predetermined intervals, with yearly adjustments being a common arrangement.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
