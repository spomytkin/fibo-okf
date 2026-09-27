---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has conversion factor
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the price of the delivered bond/note ($1 par value) to yield a fixed rate. The conversion factor is used
      to calculate a final delivery price.
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/BondFuture.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/BondFuture
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/hasConversionFactor
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: has conversion factor
type: Ontology Property
---

# has conversion factor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/hasConversionFactor>

## Definition

indicates the price of the delivered bond/note ($1 par value) to yield a fixed rate. The conversion factor is used to calculate a final delivery price.

## Relationships

- **Domain**: [BondFuture](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/BondFuture.md)
- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **Subproperty of**: [hasNumericValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue>)

## Annotations

- **label** (en): has conversion factor
- **definition** (en): indicates the price of the delivered bond/note ($1 par value) to yield a fixed rate. The conversion factor is used to calculate a final delivery price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
