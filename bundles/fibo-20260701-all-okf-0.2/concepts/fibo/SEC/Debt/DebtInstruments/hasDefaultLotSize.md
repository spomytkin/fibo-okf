---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has default lot size
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the default number of units of the security that may be held at any one time
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is the minimum denomination required for transfer or change of ownership of a tradable debt security.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasLotSize.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasLotSize
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasDefaultLotSize
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: has default lot size
type: Ontology Property
---

# has default lot size

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasDefaultLotSize>

## Definition

indicates the default number of units of the security that may be held at any one time

## Relationships

- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **Subproperty of**: [hasLotSize](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasLotSize.md)

## Annotations

- **label**: has default lot size
- **definition**: indicates the default number of units of the security that may be held at any one time
- **explanatoryNote**: This is the minimum denomination required for transfer or change of ownership of a tradable debt security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
