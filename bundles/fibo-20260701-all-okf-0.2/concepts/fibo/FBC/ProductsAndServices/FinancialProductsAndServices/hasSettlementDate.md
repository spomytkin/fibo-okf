---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has settlement date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date by which an executed order or transaction must be settled
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Settlement might involve either a buyer paying in cash or a seller delivering the relevant instrument(s) and receiving
      the proceeds as specified by the terms of a given transaction.
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculatedDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasSettlementDate
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: has settlement date
type: Ontology Property
---

# has settlement date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasSettlementDate>

## Definition

indicates the date by which an executed order or transaction must be settled

## Relationships

- **Range**: [CalculatedDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md)
- **Subproperty of**: [hasEndDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate>)

## Annotations

- **label**: has settlement date
- **definition**: indicates the date by which an executed order or transaction must be settled
- **explanatoryNote**: Settlement might involve either a buyer paying in cash or a seller delivering the relevant instrument(s) and receiving the proceeds as specified by the terms of a given transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
