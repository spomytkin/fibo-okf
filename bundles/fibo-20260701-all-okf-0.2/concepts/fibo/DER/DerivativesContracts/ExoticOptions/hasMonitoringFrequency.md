---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has monitoring frequency
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: has frequency with respect to how often, in days, the asset price is checked to see if the barrier has been breached
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/BarrierOption
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#positiveInteger
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasMonitoringFrequency
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: has monitoring frequency
type: Ontology Property
---

# has monitoring frequency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasMonitoringFrequency>

## Definition

has frequency with respect to how often, in days, the asset price is checked to see if the barrier has been breached

## Relationships

- **Domain**: [BarrierOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)
- **Range**: [positiveInteger](<http://www.w3.org/2001/XMLSchema#positiveInteger>)

## Annotations

- **label** (en): has monitoring frequency
- **definition** (en): has frequency with respect to how often, in days, the asset price is checked to see if the barrier has been breached

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
