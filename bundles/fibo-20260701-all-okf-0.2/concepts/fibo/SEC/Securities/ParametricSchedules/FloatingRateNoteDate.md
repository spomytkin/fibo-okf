---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: floating-rate note date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: calculated date associated with a floating-rate note, also known as a floater or FRN, which is a debt instrument
      with a variable interest rate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FRN date
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/FloatingRateNoteDateRule
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculatedDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/FloatingRateNoteDate
sources:
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: floating-rate note date
type: Ontology Class
---

# floating-rate note date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/FloatingRateNoteDate>

## Definition

calculated date associated with a floating-rate note, also known as a floater or FRN, which is a debt instrument with a variable interest rate

## Relationships

- **Subclass of**: [CalculatedDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md)

## Constraints

- **[hasBusinessDayConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention.md)**: exact qualified cardinality 1 of type [FloatingRateNoteDateRule](/concepts/fibo/SEC/Securities/ParametricSchedules/FloatingRateNoteDateRule.md)

## Annotations

- **label**: floating-rate note date
- **definition**: calculated date associated with a floating-rate note, also known as a floater or FRN, which is a debt instrument with a variable interest rate
- **abbreviation**: FRN date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
