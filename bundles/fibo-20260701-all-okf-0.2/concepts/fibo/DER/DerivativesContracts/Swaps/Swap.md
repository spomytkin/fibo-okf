---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: derivative instrument whereby counterparties agree to exchange periodic streams of cash flows or liabilities from
      two different financial instruments with each other
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The notional amount, effective date and termination date are some of the properties that each swap leg has that
      are taken from the swap contract.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The underlying instruments can be almost anything, representing various asset classes, but most swaps involve cash
      flows (streams of payments or other commitments over time) based on a notional principal amount that both parties agree
      to.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Usually, the principal does not change hands. Each cash flow comprises one leg of the swap. One cash flow is generally
      fixed, while the other is variable, that is, based on a a benchmark interest rate, floating currency exchange rate or
      index price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exchanges
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: swap
type: Ontology Class
---

# swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap>

## Definition

derivative instrument whereby counterparties agree to exchange periodic streams of cash flows or liabilities from two different financial instruments with each other

## Relationships

- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Constraints

- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [SwapParty](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapParty.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [SwapTerms](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapTerms.md)
- **[exchanges](/concepts/fibo/FND/Relations/Relations/exchanges.md)**: some values from of type [SwapLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [UniqueSwapIdentifier](/concepts/fibo/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier.md)

## Annotations

- **label**: swap
- **definition**: derivative instrument whereby counterparties agree to exchange periodic streams of cash flows or liabilities from two different financial instruments with each other
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15
- **explanatoryNote**: The notional amount, effective date and termination date are some of the properties that each swap leg has that are taken from the swap contract.
- **explanatoryNote**: The underlying instruments can be almost anything, representing various asset classes, but most swaps involve cash flows (streams of payments or other commitments over time) based on a notional principal amount that both parties agree to.
- **explanatoryNote**: Usually, the principal does not change hands. Each cash flow comprises one leg of the swap. One cash flow is generally fixed, while the other is variable, that is, based on a a benchmark interest rate, floating currency exchange rate or index price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
