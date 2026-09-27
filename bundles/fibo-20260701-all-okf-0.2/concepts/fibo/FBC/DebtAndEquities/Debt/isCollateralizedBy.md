---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is collateralized by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an agreement to an asset pledged as security
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: is collateralized by
type: Ontology Property
---

# is collateralized by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy>

## Definition

relates an agreement to an asset pledged as security

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Range**: [Collateral](/concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md)

## Annotations

- **label**: is collateralized by
- **definition**: relates an agreement to an asset pledged as security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
