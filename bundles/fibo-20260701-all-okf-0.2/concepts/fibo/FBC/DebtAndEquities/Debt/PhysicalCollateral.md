---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: physical collateral
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: asset pledged as collateral that has a material form, i.e., is a physical asset of the obligor
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples of physical collateral include, but are not limited to, real estate, equipment, vehicles, spare parts,
      inventory, goods, supplies, fixtures, and leasehold improvements.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/PhysicalAsset
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizationOf
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PhysicalCollateral
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: physical collateral
type: Ontology Class
---

# physical collateral

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PhysicalCollateral>

## Definition

asset pledged as collateral that has a material form, i.e., is a physical asset of the obligor

## Relationships

- **Subclass of**: [Collateral](/concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md)

## Constraints

- **[isCollateralizationOf](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizationOf.md)**: min qualified cardinality 0 of type [PhysicalAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/PhysicalAsset.md)

## Annotations

- **label**: physical collateral
- **definition**: asset pledged as collateral that has a material form, i.e., is a physical asset of the obligor
- **example**: Examples of physical collateral include, but are not limited to, real estate, equipment, vehicles, spare parts, inventory, goods, supplies, fixtures, and leasehold improvements.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
