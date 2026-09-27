---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: observable value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specification for the value for something discernible and for which evidence can be obtained
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Derivatives, such as certain exotics, can be based on values ascribed to virtually anything, including weather.
      Typically, however, an observable value refers to something that can be readily observed in the marketplace, such as
      a quoted rate (e.g., interest rate, exchange rate), index value, commodity price, stock price, economic indicator, or
      something similar as of some point in time.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2002/07/owl#Thing
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/specifiesValueOf
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasValueExpressedIn
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://en.wikipedia.org/wiki/Fair_value
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Specification
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ObservableValue
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: observable value
type: Ontology Class
---

# observable value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ObservableValue>

## Definition

specification for the value for something discernible and for which evidence can be obtained

## Relationships

- **See also**: [Fair_value](<https://en.wikipedia.org/wiki/Fair_value>)
- **Subclass of**: [Specification](<https://www.omg.org/spec/Commons/Documents/Specification>)

## Constraints

- **[specifiesValueOf](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/specifiesValueOf.md)**: some values from of type [Thing](<http://www.w3.org/2002/07/owl#Thing>)
- **[hasValueExpressedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasValueExpressedIn.md)**: min qualified cardinality 0 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label**: observable value
- **definition**: specification for the value for something discernible and for which evidence can be obtained
- **explanatoryNote**: Derivatives, such as certain exotics, can be based on values ascribed to virtually anything, including weather. Typically, however, an observable value refers to something that can be readily observed in the marketplace, such as a quoted rate (e.g., interest rate, exchange rate), index value, commodity price, stock price, economic indicator, or something similar as of some point in time.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
