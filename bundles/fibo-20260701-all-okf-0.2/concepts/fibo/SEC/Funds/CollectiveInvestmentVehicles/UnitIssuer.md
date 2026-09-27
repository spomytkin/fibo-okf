---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unit issuer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The party which issues the Fund Unit.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/issues
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/UnitIssuer
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: unit issuer
type: Ontology Class
---

# unit issuer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/UnitIssuer>

## Definition

The party which issues the Fund Unit.

## Relationships

- **Subclass of**: [FundsProcessingParty](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md)

## Constraints

- **[issues](/concepts/fibo/FND/Relations/Relations/issues.md)**: some values from of type [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [Corporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md)

## Annotations

- **label** (en): unit issuer
- **definition** (en): The party which issues the Fund Unit.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
