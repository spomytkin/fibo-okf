---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: option
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: derivative instrument that grants to the holder either the privilege to purchase or the privilege to sell the assets
      specified at a predetermined price or formula at or within a time period in the future
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth
      edition, 2019-10.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionPremium
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasCalculatedMarketValue
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StrikePrice
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasExercisePrice
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasExerciseSchedule
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/ExerciseConvention
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasExerciseStyle
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionHolder
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasOptionHolder
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionIssuer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasOptionWriter
  - filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasLotSize
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasExpirationDate
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: option
type: Ontology Class
---

# option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option>

## Definition

derivative instrument that grants to the holder either the privilege to purchase or the privilege to sell the assets specified at a predetermined price or formula at or within a time period in the future

## Relationships

- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Constraints

- **[hasCalculatedMarketValue](/concepts/fibo/DER/DerivativesContracts/Options/hasCalculatedMarketValue.md)**: min qualified cardinality 0 of type [OptionPremium](/concepts/fibo/DER/DerivativesContracts/Options/OptionPremium.md)
- **[hasExercisePrice](/concepts/fibo/DER/DerivativesContracts/Options/hasExercisePrice.md)**: some values from of type [StrikePrice](/concepts/fibo/DER/DerivativesContracts/Options/StrikePrice.md)
- **[hasExerciseSchedule](/concepts/fibo/DER/DerivativesContracts/Options/hasExerciseSchedule.md)**: some values from of type [Schedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md)
- **[hasExerciseStyle](/concepts/fibo/DER/DerivativesContracts/Options/hasExerciseStyle.md)**: some values from of type [ExerciseConvention](/concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseConvention.md)
- **[hasOptionHolder](/concepts/fibo/DER/DerivativesContracts/Options/hasOptionHolder.md)**: min qualified cardinality 0 of type [OptionHolder](/concepts/fibo/DER/DerivativesContracts/Options/OptionHolder.md)
- **[hasOptionWriter](/concepts/fibo/DER/DerivativesContracts/Options/hasOptionWriter.md)**: some values from of type [OptionIssuer](/concepts/fibo/DER/DerivativesContracts/Options/OptionIssuer.md)
- **[hasLotSize](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasLotSize.md)**: some values from of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[hasExpirationDate](/concepts/fibo/FND/Arrangements/Documents/hasExpirationDate.md)**: some values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label**: option
- **definition**: derivative instrument that grants to the holder either the privilege to purchase or the privilege to sell the assets specified at a predetermined price or formula at or within a time period in the future
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth edition, 2019-10.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
