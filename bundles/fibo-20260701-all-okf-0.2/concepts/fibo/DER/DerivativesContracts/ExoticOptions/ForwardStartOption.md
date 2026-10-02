---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: forward start option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exotic option that is fully specified with respect to a set expiry date, underlying asset and other parameters,
      purchased and paid for on initiation, but that becomes active at a set activation date with a strike price determined
      at the time of activation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, assume that two parties agree to enter into a call forward start option on XYZ stock. It is September
      and they agree that the forward start option will activate on January 1 at the money. That means on January 1 the strike
      price for the option will be the price that stock is trading at on that day. The option will expire in June. The exact
      strike price is unknown, but the parties do know the strike and underlying's price will be the same at activation. They
      can look at current six-month options (January to June) and assess volatility to determine a premium for the option.
      They agree to trade one contract, equivalent to 100 shares of the underlying stock. They decide on a premium of $40,
      or $4,000 for the contract ($40 x 100 shares). The call buyer agrees to pay the $4,000 now (September), even though
      the option doesn't activate till January. On January 1, assume the stock price is $400. The strike is set at $400, and
      an option is now a vanilla option with a June expiry. At the June expiry, assume XYZ is trading at $420. In this case,
      the option is worth $20 ($420 - $400 strike). If they settle in cash, the buyer receives $2,000, or if they exercise,
      they receive 100 shares at $400 and can keep them, or sell them at $420 to make $2,000. Notice that this still results
      in a loss for the buyer, since they paid $4,000 but are only receiving back $2,000. To make money on the call, the price
      of the underlying needs to move above the strike price plus the premium. Therefore, if the price moves up to $450 by
      expiration, the option is worth $50 ($450 - $400 strike), and the buyer receives $5,000. That's a net profit of $1,000
      over their $4,000 cost. If the underlying is trading below the $400 strike at expiry, the call option expires worthless
      and the buyer's premium is lost ($4,000 profit to the seller).
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, the people buying/selling the option could specify that the strike will be at the money (ATM) at activation,
      or 3% or 5% in the money or out of the money (OTM). Since it is a customized contract, they can negotiate any terms
      they want.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Forward start options typically attempt to keep future strike prices at the money or near the money. In this way,
      the holder will have the right, but not the obligation, to buy (call) or sell (put) the underlying asset in the future
      at or near the then-current market price. Knowing where the strike price will be in relation to the underlying's price
      makes it easier to come up with the premium (cost) of the option, which is also typically determined and paid at the
      initiation of the contract prior to the activation date. If, at the expiration date, the underlying trades below the
      strike price of the option (for a call), then it expires worthless. If the underlying is above the strike (for a call),
      then the holder exercises it and owns the underlying at the strike price. For a put option, if the underlying is below
      the strike price, the option has value and will be sold or exercised to realize a gain. If the underlying is above the
      strike price, the option will expire worthless. Typically, as with most options, the holder may sell the option if it
      is in the money and take the cash instead of exercising the option. Since it is an exotic option, the seller and buyer
      of the option may also agree to settle the option with cash instead of delivering the underlying. Once a forward start
      option becomes active (strike price is set), then the option is valued like a vanilla option.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The only unknown for the contract is the strike price. In terms of pricing the contract, the future price of the
      underlying asset is also unknown. The contract typically stipulates some parameters for where the strike price will
      be in relation to the underlying asset's price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
    value: Ne6ece89be48448929214158cad526bdf
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ForwardStartOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: forward start option
type: Ontology Class
---

# forward start option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ForwardStartOption>

## Definition

exotic option that is fully specified with respect to a set expiry date, underlying asset and other parameters, purchased and paid for on initiation, but that becomes active at a set activation date with a strike price determined at the time of activation

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from value `Ne6ece89be48448929214158cad526bdf`

## Annotations

- **label** (en): forward start option
- **definition** (en): exotic option that is fully specified with respect to a set expiry date, underlying asset and other parameters, purchased and paid for on initiation, but that becomes active at a set activation date with a strike price determined at the time of activation
- **example** (en): For example, assume that two parties agree to enter into a call forward start option on XYZ stock. It is September and they agree that the forward start option will activate on January 1 at the money. That means on January 1 the strike price for the option will be the price that stock is trading at on that day. The option will expire in June. The exact strike price is unknown, but the parties do know the strike and underlying's price will be the same at activation. They can look at current six-month options (January to June) and assess volatility to determine a premium for the option. They agree to trade one contract, equivalent to 100 shares of the underlying stock. They decide on a premium of $40, or $4,000 for the contract ($40 x 100 shares). The call buyer agrees to pay the $4,000 now (September), even though the option doesn't activate till January. On January 1, assume the stock price is $400. The strike is set at $400, and an option is now a vanilla option with a June expiry. At the June expiry, assume XYZ is trading at $420. In this case, the option is worth $20 ($420 - $400 strike). If they settle in cash, the buyer receives $2,000, or if they exercise, they receive 100 shares at $400 and can keep them, or sell them at $420 to make $2,000. Notice that this still results in a loss for the buyer, since they paid $4,000 but are only receiving back $2,000. To make money on the call, the price of the underlying needs to move above the strike price plus the premium. Therefore, if the price moves up to $450 by expiration, the option is worth $50 ($450 - $400 strike), and the buyer receives $5,000. That's a net profit of $1,000 over their $4,000 cost. If the underlying is trading below the $400 strike at expiry, the call option expires worthless and the buyer's premium is lost ($4,000 profit to the seller).
- **example** (en): For example, the people buying/selling the option could specify that the strike will be at the money (ATM) at activation, or 3% or 5% in the money or out of the money (OTM). Since it is a customized contract, they can negotiate any terms they want.
- **explanatoryNote** (en): Forward start options typically attempt to keep future strike prices at the money or near the money. In this way, the holder will have the right, but not the obligation, to buy (call) or sell (put) the underlying asset in the future at or near the then-current market price. Knowing where the strike price will be in relation to the underlying's price makes it easier to come up with the premium (cost) of the option, which is also typically determined and paid at the initiation of the contract prior to the activation date. If, at the expiration date, the underlying trades below the strike price of the option (for a call), then it expires worthless. If the underlying is above the strike (for a call), then the holder exercises it and owns the underlying at the strike price. For a put option, if the underlying is below the strike price, the option has value and will be sold or exercised to realize a gain. If the underlying is above the strike price, the option will expire worthless. Typically, as with most options, the holder may sell the option if it is in the money and take the cash instead of exercising the option. Since it is an exotic option, the seller and buyer of the option may also agree to settle the option with cash instead of delivering the underlying. Once a forward start option becomes active (strike price is set), then the option is valued like a vanilla option.
- **explanatoryNote** (en): The only unknown for the contract is the strike price. In terms of pricing the contract, the future price of the underlying asset is also unknown. The contract typically stipulates some parameters for where the strike price will be in relation to the underlying asset's price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
