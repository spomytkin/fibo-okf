---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: minimum initial subscription units
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Minimum initial number of units/shares that must be purchased.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#integer
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/minimumInitialSubscriptionUnits
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: minimum initial subscription units
type: Ontology Property
---

# minimum initial subscription units

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/minimumInitialSubscriptionUnits>

## Definition

Minimum initial number of units/shares that must be purchased.

## Relationships

- **Domain**: [FundSubscriptionTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md)
- **Range**: [integer](<http://www.w3.org/2001/XMLSchema#integer>)

## Annotations

- **label** (en): minimum initial subscription units
- **definition** (en): Minimum initial number of units/shares that must be purchased.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
