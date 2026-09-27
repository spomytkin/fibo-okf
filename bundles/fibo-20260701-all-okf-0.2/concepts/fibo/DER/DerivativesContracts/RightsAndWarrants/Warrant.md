---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entitlement that permits the holder to purchase a specified amount of a financial instrument, commodity, currency
      or other asset during a specified period at a specified price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Warrants are for any kind of instrument. Warrants may be privately issued and may not necessarily be traded on
      an exchange.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/ExerciseTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/hasExerciseTerms
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Entitlement
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: warrant
type: Ontology Class
---

# warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant>

## Definition

entitlement that permits the holder to purchase a specified amount of a financial instrument, commodity, currency or other asset during a specified period at a specified price

## Relationships

- **Subclass of**: [Entitlement](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md)

## Constraints

- **[hasExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/hasExerciseTerms.md)**: some values from of type [ExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseTerms.md)

## Annotations

- **label** (en): warrant
- **definition** (en): entitlement that permits the holder to purchase a specified amount of a financial instrument, commodity, currency or other asset during a specified period at a specified price
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): Warrants are for any kind of instrument. Warrants may be privately issued and may not necessarily be traded on an exchange.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
