---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has data provider
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: has an organization which is the data provider and is legally responsible for the information provided
  domain:
  - concept: /concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle
  range:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/fundHasRelatedParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/fundHasRelatedParty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasDataProvider
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: has data provider
type: Ontology Property
---

# has data provider

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasDataProvider>

## Definition

has an organization which is the data provider and is legally responsible for the information provided

## Relationships

- **Domain**: [CollectiveInvestmentVehicle](/concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)
- **Range**: [MarketDataProvider](/concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md)
- **Subproperty of**: [fundHasRelatedParty](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/fundHasRelatedParty.md)

## Annotations

- **label** (en): has data provider
- **definition** (en): has an organization which is the data provider and is legally responsible for the information provided

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
