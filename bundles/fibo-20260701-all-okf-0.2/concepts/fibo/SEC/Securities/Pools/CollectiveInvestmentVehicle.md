---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collective investment vehicle
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: assets pooled by investors whose share capital remains separate from the assets of the vehicle
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A fund is an entity created to pool money from multiple investors - often referred to as limited partners. Each
      investor makes an investment in the fund by purchasing an interest in the fund entity, and the adviser uses that money
      to make investments on behalf of the fund.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Collective investment vehicles are typically organized and operated by management companies, banks, or trust companies.
      Shares or units are issued in the form of unit trusts, mutual funds, or other similar contracts. Common kinds of funds
      include pension funds, insurance funds, foundations, and endowments. Such pools are often invested and professionally
      managed, including investment pools, umbrella pools, share class pools, etc.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'From EFAMA DD: The word fund can refer to either an investment pool, umbrella or share class, and is commonly
      refered to as a collective investment vehicle (can have ISIN or not). The meaning here is for the investment pool (of
      which an Umbrella fund is also one such) and not to the share class.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/UnitIssuer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundAdministrator
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/administeredBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/RegisteredInvestmentAdvisor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/advisedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundDistributor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/distributedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/fundHasRelatedParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/OtherInvestmentFundInformation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasAdditionalInformation
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ExternalAuditor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasAuditor
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasDataProvider
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundDepositary
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasDepository
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentPolicy
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasFundPolicy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundManager
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasManagementCompany
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasRelatedFundTerms
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasSubscriptionTerms
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundTransferAgent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasTransferAgent
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundSupervisoryAuthority
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/supervisedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/LegalFundStructure
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/hasLegalStructure
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/Prospectus
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDescribedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/PooledFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PooledFund
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
- id: fibo-source-73259da08c
  resource: references/fibo/SEC/Securities/Pools.rdf
  sha256: 73259da08ce2d3336ab19acd98a9182e1bef062fb636a27936e96545e083ec39
  title: FIBO source SEC/Securities/Pools.rdf
title: collective investment vehicle
type: Ontology Class
---

# collective investment vehicle

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle>

## Definition

assets pooled by investors whose share capital remains separate from the assets of the vehicle

## Relationships

- **Subclass of**: [PooledFund](/concepts/fibo/SEC/Securities/Pools/PooledFund.md)

## Constraints

- **[isLegallyRecordedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn.md)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **[hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)**: some values from of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)**: some values from of type [FundUnitDistributionMethod](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionMethod.md)
- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from of type [UnitIssuer](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/UnitIssuer.md)
- **[administeredBy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/administeredBy.md)**: some values from of type [FundAdministrator](/concepts/fibo/SEC/Funds/Funds/FundAdministrator.md)
- **[advisedBy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/advisedBy.md)**: some values from of type [RegisteredInvestmentAdvisor](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/RegisteredInvestmentAdvisor.md)
- **[distributedBy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/distributedBy.md)**: some values from of type [FundDistributor](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundDistributor.md)
- **[fundHasRelatedParty](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/fundHasRelatedParty.md)**: some values from of type [FundsProcessingParty](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md)
- **[hasAdditionalInformation](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasAdditionalInformation.md)**: some values from of type [OtherInvestmentFundInformation](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/OtherInvestmentFundInformation.md)
- **[hasAuditor](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasAuditor.md)**: some values from of type [ExternalAuditor](/concepts/fibo/BE/OwnershipAndControl/Executives/ExternalAuditor.md)
- **[hasDataProvider](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasDataProvider.md)**: some values from of type [MarketDataProvider](/concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md)
- **[hasDepository](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasDepository.md)**: some values from of type [FundDepositary](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundDepositary.md)
- **[hasFundPolicy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasFundPolicy.md)**: some values from of type [FundInvestmentPolicy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentPolicy.md)
- **[hasManagementCompany](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasManagementCompany.md)**: some values from of type [FundManager](/concepts/fibo/SEC/Funds/Funds/FundManager.md)
- **[hasRelatedFundTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasRelatedFundTerms.md)**: some values from of type [FundProcessingTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms.md)
- **[hasSubscriptionTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasSubscriptionTerms.md)**: some values from of type [FundSubscriptionTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md)
- **[hasTransferAgent](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasTransferAgent.md)**: some values from of type [FundTransferAgent](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundTransferAgent.md)
- **[supervisedBy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/supervisedBy.md)**: some values from of type [FundSupervisoryAuthority](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundSupervisoryAuthority.md)
- **[hasLegalStructure](/concepts/fibo/SEC/Funds/Funds/hasLegalStructure.md)**: some values from of type [LegalFundStructure](/concepts/fibo/SEC/Funds/Funds/LegalFundStructure.md)
- **[isDescribedBy](<https://www.omg.org/spec/Commons/Designators/isDescribedBy>)**: some values from of type [Prospectus](/concepts/fibo/SEC/Securities/SecuritiesIssuance/Prospectus.md)

## Annotations

- **label** (en): collective investment vehicle
- **definition** (en): assets pooled by investors whose share capital remains separate from the assets of the vehicle
- **adaptedFrom** (en): ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth edition, October 2019
- **explanatoryNote** (en): A fund is an entity created to pool money from multiple investors - often referred to as limited partners. Each investor makes an investment in the fund by purchasing an interest in the fund entity, and the adviser uses that money to make investments on behalf of the fund.
- **explanatoryNote** (en): Collective investment vehicles are typically organized and operated by management companies, banks, or trust companies. Shares or units are issued in the form of unit trusts, mutual funds, or other similar contracts. Common kinds of funds include pension funds, insurance funds, foundations, and endowments. Such pools are often invested and professionally managed, including investment pools, umbrella pools, share class pools, etc.
- **explanatoryNote** (en): From EFAMA DD: The word fund can refer to either an investment pool, umbrella or share class, and is commonly refered to as a collective investment vehicle (can have ISIN or not). The meaning here is for the investment pool (of which an Umbrella fund is also one such) and not to the share class.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
