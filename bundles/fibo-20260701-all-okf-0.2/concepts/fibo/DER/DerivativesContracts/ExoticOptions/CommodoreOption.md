---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodore option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exotic option consisting of a number of digital barrier options that pay a coupon if a pre-determined level of
      the underlying or basket of underlyings is reached
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: A three-year commodore option with annual barriers would have three potential payoffs. The first would pay at the
      end of the first year and would be dependent on the pre-determined barrier being reached or exceeded. For example, if
      the underlying or basket of underlyings reached or exceeded 102% of its initial level at the end of year one, a coupon
      of 6% would be paid. At the end of year two, if the underlying reached or exceeded 104% of its initial level, another
      6% coupon would be paid. The coupon in the final year would be 6% if the underlying reached or exceeded 106%. The coupon
      should exceed the performance level of the underlying, otherwise the investor would achieve the same result by investing
      directly in the underlying.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Sometimes the digital barrier increases with the number of years since the trade began. All of the options are
      active from the start of the trade.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/DigitalOption
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/CommodoreOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: commodore option
type: Ontology Class
---

# commodore option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/CommodoreOption>

## Definition

exotic option consisting of a number of digital barrier options that pay a coupon if a pre-determined level of the underlying or basket of underlyings is reached

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [DigitalOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/DigitalOption.md)

## Annotations

- **label** (en): commodore option
- **definition** (en): exotic option consisting of a number of digital barrier options that pay a coupon if a pre-determined level of the underlying or basket of underlyings is reached
- **example** (en): A three-year commodore option with annual barriers would have three potential payoffs. The first would pay at the end of the first year and would be dependent on the pre-determined barrier being reached or exceeded. For example, if the underlying or basket of underlyings reached or exceeded 102% of its initial level at the end of year one, a coupon of 6% would be paid. At the end of year two, if the underlying reached or exceeded 104% of its initial level, another 6% coupon would be paid. The coupon in the final year would be 6% if the underlying reached or exceeded 106%. The coupon should exceed the performance level of the underlying, otherwise the investor would achieve the same result by investing directly in the underlying.
- **explanatoryNote** (en): Sometimes the digital barrier increases with the number of years since the trade began. All of the options are active from the start of the trade.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
