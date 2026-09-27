---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unit price
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: monetary price expressed in relation to a well-known measurable unit by which the goods or services are allocated
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, gold is commonly measured in troy ounces, grams, etc., and oil is measured in terms of barrels.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2002/07/owl#Thing
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/isPriceFor
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/UnitPrice
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: unit price
type: Ontology Class
---

# unit price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/UnitPrice>

## Definition

monetary price expressed in relation to a well-known measurable unit by which the goods or services are allocated

## Relationships

- **Subclass of**: [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)

## Constraints

- **[isPriceFor](/concepts/fibo/FND/Accounting/CurrencyAmount/isPriceFor.md)**: some values from of type [Thing](<http://www.w3.org/2002/07/owl#Thing>)

## Annotations

- **label**: unit price
- **definition**: monetary price expressed in relation to a well-known measurable unit by which the goods or services are allocated
- **example**: For example, gold is commonly measured in troy ounces, grams, etc., and oil is measured in terms of barrels.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
