---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: compound option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exotic option for which the underlying asset is another option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, assume an investor wants to buy a put to sell 100 shares of stock at $50. The stock is currently trading
      at $55. The investor could buy a Call-Put, which allows them to buy a call now, for say $1 per share ($100), which will
      allow them to buy a put with a $50 strike in the future. They pay the $1 per share now, but only need to pay the fee
      for the second option if they exercise the first resulting in them receiving the second option.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Therefore, there are two strike prices and two exercise dates. They are available for any combination of calls
      and puts. For example, a put where the underlying is a call option or a call where the underlying is a put option. The
      underlying is the second option, while the initial option is called the overlying. If the compound option is exercised,
      there are two premiums.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: split-fee options
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/CompoundOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: compound option
type: Ontology Class
---

# compound option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/CompoundOption>

## Definition

exotic option for which the underlying asset is another option

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)

## Annotations

- **label** (en): compound option
- **definition** (en): exotic option for which the underlying asset is another option
- **example** (en): For example, assume an investor wants to buy a put to sell 100 shares of stock at $50. The stock is currently trading at $55. The investor could buy a Call-Put, which allows them to buy a call now, for say $1 per share ($100), which will allow them to buy a put with a $50 strike in the future. They pay the $1 per share now, but only need to pay the fee for the second option if they exercise the first resulting in them receiving the second option.
- **explanatoryNote** (en): Therefore, there are two strike prices and two exercise dates. They are available for any combination of calls and puts. For example, a put where the underlying is a call option or a call where the underlying is a put option. The underlying is the second option, while the initial option is called the overlying. If the compound option is exercised, there are two premiums.
- **synonym** (en): split-fee options

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
