---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exchange rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rate at which one currency can be exchanged for another
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: The exchange rate between the U.S. dollar and British pound is distinct from the exchange rate between the U.S.
      dollar and the euro.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasBaseCurrency
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasDealtCurrency
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasRateValue
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Ratio
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/ExchangeRate
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: exchange rate
type: Ontology Class
---

# exchange rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/ExchangeRate>

## Definition

rate at which one currency can be exchanged for another

## Relationships

- **Subclass of**: [Ratio](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Ratio>)

## Constraints

- **[hasBaseCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasBaseCurrency.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasDealtCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasDealtCurrency.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasRateValue](/concepts/fibo/FND/Accounting/CurrencyAmount/hasRateValue.md)**: exact qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: exchange rate
- **definition**: rate at which one currency can be exchanged for another
- **example**: The exchange rate between the U.S. dollar and British pound is distinct from the exchange rate between the U.S. dollar and the euro.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
