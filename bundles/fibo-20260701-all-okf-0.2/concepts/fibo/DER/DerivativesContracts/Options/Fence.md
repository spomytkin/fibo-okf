---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fence
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option trading strategy that uses options to limit the range of possible returns on a financial instrument
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'A fence consists of the following elements:

      - long position in a financial instrument (e.g., a share, index or currency)

      - long put (normally with a strike price close to or at the current spot price of the financial instrument)

      - short put (with a strike price lower than the bought put - e.g., 80% of the current spot price)

      - short call (with a strike price higher than the current spot price).'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The expiration dates of all the options are usually the same. The call strike is normally chosen in such a way
      that the sum total of the three option premiums is equal to zero. This investment strategy will ensure that the value
      of the investment at expiry will be between the strike price on the short call and the strike price on the long put.
      Thus, possible gains and losses (the value of the financial instrument minus the cost of acquiring it) are confined
      to a specified range. However, if the price of the financial instrument falls below the strike level of the sold put
      the investor will start participating in any further price declines of the financial instrument.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CallOption
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/PutOption
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionTradingStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Fence
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: fence
type: Ontology Class
---

# fence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Fence>

## Definition

option trading strategy that uses options to limit the range of possible returns on a financial instrument

## Relationships

- **Subclass of**: [OptionTradingStrategy](/concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [CallOption](/concepts/fibo/DER/DerivativesContracts/Options/CallOption.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 2 of type [PutOption](/concepts/fibo/DER/DerivativesContracts/Options/PutOption.md)

## Annotations

- **label** (en): fence
- **definition** (en): option trading strategy that uses options to limit the range of possible returns on a financial instrument
- **explanatoryNote** (en): A fence consists of the following elements: - long position in a financial instrument (e.g., a share, index or currency) - long put (normally with a strike price close to or at the current spot price of the financial instrument) - short put (with a strike price lower than the bought put - e.g., 80% of the current spot price) - short call (with a strike price higher than the current spot price).
- **explanatoryNote** (en): The expiration dates of all the options are usually the same. The call strike is normally chosen in such a way that the sum total of the three option premiums is equal to zero. This investment strategy will ensure that the value of the investment at expiry will be between the strike price on the short call and the strike price on the long put. Thus, possible gains and losses (the value of the financial instrument minus the cost of acquiring it) are confined to a specified range. However, if the price of the financial instrument falls below the strike level of the sold put the investor will start participating in any further price declines of the financial instrument.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
