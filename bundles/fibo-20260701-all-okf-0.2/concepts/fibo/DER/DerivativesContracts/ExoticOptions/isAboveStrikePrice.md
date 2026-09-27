---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is above strike price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the barrier is crossed when the price of the underlier is above (or below, if not) the strike
      price (threshold)
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/BarrierOption
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/isAboveStrikePrice
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: is above strike price
type: Ontology Property
---

# is above strike price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/isAboveStrikePrice>

## Definition

indicates whether the barrier is crossed when the price of the underlier is above (or below, if not) the strike price (threshold)

## Relationships

- **Domain**: [BarrierOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is above strike price
- **definition** (en): indicates whether the barrier is crossed when the price of the underlier is above (or below, if not) the strike price (threshold)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
