---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: special dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: dividend that is paid to shareholders on a one-time basis
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Special dividends may be included in a dividend schedule as an ad-hoc entry, since they still need to be tracked
      based on the date of issuance.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Dividend
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SpecialDividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: special dividend
type: Ontology Class
---

# special dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SpecialDividend>

## Definition

dividend that is paid to shareholders on a one-time basis

## Relationships

- **Subclass of**: [Dividend](/concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md)

## Annotations

- **label**: special dividend
- **definition**: dividend that is paid to shareholders on a one-time basis
- **usageNote** (en): Special dividends may be included in a dividend schedule as an ad-hoc entry, since they still need to be tracked based on the date of issuance.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
