---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit default swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bilateral contract in which one party (protection seller) agrees to provide payment to the other party (protection
      buyer) should a credit event occur against the underlying, which could be a specified debt (the reference obligation),
      a specific debt issuer (reference entity), a basket of reference entities and/or reference obligations, or a credit
      index (reference index)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CDS
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: According to a 2022 working paper from the Federal Reserve, "credit default swaps (CDS) are, by far, the most common
      type of credit derivative. They are financial instruments that allow the transfer of credit risk among market participants,
      potentially facilitating greater efficiency in the pricing and distribution of credit risk. In its most basic form,
      a CDS is a contract where a 'protection buyer' agrees to make periodic payments (the CDS 'spread' or premium) over a
      predetermined number of years (the maturity or term of the CDS) to a 'protection seller' in exchange for a payment from
      the protection seller in the event of default by a 'reference entity.' CDS premiums tend to be paid quarterly and are
      set as a percentage of the total amount of protection bought (the 'notional amount' of the contract). CDS maturities
      generally range from one to ten years, with the five-year maturity being particularly common." See https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf
      for more detail.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the effective date of the contract indicates the starting date of the credit protection defined therein.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/hasContractPrice
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/SettlementAuction
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOccurrence
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CreditDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CreditDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: credit default swap
type: Ontology Class
---

# credit default swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap>

## Definition

bilateral contract in which one party (protection seller) agrees to provide payment to the other party (protection buyer) should a credit event occur against the underlying, which could be a specified debt (the reference obligation), a specific debt issuer (reference entity), a basket of reference entities and/or reference obligations, or a credit index (reference index)

## Relationships

- **Subclass of**: [CreditDerivative](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CreditDerivative.md)
- **Subclass of**: [Swap](/concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md)

## Constraints

- **[hasContractPrice](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/hasContractPrice.md)**: some values from of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [CreditProtectionTerms](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms.md)
- **[hasOccurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOccurrence.md)**: min qualified cardinality 0 of type [SettlementAuction](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/SettlementAuction.md)
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: some values from of type [TriggeringEvent](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md)

## Annotations

- **label** (en): credit default swap
- **definition** (en): bilateral contract in which one party (protection seller) agrees to provide payment to the other party (protection buyer) should a credit event occur against the underlying, which could be a specified debt (the reference obligation), a specific debt issuer (reference entity), a basket of reference entities and/or reference obligations, or a credit index (reference index)
- **abbreviation** (en): CDS
- **adaptedFrom**: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code
- **explanatoryNote** (en): According to a 2022 working paper from the Federal Reserve, "credit default swaps (CDS) are, by far, the most common type of credit derivative. They are financial instruments that allow the transfer of credit risk among market participants, potentially facilitating greater efficiency in the pricing and distribution of credit risk. In its most basic form, a CDS is a contract where a 'protection buyer' agrees to make periodic payments (the CDS 'spread' or premium) over a predetermined number of years (the maturity or term of the CDS) to a 'protection seller' in exchange for a payment from the protection seller in the event of default by a 'reference entity.' CDS premiums tend to be paid quarterly and are set as a percentage of the total amount of protection bought (the 'notional amount' of the contract). CDS maturities generally range from one to ten years, with the five-year maturity being particularly common." See https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf for more detail.
- **explanatoryNote** (en): Note that the effective date of the contract indicates the starting date of the credit protection defined therein.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
