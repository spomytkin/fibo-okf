---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collateral value as of date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: appraised value of the collateral for an obligation as of a given date
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/hasDateOfAssessment
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/isEstimatedValueOf
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AppraisedValue.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AppraisedValue
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: collateral value as of date
type: Ontology Class
---

# collateral value as of date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate>

## Definition

appraised value of the collateral for an obligation as of a given date

## Relationships

- **Subclass of**: [AppraisedValue](/concepts/fibo/FND/Arrangements/Assessments/AppraisedValue.md)

## Constraints

- **[hasDateOfAssessment](/concepts/fibo/FND/Arrangements/Assessments/hasDateOfAssessment.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[isEstimatedValueOf](/concepts/fibo/FND/Arrangements/Assessments/isEstimatedValueOf.md)**: some values from of type [Collateral](/concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md)

## Annotations

- **label**: collateral value as of date
- **definition**: appraised value of the collateral for an obligation as of a given date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
