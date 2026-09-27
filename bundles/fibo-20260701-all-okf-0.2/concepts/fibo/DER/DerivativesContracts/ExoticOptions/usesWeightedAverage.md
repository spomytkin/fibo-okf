---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: uses weighted average
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether a weighted average is being used to calculate the average rate or strike price
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/ExoticOptions/AsianOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AsianOption
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/usesWeightedAverage
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: uses weighted average
type: Ontology Property
---

# uses weighted average

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/usesWeightedAverage>

## Definition

indicates whether a weighted average is being used to calculate the average rate or strike price

## Relationships

- **Domain**: [AsianOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/AsianOption.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): uses weighted average
- **definition** (en): indicates whether a weighted average is being used to calculate the average rate or strike price

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
