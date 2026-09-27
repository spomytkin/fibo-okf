---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: settlement convention
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: convention employed to determine the closing date (from the stated settlement date) in the process of settling
      a transaction on which securities or interests in securities are delivered, usually against (in simultaneous exchange
      for) payment of some consideration
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is often stated in the form 'T+n' where n is the number of business days from the specified settlement date
      (T).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#positiveInteger
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/Convention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/Convention
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/SettlementConvention
sources:
- id: fibo-source-89377f435c
  resource: references/fibo/FBC/FinancialInstruments/Settlement.rdf
  sha256: 89377f435ce3f9d5ae76a4c2bf85b0591df9c10d237d0a2ca9700d9da0c4da5c
  title: FIBO source FBC/FinancialInstruments/Settlement.rdf
title: settlement convention
type: Ontology Class
---

# settlement convention

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/SettlementConvention>

## Definition

convention employed to determine the closing date (from the stated settlement date) in the process of settling a transaction on which securities or interests in securities are delivered, usually against (in simultaneous exchange for) payment of some consideration

## Relationships

- **Subclass of**: [Convention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/Convention.md)

## Constraints

- **[hasNumericValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue>)**: some values from of type [positiveInteger](<http://www.w3.org/2001/XMLSchema#positiveInteger>)

## Annotations

- **label**: settlement convention
- **definition**: convention employed to determine the closing date (from the stated settlement date) in the process of settling a transaction on which securities or interests in securities are delivered, usually against (in simultaneous exchange for) payment of some consideration
- **explanatoryNote**: This is often stated in the form 'T+n' where n is the number of business days from the specified settlement date (T).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
