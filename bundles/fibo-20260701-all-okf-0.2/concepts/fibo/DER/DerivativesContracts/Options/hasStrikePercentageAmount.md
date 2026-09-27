---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has strike percentage amount
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a strike price or level expressed as a percentage of the value of the underlying asset
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasStrikePercentageAmount
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: has strike percentage amount
type: Ontology Property
---

# has strike percentage amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasStrikePercentageAmount>

## Definition

indicates a strike price or level expressed as a percentage of the value of the underlying asset

## Relationships

- **Range**: [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
- **Subproperty of**: [hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)

## Annotations

- **label** (en): has strike percentage amount
- **definition** (en): indicates a strike price or level expressed as a percentage of the value of the underlying asset

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
