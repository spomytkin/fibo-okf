---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: term structure
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured collection of rates, such as interest rates, or bond yields with different terms to maturity, such that
      a yield curve may be constructed for the structure
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Term structure refers to a set of discrete points; elements are ordered by time. Restrictions on the rate (see
      above) and a point in time, paired together, and then ordered in a structured collection is how this should ultimately
      be modeled. Then the concept of yield curve would be a child of term structure, for calculation of net present value,
      for example. Term structures consist of two or more observed or projected values, typically related to debt instruments
      or interest rates. assessment of monetary policy conditions, and so forth.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/TermStructure
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: term structure
type: Ontology Class
---

# term structure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/TermStructure>

## Definition

structured collection of rates, such as interest rates, or bond yields with different terms to maturity, such that a yield curve may be constructed for the structure

## Relationships

- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [MarketRate](/concepts/fibo/IND/Indicators/Indicators/MarketRate.md)

## Annotations

- **label**: term structure
- **definition**: structured collection of rates, such as interest rates, or bond yields with different terms to maturity, such that a yield curve may be constructed for the structure
- **explanatoryNote**: Term structure refers to a set of discrete points; elements are ordered by time. Restrictions on the rate (see above) and a point in time, paired together, and then ordered in a structured collection is how this should ultimately be modeled. Then the concept of yield curve would be a child of term structure, for calculation of net present value, for example. Term structures consist of two or more observed or projected values, typically related to debt instruments or interest rates. assessment of monetary policy conditions, and so forth.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
