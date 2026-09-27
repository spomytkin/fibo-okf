---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trading status message
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A message about trading status.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'There are a number of such messages. Events v Status: See e.g. Active: this relates to one state OR two transitions
      (transition from pre-issuance to Trading, or from Suspended to Trading).'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/SecurityTradingStatus
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/isAbout
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Notice
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/TradingStatusMessage
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: trading status message
type: Ontology Class
---

# trading status message

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/TradingStatusMessage>

## Definition

A message about trading status.

## Relationships

- **Subclass of**: [Notice](<https://www.omg.org/spec/Commons/Documents/Notice>)

## Constraints

- **[isAbout](<https://www.omg.org/spec/Commons/Documents/isAbout>)**: some values from of type [SecurityTradingStatus](/concepts/fibo/MD/TemporalCore/SecurityTradingStatuses/SecurityTradingStatus.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label** (en): trading status message
- **definition** (en): A message about trading status.
- **explanatoryNote** (en): There are a number of such messages. Events v Status: See e.g. Active: this relates to one state OR two transitions (transition from pre-issuance to Trading, or from Suspended to Trading).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
