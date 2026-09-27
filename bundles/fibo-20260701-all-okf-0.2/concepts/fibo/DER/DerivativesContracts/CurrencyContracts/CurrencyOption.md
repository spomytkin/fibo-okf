---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option giving the buyer (holder) the right, but not the obligation, to buy or sell currency at a specified exchange
      rate during a specified period of time
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FX option
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For this right, a premium is paid to the broker, which will vary depending on the number of contracts purchased.
      Currency options are one of the best ways for corporations or individuals to hedge against adverse movements in exchange
      rates. Investors can hedge against foreign currency risk by purchasing a currency option put or call. For example, assume
      that an investor believes that the USD/EUR rate is going to increase from 0.80 to 0.90 (meaning that it will become
      more expensive for a European investor to buy U.S dollars). In this case, the investor would want to buy a call option
      on USD/EUR so that he or she could stand to gain from an increase in the exchange rate (or the USD rise).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: foreign exchange option
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: forex option
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/ExchangeRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasStrikeRate
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N900ed6e687f141108481ac7aacf98769
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/VanillaOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyOption
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: currency option
type: Ontology Class
---

# currency option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyOption>

## Definition

option giving the buyer (holder) the right, but not the obligation, to buy or sell currency at a specified exchange rate during a specified period of time

## Relationships

- **Subclass of**: [CurrencyDerivative](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md)
- **Subclass of**: [VanillaOption](/concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md)

## Constraints

- **[hasStrikeRate](/concepts/fibo/DER/DerivativesContracts/Options/hasStrikeRate.md)**: some values from of type [ExchangeRate](/concepts/fibo/FND/Accounting/CurrencyAmount/ExchangeRate.md)
- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N900ed6e687f141108481ac7aacf98769`

## Annotations

- **label** (en): currency option
- **definition** (en): option giving the buyer (holder) the right, but not the obligation, to buy or sell currency at a specified exchange rate during a specified period of time
- **abbreviation** (en): FX option
- **explanatoryNote** (en): For this right, a premium is paid to the broker, which will vary depending on the number of contracts purchased. Currency options are one of the best ways for corporations or individuals to hedge against adverse movements in exchange rates. Investors can hedge against foreign currency risk by purchasing a currency option put or call. For example, assume that an investor believes that the USD/EUR rate is going to increase from 0.80 to 0.90 (meaning that it will become more expensive for a European investor to buy U.S dollars). In this case, the investor would want to buy a call option on USD/EUR so that he or she could stand to gain from an increase in the exchange rate (or the USD rise).
- **synonym** (en): foreign exchange option
- **synonym** (en): forex option

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
