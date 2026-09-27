---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: conversion action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action involving conversion of securities (generally convertible bonds or preferred shares) into another
      form of securities (usually common shares) at a pre-stated price/ratio
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/convertsFrom
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/convertsTo
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/ConversionAction
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: conversion action
type: Ontology Class
---

# conversion action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/ConversionAction>

## Definition

corporate action involving conversion of securities (generally convertible bonds or preferred shares) into another form of securities (usually common shares) at a pre-stated price/ratio

## Relationships

- **Subclass of**: [VoluntaryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md)

## Constraints

- **[convertsFrom](/concepts/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions/convertsFrom.md)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **[convertsTo](/concepts/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions/convertsTo.md)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label** (en): conversion action
- **definition** (en): corporate action involving conversion of securities (generally convertible bonds or preferred shares) into another form of securities (usually common shares) at a pre-stated price/ratio

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
