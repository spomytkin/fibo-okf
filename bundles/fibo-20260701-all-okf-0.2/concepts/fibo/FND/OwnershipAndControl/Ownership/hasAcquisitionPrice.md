---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has acquisition price
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: has a value as of the date of acquisition, expressed as an amount of money, other financial assets, or goods
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Price.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Price
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasAcquisitionPrice
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: has acquisition price
type: Ontology Property
---

# has acquisition price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasAcquisitionPrice>

## Definition

has a value as of the date of acquisition, expressed as an amount of money, other financial assets, or goods

## Relationships

- **Range**: [Price](/concepts/fibo/FND/Accounting/CurrencyAmount/Price.md)
- **Subproperty of**: [hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)

## Annotations

- **label**: has acquisition price
- **definition**: has a value as of the date of acquisition, expressed as an amount of money, other financial assets, or goods

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
