---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund processing terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'Formal terms for processing of the fund. These set out what the investor and the fund may or may not do. These
      include terms for redemption and subscription processing as well as general processing terms. ISO FIBIM definition:
      Processing characteristics linked to the instrument, ie, not to the market.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'These include Fund Subscription Terms, Fund Redemption Terms. and terms which relate to general processing and
      restrictions or otherwise on the holder. FPP notes: FPP presentation identifies many of these terms under the heading
      of Valuation Dealing characteristics. May need to revise which goes where in line with FPP. See also terms under NAV
      Valuation Calculation Method. Others of these terms appear in FPP under Instrument Restrictions. These cover the subscription,
      redemption and holding amounts and units and minimum holding period.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingAccount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/definesMainFundOrderDeskAccount
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/SettlementConvention
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasDefaultSettlementConvention
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund processing terms
type: Ontology Class
---

# fund processing terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms>

## Definition

Formal terms for processing of the fund. These set out what the investor and the fund may or may not do. These include terms for redemption and subscription processing as well as general processing terms. ISO FIBIM definition: Processing characteristics linked to the instrument, ie, not to the market.

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Constraints

- **[definesMainFundOrderDeskAccount](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/definesMainFundOrderDeskAccount.md)**: some values from of type [FundsProcessingAccount](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingAccount.md)
- **[hasDefaultSettlementConvention](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasDefaultSettlementConvention.md)**: some values from of type [SettlementConvention](/concepts/fibo/FBC/FinancialInstruments/Settlement/SettlementConvention.md)

## Annotations

- **label** (en): fund processing terms
- **definition** (en): Formal terms for processing of the fund. These set out what the investor and the fund may or may not do. These include terms for redemption and subscription processing as well as general processing terms. ISO FIBIM definition: Processing characteristics linked to the instrument, ie, not to the market.
- **explanatoryNote** (en): These include Fund Subscription Terms, Fund Redemption Terms. and terms which relate to general processing and restrictions or otherwise on the holder. FPP notes: FPP presentation identifies many of these terms under the heading of Valuation Dealing characteristics. May need to revise which goes where in line with FPP. See also terms under NAV Valuation Calculation Method. Others of these terms appear in FPP under Instrument Restrictions. These cover the subscription, redemption and holding amounts and units and minimum holding period.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
