---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: default rate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: qualified measure of the rate at which holders of the debt instruments in the pool default on those instruments
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Ratio
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DefaultRate
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: default rate
type: Ontology Class
---

# default rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DefaultRate>

## Definition

qualified measure of the rate at which holders of the debt instruments in the pool default on those instruments

## Relationships

- **Subclass of**: [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
- **Subclass of**: [Ratio](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Ratio>)

## Annotations

- **label** (en): default rate
- **definition** (en): qualified measure of the rate at which holders of the debt instruments in the pool default on those instruments

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
