---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has quotation date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the quotation date for a given market rate or indicator
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Typically this property reflects a daily average or end of day quote.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Note that this property requires a reified date value, if used.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/hasQuotationDate
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: has quotation date
type: Ontology Property
---

# has quotation date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/hasQuotationDate>

## Definition

indicates the quotation date for a given market rate or indicator

## Relationships

- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **Subproperty of**: [hasDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDate>)

## Annotations

- **label**: has quotation date
- **definition**: indicates the quotation date for a given market rate or indicator
- **explanatoryNote**: Typically this property reflects a daily average or end of day quote.
- **usageNote**: Note that this property requires a reified date value, if used.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
