---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underlier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: something that can be assigned a value in the marketplace that forms the basis for a derivative or pool-backed
      instrument
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Underlier means any rate (including interest and foreign exchange rates), currency, commodity, security, instrument
      of indebtedness, index, quantitative measure, occurrence or non-occurrence of an event, or other financial or economic
      interest, or property of any kind, or any interest therein or based on the value thereof, in or by reference to which
      any payment or delivery under a transaction is to be made or determined.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nd0bbbe9c37b5466bb128b76b530c1eb4
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Undergoer
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Underlier
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: underlier
type: Ontology Class
---

# underlier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Underlier>

## Definition

something that can be assigned a value in the marketplace that forms the basis for a derivative or pool-backed instrument

## Relationships

- **Subclass of**: [Undergoer](<https://www.omg.org/spec/Commons/PartiesAndSituations/Undergoer>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nd0bbbe9c37b5466bb128b76b530c1eb4`

## Annotations

- **label**: underlier
- **definition**: something that can be assigned a value in the marketplace that forms the basis for a derivative or pool-backed instrument
- **explanatoryNote**: Underlier means any rate (including interest and foreign exchange rates), currency, commodity, security, instrument of indebtedness, index, quantitative measure, occurrence or non-occurrence of an event, or other financial or economic interest, or property of any kind, or any interest therein or based on the value thereof, in or by reference to which any payment or delivery under a transaction is to be made or determined.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
