---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is MiFID reporting required
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether reporting on the security is required by the Markets in Financial Instruments Directive (MiFID)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This indicator specifies whether the security is eligible for trade reporting within the Markets in Financial Instruments
      Directive (MiFID) zone.
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/isMiFIDReportingRequired
sources:
- id: fibo-source-d2c4e0b02d
  resource: references/fibo/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions.rdf
  sha256: d2c4e0b02d30114692ca293e6f51e26b36eef9f530171ac73c4831c6e7869087
  title: FIBO source SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions.rdf
title: is MiFID reporting required
type: Ontology Property
---

# is MiFID reporting required

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/isMiFIDReportingRequired>

## Definition

indicates whether reporting on the security is required by the Markets in Financial Instruments Directive (MiFID)

## Relationships

- **Domain**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is MiFID reporting required
- **definition**: indicates whether reporting on the security is required by the Markets in Financial Instruments Directive (MiFID)
- **explanatoryNote**: This indicator specifies whether the security is eligible for trade reporting within the Markets in Financial Instruments Directive (MiFID) zone.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
