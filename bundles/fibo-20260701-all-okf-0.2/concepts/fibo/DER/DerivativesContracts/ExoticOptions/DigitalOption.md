---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: digital option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exotic option that has a pre-determined payout if the option is in-the-money and the payoff condition is satisfied
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, let's say the ABC Index is trading at a level of 2,795 on June 2. An investor believes the ABC Index
      will trade above 2,800 before the end of the trading day, June 4th. The trader purchases 10 ABC Index options at a strike
      price of 2,800 options for $40 per contract. If the ABC Index closes above 2,800 at the end of the trading day on June
      4, the investor is paid $100 per contract, which is a profit of $60 per contract or $600 (($100 - $40) x 10 contracts).
      However, if the ABC Index closes below 2,800 on June 4. The investor loses all of the premium amount or $400 ($40 x
      10 contracts).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There is an upfront fee called the premium for digital options, which is the maximum loss for the option. Unlike
      traditional options, digital options don't convert or exercise to the underlying asset's shares. Instead, they pay out
      a fixed reward if the asset's price is above or below the option's strike price.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: binary option
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/BarrierOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/DigitalOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: digital option
type: Ontology Class
---

# digital option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/DigitalOption>

## Definition

exotic option that has a pre-determined payout if the option is in-the-money and the payoff condition is satisfied

## Relationships

- **Subclass of**: [BarrierOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)

## Annotations

- **label** (en): digital option
- **definition** (en): exotic option that has a pre-determined payout if the option is in-the-money and the payoff condition is satisfied
- **example** (en): For example, let's say the ABC Index is trading at a level of 2,795 on June 2. An investor believes the ABC Index will trade above 2,800 before the end of the trading day, June 4th. The trader purchases 10 ABC Index options at a strike price of 2,800 options for $40 per contract. If the ABC Index closes above 2,800 at the end of the trading day on June 4, the investor is paid $100 per contract, which is a profit of $60 per contract or $600 (($100 - $40) x 10 contracts). However, if the ABC Index closes below 2,800 on June 4. The investor loses all of the premium amount or $400 ($40 x 10 contracts).
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.
- **explanatoryNote** (en): There is an upfront fee called the premium for digital options, which is the maximum loss for the option. Unlike traditional options, digital options don't convert or exercise to the underlying asset's shares. Instead, they pay out a fixed reward if the asset's price is above or below the option's strike price.
- **synonym** (en): binary option

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
