---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: percentage monetary amount
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of some amount of money expressed as a percentage of some other amount, some notional amount or some concrete
      money amount
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: percentage monetary amount
type: Ontology Class
---

# percentage monetary amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount>

## Definition

measure of some amount of money expressed as a percentage of some other amount, some notional amount or some concrete money amount

## Relationships

- **Subclass of**: [Percentage](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage>)

## Constraints

- **[hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label**: percentage monetary amount
- **definition**: measure of some amount of money expressed as a percentage of some other amount, some notional amount or some concrete money amount

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
