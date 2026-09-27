---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: revolving line of credit
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit facility that enables the borrower to withdraw funds, repay, and withdraw again
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Revolving credit facilities are essentially lines of credit with variable interest rates.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CommittedCreditFacility
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/RevolvingLineOfCredit
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: revolving line of credit
type: Ontology Class
---

# revolving line of credit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/RevolvingLineOfCredit>

## Definition

credit facility that enables the borrower to withdraw funds, repay, and withdraw again

## Relationships

- **Subclass of**: [CommittedCreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md)

## Constraints

- **[isCollateralizedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizedBy.md)**: min qualified cardinality 0 of type [Collateral](/concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md)

## Annotations

- **label** (en): revolving line of credit
- **definition** (en): credit facility that enables the borrower to withdraw funds, repay, and withdraw again
- **explanatoryNote** (en): Revolving credit facilities are essentially lines of credit with variable interest rates.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
