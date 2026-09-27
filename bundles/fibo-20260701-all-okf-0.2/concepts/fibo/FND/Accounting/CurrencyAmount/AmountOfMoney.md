---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: amount of money
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: amount of readily available cash in banknotes and coins
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: This is an actual sum of money, not the measure of a sum of money in monetary units, although it has the same basic
      properties (decimal number with a currenct unit).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: cash
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/AmountOfMoney
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: amount of money
type: Ontology Class
---

# amount of money

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/AmountOfMoney>

## Definition

amount of readily available cash in banknotes and coins

## Relationships

- **Subclass of**: [ScalarQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue>)

## Constraints

- **[hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label**: amount of money
- **definition**: amount of readily available cash in banknotes and coins
- **editorialNote**: This is an actual sum of money, not the measure of a sum of money in monetary units, although it has the same basic properties (decimal number with a currenct unit).
- **synonym**: cash

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
