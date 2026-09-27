---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund bond class unit
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A fund unit which takes the form of debt in that fund.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'From EFAMA Review: called denominations e.g. issued in $5000 pieces. You cannot buy fractional amounts in a bond.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionPolicy
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundBondUnitCoupon
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasExpectedCoupon
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/Funds/FundUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundBondClassUnit
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund bond class unit
type: Ontology Class
---

# fund bond class unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundBondClassUnit>

## Definition

A fund unit which takes the form of debt in that fund.

## Relationships

- **Subclass of**: [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)

## Constraints

- **[hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)**: some values from of type [FundUnitDistributionPolicy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionPolicy.md)
- **[hasExpectedCoupon](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasExpectedCoupon.md)**: some values from of type [FundBondUnitCoupon](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundBondUnitCoupon.md)

## Annotations

- **label** (en): fund bond class unit
- **definition** (en): A fund unit which takes the form of debt in that fund.
- **explanatoryNote** (en): From EFAMA Review: called denominations e.g. issued in $5000 pieces. You cannot buy fractional amounts in a bond.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
