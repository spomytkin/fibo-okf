---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: chooser option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exotic option that allows its holder (buyer) to exercise the right to buy (call) or sell (put) specified assets
      at a fixed price whereby the buyer does not have to decide whether the contract will be a put or a call until an agreed
      future date, prior to expiration
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, assume a trader wants to have an option position for the updated XYZ Inc. earnings release. They think
      the stock will have a big move, but they are not sure in which direction. The earnings release is in one month, so the
      trader decides to buy a chooser option that will expire about three weeks after the earnings release. They believe this
      should provide enough time for the stock to make a significant move if it is going to make one, and fully digest the
      earnings release. Therefore, the option they choose will expire in seven to eight weeks. The chooser option allows them
      to exercise the option as a call if the price of XYZ rises, or as a put if the price falls. At the time of the chooser
      option purchase, XYZ is trading at $28. The trader chooses an at-the-money strike price of $28 and pays a premium of
      $2 or $200 for one contract ($2 x 100 shares). The buyer can't exercise the option prior to expiry since it is a European
      option. At expiry, the trader will determine if they will exercise the option as a call or put. Assume the price of
      XYZ at the time of expiry is $31. This is higher than the strike price of $28, therefore the trader will exercise the
      option as a call. Their profit is $1 ($31 - $28 - $2) or $100. If XYZ is trading between $28 and $29.99 the trader will
      still choose to exercise the option as a call, but they will still be losing money since the profit is not enough to
      offset their $2 cost. $30 is the breakeven point on the call. If the price of BAC is below $28, the trader will exercise
      the option as a put. In this case, $26 is the breakeven point ($28 - $2). If the underlying is trading between $28 and
      $26.01 the trader will lose money since the price didn't fall enough to offset the cost of the option. If the price
      of BAC falls below $26, say to $24, the trader will make money on the put. Their profit is $2 ($28 - $24 - $2) or $200.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Commodity Futures Trading Commission (CFTC) glossary, https://www.cftc.gov/LearnAndProtect/EducationCenter/CFTCGlossary/glossary_c.html
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A chooser option is an option contract that allows the holder to decide whether it is a call or put prior to the
      expiration date. Chooser options usually have the same strike price and expiration date regardless of what decision
      the holder makes. Because the option could benefit from upside or downside movement, chooser options provide investors
      a great deal of flexibility and thus may cost more than comparable vanilla options. Chooser options are typically European
      style, and have one strike price and one expiration date regardless of whether the option is exercised as a call or
      put.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasOptionTypeElectionDate
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
    value: N31abfadb24b2449ab52d42e74b32b31a
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ChooserOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: chooser option
type: Ontology Class
---

# chooser option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ChooserOption>

## Definition

exotic option that allows its holder (buyer) to exercise the right to buy (call) or sell (put) specified assets at a fixed price whereby the buyer does not have to decide whether the contract will be a put or a call until an agreed future date, prior to expiration

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[hasOptionTypeElectionDate](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasOptionTypeElectionDate.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from value `N31abfadb24b2449ab52d42e74b32b31a`

## Annotations

- **label** (en): chooser option
- **definition** (en): exotic option that allows its holder (buyer) to exercise the right to buy (call) or sell (put) specified assets at a fixed price whereby the buyer does not have to decide whether the contract will be a put or a call until an agreed future date, prior to expiration
- **example** (en): For example, assume a trader wants to have an option position for the updated XYZ Inc. earnings release. They think the stock will have a big move, but they are not sure in which direction. The earnings release is in one month, so the trader decides to buy a chooser option that will expire about three weeks after the earnings release. They believe this should provide enough time for the stock to make a significant move if it is going to make one, and fully digest the earnings release. Therefore, the option they choose will expire in seven to eight weeks. The chooser option allows them to exercise the option as a call if the price of XYZ rises, or as a put if the price falls. At the time of the chooser option purchase, XYZ is trading at $28. The trader chooses an at-the-money strike price of $28 and pays a premium of $2 or $200 for one contract ($2 x 100 shares). The buyer can't exercise the option prior to expiry since it is a European option. At expiry, the trader will determine if they will exercise the option as a call or put. Assume the price of XYZ at the time of expiry is $31. This is higher than the strike price of $28, therefore the trader will exercise the option as a call. Their profit is $1 ($31 - $28 - $2) or $100. If XYZ is trading between $28 and $29.99 the trader will still choose to exercise the option as a call, but they will still be losing money since the profit is not enough to offset their $2 cost. $30 is the breakeven point on the call. If the price of BAC is below $28, the trader will exercise the option as a put. In this case, $26 is the breakeven point ($28 - $2). If the underlying is trading between $28 and $26.01 the trader will lose money since the price didn't fall enough to offset the cost of the option. If the price of BAC falls below $26, say to $24, the trader will make money on the put. Their profit is $2 ($28 - $24 - $2) or $200.
- **adaptedFrom** (en): Commodity Futures Trading Commission (CFTC) glossary, https://www.cftc.gov/LearnAndProtect/EducationCenter/CFTCGlossary/glossary_c.html
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.
- **explanatoryNote** (en): A chooser option is an option contract that allows the holder to decide whether it is a call or put prior to the expiration date. Chooser options usually have the same strike price and expiration date regardless of what decision the holder makes. Because the option could benefit from upside or downside movement, chooser options provide investors a great deal of flexibility and thus may cost more than comparable vanilla options. Chooser options are typically European style, and have one strike price and one expiration date regardless of whether the option is exercised as a call or put.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
