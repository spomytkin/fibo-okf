---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: price structure
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured collection of prices, such as market prices for some index or security, such that volatility or other
      analyses may be performed over the structure
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Historical prices are needed not only for various statistical analyses but for determining best prices for certain
      kinds of options, for example. Note that prices may be quoted or calculated.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: price history
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/PriceStructure
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: price structure
type: Ontology Class
---

# price structure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/PriceStructure>

## Definition

structured collection of prices, such as market prices for some index or security, such that volatility or other analyses may be performed over the structure

## Relationships

- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)

## Annotations

- **label**: price structure
- **definition**: structured collection of prices, such as market prices for some index or security, such that volatility or other analyses may be performed over the structure
- **explanatoryNote**: Historical prices are needed not only for various statistical analyses but for determining best prices for certain kinds of options, for example. Note that prices may be quoted or calculated.
- **synonym**: price history

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
