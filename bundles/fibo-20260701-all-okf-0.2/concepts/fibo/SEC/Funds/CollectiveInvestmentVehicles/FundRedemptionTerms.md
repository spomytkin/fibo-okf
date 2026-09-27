---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund redemption terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Formal terms for redemption of units in the fund. These set out what the investor and the fund may or may not do.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/ReferToFundOrderDesk
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasAdditionalRedemptionRestrictions
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundRedemptionTerms
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund redemption terms
type: Ontology Class
---

# fund redemption terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundRedemptionTerms>

## Definition

Formal terms for redemption of units in the fund. These set out what the investor and the fund may or may not do.

## Relationships

- **Subclass of**: [FundProcessingTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms.md)

## Constraints

- **[hasAdditionalRedemptionRestrictions](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasAdditionalRedemptionRestrictions.md)**: some values from of type [ReferToFundOrderDesk](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/ReferToFundOrderDesk.md)

## Annotations

- **label** (en): fund redemption terms
- **definition** (en): Formal terms for redemption of units in the fund. These set out what the investor and the fund may or may not do.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
