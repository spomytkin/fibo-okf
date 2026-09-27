---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has price
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the value of something expressed as an amount of money or goods
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Price.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Price
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: has price
type: Ontology Property
---

# has price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice>

## Definition

indicates the value of something expressed as an amount of money or goods

## Relationships

- **Range**: [Price](/concepts/fibo/FND/Accounting/CurrencyAmount/Price.md)
- **Subproperty of**: [hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)

## Annotations

- **label**: has price
- **definition**: indicates the value of something expressed as an amount of money or goods

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
