---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ordinary dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: dividend that is paid to shareholders periodically
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Most dividends are considered ordinary, unless they are specifically designated as qualified dividends.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the terms related to ordinary dividend payment are typically specified in the context of a board resolution
      rather than contractually.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentAmount
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Dividend
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/OrdinaryDividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: ordinary dividend
type: Ontology Class
---

# ordinary dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/OrdinaryDividend>

## Definition

dividend that is paid to shareholders periodically

## Relationships

- **Subclass of**: [Dividend](/concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md)

## Constraints

- **[hasPaymentAmount](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentAmount.md)**: exact qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: ordinary dividend
- **definition**: dividend that is paid to shareholders periodically
- **explanatoryNote**: Most dividends are considered ordinary, unless they are specifically designated as qualified dividends.
- **explanatoryNote**: Note that the terms related to ordinary dividend payment are typically specified in the context of a board resolution rather than contractually.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
