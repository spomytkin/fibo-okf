---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: swap leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms defining and the commitment to fulfill cashflow requirements (e.g., interest payments, coupon payments, etc.)
      for a component of a swap
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A one-leg financing swap (also known as a single-leg financing swap) is a type of financial derivative, typically
      used by institutional investors or corporations, in which one party makes a series of fixed or floating payments to
      another party in exchange for a single upfront cash payment or financing.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A three-leg financial swap is a more complex type of swap agreement where three different payment streams (or 'legs')
      are involved, as opposed to the traditional two-leg swaps (like fixed-for-floating interest rate swaps). This structure
      can be useful for sophisticated risk management or hedging strategies, particularly when exposure to multiple interest
      rates or currencies is desired.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A two-leg financial swap is the most common type of swap agreement, where two counterparties exchange cash flows
      or obligations based on different financial variables. Each leg represents a stream of payments or flows tied to specific
      terms, such as fixed or floating interest rates, currencies, or commodities. The classic example of a two-leg swap is
      the interest rate swap, where one party pays a fixed interest rate while the other pays a floating interest rate.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For some swaps this may be a commitment to net up the difference between a strike and an outcome, rather than to
      make a series of cashflows over time. For credit default swaps there are conditional commitments, contingent on the
      occurrence of a credit event.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In most cases, a swap has two legs, one expressing the obligations of the seller and one expressing the obligations
      of the buyer. However, it is possible to represent more complex swaps, with one, three or more legs. The legs can be
      almost anything but usually one leg involves cash flows based on a notional principal amount that both parties agree
      to.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/isLegOf
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isDenominatedIn
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasEffectiveDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasTerminationDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapPayingParty
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasBuyer
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapReceivingParty
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasSeller
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CashflowTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CashflowTerms
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/SwapTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapTerms
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: swap leg
type: Ontology Class
---

# swap leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg>

## Definition

terms defining and the commitment to fulfill cashflow requirements (e.g., interest payments, coupon payments, etc.) for a component of a swap

## Relationships

- **Subclass of**: [CashflowTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CashflowTerms.md)
- **Subclass of**: [SwapTerms](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapTerms.md)

## Constraints

- **[isLegOf](/concepts/fibo/DER/DerivativesContracts/Swaps/isLegOf.md)**: some values from of type [Swap](/concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md)
- **[isDenominatedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isDenominatedIn.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasEffectiveDate](/concepts/fibo/FND/Agreements/Contracts/hasEffectiveDate.md)**: exact qualified cardinality 1 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasTerminationDate](/concepts/fibo/FND/Arrangements/Documents/hasTerminationDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasBuyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/hasBuyer.md)**: exact qualified cardinality 1 of type [SwapPayingParty](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapPayingParty.md)
- **[hasSeller](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/hasSeller.md)**: exact qualified cardinality 1 of type [SwapReceivingParty](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapReceivingParty.md)

## Annotations

- **label**: swap leg
- **definition**: terms defining and the commitment to fulfill cashflow requirements (e.g., interest payments, coupon payments, etc.) for a component of a swap
- **explanatoryNote**: A one-leg financing swap (also known as a single-leg financing swap) is a type of financial derivative, typically used by institutional investors or corporations, in which one party makes a series of fixed or floating payments to another party in exchange for a single upfront cash payment or financing.
- **explanatoryNote**: A three-leg financial swap is a more complex type of swap agreement where three different payment streams (or 'legs') are involved, as opposed to the traditional two-leg swaps (like fixed-for-floating interest rate swaps). This structure can be useful for sophisticated risk management or hedging strategies, particularly when exposure to multiple interest rates or currencies is desired.
- **explanatoryNote**: A two-leg financial swap is the most common type of swap agreement, where two counterparties exchange cash flows or obligations based on different financial variables. Each leg represents a stream of payments or flows tied to specific terms, such as fixed or floating interest rates, currencies, or commodities. The classic example of a two-leg swap is the interest rate swap, where one party pays a fixed interest rate while the other pays a floating interest rate.
- **explanatoryNote**: For some swaps this may be a commitment to net up the difference between a strike and an outcome, rather than to make a series of cashflows over time. For credit default swaps there are conditional commitments, contingent on the occurrence of a credit event.
- **explanatoryNote**: In most cases, a swap has two legs, one expressing the obligations of the seller and one expressing the obligations of the buyer. However, it is possible to represent more complex swaps, with one, three or more legs. The legs can be almost anything but usually one leg involves cash flows based on a notional principal amount that both parties agree to.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
