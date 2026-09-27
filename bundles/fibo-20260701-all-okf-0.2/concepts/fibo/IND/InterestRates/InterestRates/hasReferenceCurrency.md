---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has reference currency
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something to the currency it is based on
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency
sources:
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: has reference currency
type: Ontology Property
---

# has reference currency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency>

## Definition

relates something to the currency it is based on

## Relationships

- **Range**: [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **Subproperty of**: [hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)

## Annotations

- **label**: has reference currency
- **definition**: relates something to the currency it is based on

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
