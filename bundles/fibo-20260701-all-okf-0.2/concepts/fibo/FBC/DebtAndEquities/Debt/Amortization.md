---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: amortization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the process of reduction of debt or other costs through periodic charges to assets or liabilities, such as through
      principal payments on mortgages
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debt
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isAmortizationOf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/Role
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Amortization
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: amortization
type: Ontology Class
---

# amortization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Amortization>

## Definition

the process of reduction of debt or other costs through periodic charges to assets or liabilities, such as through principal payments on mortgages

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [Role](<https://www.omg.org/spec/Commons/RolesAndCompositions/Role>)

## Constraints

- **[isAmortizationOf](/concepts/fibo/FBC/DebtAndEquities/Debt/isAmortizationOf.md)**: min qualified cardinality 0 of type [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt/Debt.md)

## Annotations

- **label**: amortization
- **definition**: the process of reduction of debt or other costs through periodic charges to assets or liabilities, such as through principal payments on mortgages

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
