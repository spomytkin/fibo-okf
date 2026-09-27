---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: valuation frequency textual description
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Description of the frequency of the net asset value calculation.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/NetAssetValueCalculationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/NetAssetValueCalculationMethod
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/valuationFrequencyTextualDescription
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: valuation frequency textual description
type: Ontology Property
---

# valuation frequency textual description

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/valuationFrequencyTextualDescription>

## Definition

Description of the frequency of the net asset value calculation.

## Relationships

- **Domain**: [NetAssetValueCalculationMethod](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/NetAssetValueCalculationMethod.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): valuation frequency textual description
- **definition** (en): Description of the frequency of the net asset value calculation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
