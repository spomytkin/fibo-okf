---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund unit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: quantified share of beneficial interest in a pooled fund, representing a proportional claim on the fund's assets,
      income, or entitlements
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A fund unit may be tradable or non-tradable depending on the legal form, regulatory status, and operational framework
      of the fund.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Fund units are allocated to a participant, investor, or beneficiary according to the fund's governing structure.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If it is a closed fund, you can still trade the units. You trade back with the fund. Not with a counterparty. Therefore
      this is a tradable contract, though it may not necessarily be a transferable contract.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/NetAssetValueCalculationMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasDetails
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingGeneralTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasFundProcessingTerms
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundRedemptionTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasFundProcessingTerms
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PooledFund
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isPartOf
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/ContractualInterest.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualInterest
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: fund unit
type: Ontology Class
---

# fund unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit>

## Definition

quantified share of beneficial interest in a pooled fund, representing a proportional claim on the fund's assets, income, or entitlements

## Relationships

- **Subclass of**: [ContractualInterest](/concepts/fibo/FND/Law/LegalCapacity/ContractualInterest.md)

## Constraints

- **[hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)**: some values from of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasDetails](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasDetails.md)**: some values from of type [NetAssetValueCalculationMethod](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/NetAssetValueCalculationMethod.md)
- **[hasFundProcessingTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasFundProcessingTerms.md)**: some values from of type [FundProcessingGeneralTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingGeneralTerms.md)
- **[hasFundProcessingTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasFundProcessingTerms.md)**: some values from of type [FundRedemptionTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundRedemptionTerms.md)
- **[isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)**: some values from of type [PooledFund](/concepts/fibo/SEC/Securities/Pools/PooledFund.md)

## Annotations

- **label**: fund unit
- **definition**: quantified share of beneficial interest in a pooled fund, representing a proportional claim on the fund's assets, income, or entitlements
- **explanatoryNote**: A fund unit may be tradable or non-tradable depending on the legal form, regulatory status, and operational framework of the fund.
- **explanatoryNote**: Fund units are allocated to a participant, investor, or beneficiary according to the fund's governing structure.
- **explanatoryNote** (en): If it is a closed fund, you can still trade the units. You trade back with the fund. Not with a counterparty. Therefore this is a tradable contract, though it may not necessarily be a transferable contract.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
