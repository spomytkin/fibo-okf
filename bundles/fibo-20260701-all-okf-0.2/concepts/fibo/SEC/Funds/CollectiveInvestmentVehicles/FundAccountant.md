---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund accountant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The party that keeps accounting records of the available assets and liabilities of the Fund. It calculates dealing
      prices, the Net Asset Value (NAV) of the Fund, and may provide fund performance and tax data. Can be subcontracted by
      the FundAdministrator.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundAccountant
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund accountant
type: Ontology Class
---

# fund accountant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundAccountant>

## Definition

The party that keeps accounting records of the available assets and liabilities of the Fund. It calculates dealing prices, the Net Asset Value (NAV) of the Fund, and may provide fund performance and tax data. Can be subcontracted by the FundAdministrator.

## Relationships

- **Subclass of**: [FundsProcessingParty](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md)

## Annotations

- **label** (en): fund accountant
- **definition** (en): The party that keeps accounting records of the available assets and liabilities of the Fund. It calculates dealing prices, the Net Asset Value (NAV) of the Fund, and may provide fund performance and tax data. Can be subcontracted by the FundAdministrator.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
