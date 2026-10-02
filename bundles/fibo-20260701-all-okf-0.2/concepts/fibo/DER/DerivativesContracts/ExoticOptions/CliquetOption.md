---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cliquet option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exotic option that is a series of at-the-money (ATM) options, either puts or calls, where each successive option
      becomes active when the previous one expires
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A cliquet is a cash-settled, exotic option that settles at predetermined dates and then resets its strike price
      based on the price of the underlying security at the time of settlement. Each new option within the cliquet enters into
      force when the previous option expires. The total premium and the exact reset dates are known at the time of transacting
      a cliquet. Investors can opt to receive their payout when each option expires or wait until the entire series plays
      out.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A cliquet is a series of forward start options, all related to each other. Each forward start option represents
      the advance purchase of a put, or call, option with an at-the-money (ATM) strike price to be determined at a later date,
      typically when the option becomes active. A forward start option becomes active at a specified date in the future. The
      premium is paid in advance, while the time to expiration and the underlying security are established at the time the
      forward start option is purchased. If at the first settlement date the underlying security trades below the strike price
      of the option (for a call), then it expires worthless and resets to the price of the underlying security at the time
      of settlement. If at the end of the next settlement the underlying security trades above the new strike, the holder
      may elect to receive the difference between the market price of the underlying security and the strike price. Alternatively,
      the holder can let it ride to receive the sum of all payouts at maturity. The main advantage of initiating a cliquet
      is, if an investor expects volatility to rise, they can lock in their profits at predetermined levels and thus maximize
      their overall portfolio return.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: rachet option
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ForwardStartOption
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/CliquetOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: cliquet option
type: Ontology Class
---

# cliquet option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/CliquetOption>

## Definition

exotic option that is a series of at-the-money (ATM) options, either puts or calls, where each successive option becomes active when the previous one expires

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [ForwardStartOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/ForwardStartOption.md)

## Annotations

- **label** (en): cliquet option
- **definition** (en): exotic option that is a series of at-the-money (ATM) options, either puts or calls, where each successive option becomes active when the previous one expires
- **explanatoryNote** (en): A cliquet is a cash-settled, exotic option that settles at predetermined dates and then resets its strike price based on the price of the underlying security at the time of settlement. Each new option within the cliquet enters into force when the previous option expires. The total premium and the exact reset dates are known at the time of transacting a cliquet. Investors can opt to receive their payout when each option expires or wait until the entire series plays out.
- **explanatoryNote** (en): A cliquet is a series of forward start options, all related to each other. Each forward start option represents the advance purchase of a put, or call, option with an at-the-money (ATM) strike price to be determined at a later date, typically when the option becomes active. A forward start option becomes active at a specified date in the future. The premium is paid in advance, while the time to expiration and the underlying security are established at the time the forward start option is purchased. If at the first settlement date the underlying security trades below the strike price of the option (for a call), then it expires worthless and resets to the price of the underlying security at the time of settlement. If at the end of the next settlement the underlying security trades above the new strike, the holder may elect to receive the difference between the market price of the underlying security and the strike price. Alternatively, the holder can let it ride to receive the sum of all payouts at maturity. The main advantage of initiating a cliquet is, if an investor expects volatility to rise, they can lock in their profits at predetermined levels and thus maximize their overall portfolio return.
- **synonym** (en): rachet option

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
