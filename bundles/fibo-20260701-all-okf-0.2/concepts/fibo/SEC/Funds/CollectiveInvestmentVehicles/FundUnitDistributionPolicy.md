---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund unit distribution policy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: policy relating to the unit, e.g. if income is paid out or retained in the fund and how this is treated, including
      distribution policy details for dividends and coupons.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Policy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Policy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionPolicy
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund unit distribution policy
type: Ontology Class
---

# fund unit distribution policy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionPolicy>

## Definition

policy relating to the unit, e.g. if income is paid out or retained in the fund and how this is treated, including distribution policy details for dividends and coupons.

## Relationships

- **Subclass of**: [Policy](/concepts/fibo/FND/Law/LegalCapacity/Policy.md)

## Constraints

- **[hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)**: some values from of type [FundUnitDistributionMethod](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionMethod.md)

## Annotations

- **label** (en): fund unit distribution policy
- **definition** (en): policy relating to the unit, e.g. if income is paid out or retained in the fund and how this is treated, including distribution policy details for dividends and coupons.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
