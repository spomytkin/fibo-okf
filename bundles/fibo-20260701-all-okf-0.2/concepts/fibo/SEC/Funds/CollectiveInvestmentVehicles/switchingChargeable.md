---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: switching chargeable
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether a switching charge for changing between sub-funds of the same umbrella can be applied.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingGeneralTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingGeneralTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/switchingChargeable
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: switching chargeable
type: Ontology Property
---

# switching chargeable

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/switchingChargeable>

## Definition

Whether a switching charge for changing between sub-funds of the same umbrella can be applied.

## Relationships

- **Domain**: [FundProcessingGeneralTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingGeneralTerms.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): switching chargeable
- **definition** (en): Whether a switching charge for changing between sub-funds of the same umbrella can be applied.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
