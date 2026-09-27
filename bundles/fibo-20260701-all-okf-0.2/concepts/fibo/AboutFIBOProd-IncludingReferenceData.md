---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology is provided for the convenience of FIBO users. It loads the latest FIBO production ontologies, including
      reference data but excluding examples, based on the contents of GitHub, rather than those that comprise a specific version,
      such as a quarterly release. By reference data we mean ISO currency codes and USPS individuals in FND, juridictions
      and governments in BE, regulatory agencies and related financial services entities as well as business centers and MIC
      codes in FBC, FpML interest rates in IND, CFI codes in SEC (incomplete but planned for extension in subsequent releases),
      and so forth. Note that metadata files and other 'load' files, such as the various domain-specific 'all' files, are
      intentionally excluded.
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/issued
    value: '2018-03-31T18:00:00'
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2018-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\nSee https://opensource.org/licenses/MIT."
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/modified
    value: '2026-07-07T18:00:00'
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: About FIBO Production - including Reference Data
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    value: https://spec.edmcouncil.org/fibo/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 Object Management Group
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/20260701/AboutFIBOProd-IncludingReferenceData/
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - concept: /concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/CentralAsiaGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/CentralAsiaGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/EasternAsiaGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/EasternAsiaGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/SoutheasternAsiaGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/SoutheasternAsiaGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/SouthernAsiaGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/SouthernAsiaGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/WesternAsiaGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/WesternAsiaGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EasternEuropeGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/EasternEuropeGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/NorthernEuropeGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/NorthernEuropeGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/SouthernEuropeGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/SouthernEuropeGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/UKGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/UKGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/
  - concept: /concepts/fibo/BE/GovernmentEntities/LatinAmericanJurisdiction/CentralAmericanGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/LatinAmericanJurisdiction/CentralAmericanGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/LatinAmericanJurisdiction/SouthAmericanGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/LatinAmericanJurisdiction/SouthAmericanGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CaribbeanGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/CaribbeanGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/MXGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/MXGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/LegalEntities/LEIEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/
  - concept: /concepts/fibo/BE/Partnerships/Partnerships.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/
  - concept: /concepts/fibo/BE/SoleProprietorships/SoleProprietorships.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/SoleProprietorships/SoleProprietorships/
  - concept: /concepts/fibo/BE/Trusts/Trusts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/
  - concept: /concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/
  - concept: /concepts/fibo/DER/DerivativesContracts/CurrencyContracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesMasterAgreements.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/
  - concept: /concepts/fibo/DER/DerivativesContracts/ExoticOptions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/
  - concept: /concepts/fibo/DER/DerivativesContracts/Options.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/
  - concept: /concepts/fibo/DER/DerivativesContracts/SwapsIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/
  - concept: /concepts/fibo/DER/RateDerivatives/RateDerivatives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/RateDerivatives/
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/
  - concept: /concepts/fibo/FBC/FinancialInstruments/Settlement.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCenters.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EuropeanFinancialServicesEntitiesIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EuropeanFinancialServicesEntitiesIndividuals/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CAFinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CAFinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  - concept: /concepts/fibo/FBC/FunctionalEntities/RegulatoryAgencies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/
  - concept: /concepts/fibo/FND/AgentsAndPeople/People.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/
  - concept: /concepts/fibo/FND/Agreements/Agreements.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/Arrangements/Arrangements.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Arrangements/
  - concept: /concepts/fibo/FND/Arrangements/Assessments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/
  - concept: /concepts/fibo/FND/Arrangements/Documents.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/
  - concept: /concepts/fibo/FND/Arrangements/IdentifiersAndIndices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/
  - concept: /concepts/fibo/FND/Arrangements/Ratings.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/
  - concept: /concepts/fibo/FND/Arrangements/Reporting.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/Law/LegalCapacity.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/
  - concept: /concepts/fibo/FND/Law/LegalCore.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
  - concept: /concepts/fibo/FND/OwnershipAndControl/OwnershipAndControl.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/
  - concept: /concepts/fibo/FND/Parties/Parties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/
  - concept: /concepts/fibo/FND/Places/Addresses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/
  - concept: /concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/
  - concept: /concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddressesIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddressesIndividuals/
  - concept: /concepts/fibo/FND/Places/RealProperty.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/
  - concept: /concepts/fibo/FND/Places/VirtualPlaces.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/Analytics.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/
  - concept: /concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/
  - concept: /concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/
  - concept: /concepts/fibo/IND/Indicators/Indicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/
  - concept: /concepts/fibo/IND/InterestRates/CommonInterestRates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/
  - concept: /concepts/fibo/IND/InterestRates/InterestRates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/
  - concept: /concepts/fibo/IND/InterestRates/MarketDataProviders.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/
  - concept: /concepts/fibo/LOAN/LoansSpecific/CommercialLoans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/
  - concept: /concepts/fibo/LOAN/LoansSpecific/ConsumerLoans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/
  - concept: /concepts/fibo/LOAN/LoansSpecific/GreenLoans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/
  - concept: /concepts/fibo/LOAN/LoansSpecific/StudentLoans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/
  - concept: /concepts/fibo/SEC/Debt/AssetBackedSecurities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/
  - concept: /concepts/fibo/SEC/Debt/Bonds.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/
  - concept: /concepts/fibo/SEC/Debt/DistributedLoans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/
  - concept: /concepts/fibo/SEC/Equities/EquityCFIClassificationIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/
  - concept: /concepts/fibo/SEC/Funds/Funds.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/
  - concept: /concepts/fibo/SEC/Securities/Baskets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/
  - concept: /concepts/fibo/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/
  - concept: /concepts/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/
  - concept: /concepts/fibo/SEC/Securities/ParametricSchedules.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/
  - concept: /concepts/fibo/SEC/Securities/Pools.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesClassification.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesRestrictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-2-SubdivisionCodes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-AD/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-AG/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-AL/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-AS/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-AT/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BA/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BB/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BE/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BG/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BQ/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BS/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BY/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BZ/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CA/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CH/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CR/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CU/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CZ/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-DE/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-DK/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-DM/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-DO/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-EE/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-ES/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-FI/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-FR/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GB/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GD/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GG/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GL/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GP/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GR/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GT/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-HN/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-HR/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-HT/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-HU/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-IE/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-IS/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-IT/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-KN/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-KY/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-LC/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-LI/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-LT/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-LU/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-LV/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MC/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MD/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-ME/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MF/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MK/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MP/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MT/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MX/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-NI/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-NL/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-NO/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-PA/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-PL/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-PM/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-PT/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-RO/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-RS/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-RU/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SE/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SI/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SJ/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SK/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SM/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SV/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-TC/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-TT/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-UA/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-UM/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-VC/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-VG/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-VI/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/UN-M49-RegionCodes/
resource: https://spec.edmcouncil.org/fibo/ontology/AboutFIBOProd-IncludingReferenceData/
sources:
- id: fibo-source-314b2875a2
  resource: references/fibo/AboutFIBOProd-IncludingReferenceData.rdf
  sha256: 314b2875a2e429faea509e852fc56d3b6228a680f8290a04865c176e64e8563f
  title: FIBO source AboutFIBOProd-IncludingReferenceData.rdf
title: About FIBO Production - including Reference Data
type: Ontology Definition
---

# About FIBO Production - including Reference Data

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/AboutFIBOProd-IncludingReferenceData/>

## Relationships

- **Related to**: [FunctionalEntities](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md)
- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [CentralAsiaGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/CentralAsiaGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [EasternAsiaGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/EasternAsiaGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [SoutheasternAsiaGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/SoutheasternAsiaGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [SouthernAsiaGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/SouthernAsiaGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [WesternAsiaGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/WesternAsiaGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [EUGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [EasternEuropeGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EasternEuropeGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [NorthernEuropeGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/NorthernEuropeGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [SouthernEuropeGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/SouthernEuropeGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [UKGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/UKGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [WesternEuropeGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [GovernmentEntities](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md)
- **Related to**: [CentralAmericanGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/LatinAmericanJurisdiction/CentralAmericanGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [SouthAmericanGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/LatinAmericanJurisdiction/SouthAmericanGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [CAGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [CaribbeanGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CaribbeanGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [MXGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/MXGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [USGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [CorporateBodies](/concepts/fibo/BE/LegalEntities/CorporateBodies.md)
- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [LEIEntities](/concepts/fibo/BE/LegalEntities/LEIEntities.md)
- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [ControlParties](/concepts/fibo/BE/OwnershipAndControl/ControlParties.md)
- **Related to**: [CorporateControl](/concepts/fibo/BE/OwnershipAndControl/CorporateControl.md)
- **Related to**: [CorporateOwnership](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md)
- **Related to**: [Executives](/concepts/fibo/BE/OwnershipAndControl/Executives.md)
- **Related to**: [OwnershipParties](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md)
- **Related to**: [Partnerships](/concepts/fibo/BE/Partnerships/Partnerships.md)
- **Related to**: [PrivateLimitedCompanies](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.md)
- **Related to**: [SoleProprietorships](/concepts/fibo/BE/SoleProprietorships/SoleProprietorships.md)
- **Related to**: [Trusts](/concepts/fibo/BE/Trusts/Trusts.md)
- **Related to**: [CorporateActions](/concepts/fibo/CAE/CorporateEvents/CorporateActions.md)
- **Related to**: [CreditDefaultSwaps](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps.md)
- **Related to**: [CommoditiesContracts](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts.md)
- **Related to**: [CurrencyContracts](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts.md)
- **Related to**: [DerivativesBasics](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics.md)
- **Related to**: [DerivativesMasterAgreements](/concepts/fibo/DER/DerivativesContracts/DerivativesMasterAgreements.md)
- **Related to**: [ExoticOptions](/concepts/fibo/DER/DerivativesContracts/ExoticOptions.md)
- **Related to**: [FuturesAndForwards](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards.md)
- **Related to**: [Options](/concepts/fibo/DER/DerivativesContracts/Options.md)
- **Related to**: [RightsAndWarrants](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants.md)
- **Related to**: [StructuredInstruments](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments.md)
- **Related to**: [Swaps](/concepts/fibo/DER/DerivativesContracts/Swaps.md)
- **Related to**: [SwapsIndividuals](/concepts/fibo/DER/DerivativesContracts/SwapsIndividuals.md)
- **Related to**: [IRSwaps](/concepts/fibo/DER/RateDerivatives/IRSwaps.md)
- **Related to**: [RateDerivatives](/concepts/fibo/DER/RateDerivatives/RateDerivatives.md)
- **Related to**: [EquitySwaps](/concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps.md)
- **Related to**: [SecurityBasedDerivatives](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.md)
- **Related to**: [CreditEvents](/concepts/fibo/FBC/DebtAndEquities/CreditEvents.md)
- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [InstrumentPricing](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md)
- **Related to**: [Settlement](/concepts/fibo/FBC/FinancialInstruments/Settlement.md)
- **Related to**: [BusinessCenters](/concepts/fibo/FBC/FunctionalEntities/BusinessCenters.md)
- **Related to**: [BusinessCentersIndividuals](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals.md)
- **Related to**: [BusinessRegistries](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md)
- **Related to**: [CommercialRegistrationAuthorities](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md)
- **Related to**: [EUFinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.md)
- **Related to**: [EURegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies.md)
- **Related to**: [EuropeanFinancialServicesEntitiesIndividuals](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EuropeanFinancialServicesEntitiesIndividuals.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [InternationalRegistriesAndAuthorities](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.md)
- **Related to**: [Markets](/concepts/fibo/FBC/FunctionalEntities/Markets.md)
- **Related to**: [MarketsIndividuals](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals.md)
- **Related to**: [CAFinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CAFinancialServicesEntities.md)
- **Related to**: [CARegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.md)
- **Related to**: [USFinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.md)
- **Related to**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [RegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/RegulatoryAgencies.md)
- **Related to**: [ClientsAndAccounts](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [ISO4217-CurrencyCodes](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes.md)
- **Related to**: [People](/concepts/fibo/FND/AgentsAndPeople/People.md)
- **Related to**: [Agreements](/concepts/fibo/FND/Agreements/Agreements.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Arrangements](/concepts/fibo/FND/Arrangements/Arrangements.md)
- **Related to**: [Assessments](/concepts/fibo/FND/Arrangements/Assessments.md)
- **Related to**: [ClassificationSchemes](/concepts/fibo/FND/Arrangements/ClassificationSchemes.md)
- **Related to**: [Documents](/concepts/fibo/FND/Arrangements/Documents.md)
- **Related to**: [IdentifiersAndIndices](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices.md)
- **Related to**: [Lifecycles](/concepts/fibo/FND/Arrangements/Lifecycles.md)
- **Related to**: [Ratings](/concepts/fibo/FND/Arrangements/Ratings.md)
- **Related to**: [Reporting](/concepts/fibo/FND/Arrangements/Reporting.md)
- **Related to**: [BusinessDates](/concepts/fibo/FND/DatesAndTimes/BusinessDates.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Occurrences](/concepts/fibo/FND/DatesAndTimes/Occurrences.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity.md)
- **Related to**: [LegalCore](/concepts/fibo/FND/Law/LegalCore.md)
- **Related to**: [FormalOrganizations](/concepts/fibo/FND/Organizations/FormalOrganizations.md)
- **Related to**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [OwnershipAndControl](/concepts/fibo/FND/OwnershipAndControl/OwnershipAndControl.md)
- **Related to**: [Parties](/concepts/fibo/FND/Parties/Parties.md)
- **Related to**: [Addresses](/concepts/fibo/FND/Places/Addresses.md)
- **Related to**: [USPostalServiceAddresses](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.md)
- **Related to**: [USPostalServiceAddressesIndividuals](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddressesIndividuals.md)
- **Related to**: [RealProperty](/concepts/fibo/FND/Places/RealProperty.md)
- **Related to**: [VirtualPlaces](/concepts/fibo/FND/Places/VirtualPlaces.md)
- **Related to**: [PaymentsAndSchedules](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules.md)
- **Related to**: [ProductsAndServices](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [Analytics](/concepts/fibo/FND/Utilities/Analytics.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [EconomicIndicators](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators.md)
- **Related to**: [CAEconomicIndicators](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.md)
- **Related to**: [USEconomicIndicators](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.md)
- **Related to**: [ForeignExchange](/concepts/fibo/IND/ForeignExchange/ForeignExchange.md)
- **Related to**: [Indicators](/concepts/fibo/IND/Indicators/Indicators.md)
- **Related to**: [CommonInterestRates](/concepts/fibo/IND/InterestRates/CommonInterestRates.md)
- **Related to**: [InterestRates](/concepts/fibo/IND/InterestRates/InterestRates.md)
- **Related to**: [MarketDataProviders](/concepts/fibo/IND/InterestRates/MarketDataProviders.md)
- **Related to**: [BasketIndices](/concepts/fibo/IND/MarketIndices/BasketIndices.md)
- **Related to**: [Loans](/concepts/fibo/LOAN/LoansGeneral/Loans.md)
- **Related to**: [CardAccounts](/concepts/fibo/LOAN/LoansSpecific/CardAccounts.md)
- **Related to**: [CommercialLoans](/concepts/fibo/LOAN/LoansSpecific/CommercialLoans.md)
- **Related to**: [ConsumerLoans](/concepts/fibo/LOAN/LoansSpecific/ConsumerLoans.md)
- **Related to**: [GreenLoans](/concepts/fibo/LOAN/LoansSpecific/GreenLoans.md)
- **Related to**: [StudentLoans](/concepts/fibo/LOAN/LoansSpecific/StudentLoans.md)
- **Related to**: [Mortgages](/concepts/fibo/LOAN/RealEstateLoans/Mortgages.md)
- **Related to**: [AssetBackedSecurities](/concepts/fibo/SEC/Debt/AssetBackedSecurities.md)
- **Related to**: [Bonds](/concepts/fibo/SEC/Debt/Bonds.md)
- **Related to**: [DebtInstruments](/concepts/fibo/SEC/Debt/DebtInstruments.md)
- **Related to**: [DistributedLoans](/concepts/fibo/SEC/Debt/DistributedLoans.md)
- **Related to**: [ExerciseConventions](/concepts/fibo/SEC/Debt/ExerciseConventions.md)
- **Related to**: [PoolBackedSecurities](/concepts/fibo/SEC/Debt/PoolBackedSecurities.md)
- **Related to**: [TradedShortTermDebt](/concepts/fibo/SEC/Debt/TradedShortTermDebt.md)
- **Related to**: [DepositaryReceipts](/concepts/fibo/SEC/Equities/DepositaryReceipts.md)
- **Related to**: [EquityCFIClassificationIndividuals](/concepts/fibo/SEC/Equities/EquityCFIClassificationIndividuals.md)
- **Related to**: [EquityInstruments](/concepts/fibo/SEC/Equities/EquityInstruments.md)
- **Related to**: [Funds](/concepts/fibo/SEC/Funds/Funds.md)
- **Related to**: [Baskets](/concepts/fibo/SEC/Securities/Baskets.md)
- **Related to**: [EUSecuritiesRestrictions](/concepts/fibo/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions.md)
- **Related to**: [USSecuritiesRestrictions](/concepts/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.md)
- **Related to**: [ParametricSchedules](/concepts/fibo/SEC/Securities/ParametricSchedules.md)
- **Related to**: [Pools](/concepts/fibo/SEC/Securities/Pools.md)
- **Related to**: [SecuritiesClassification](/concepts/fibo/SEC/Securities/SecuritiesClassification.md)
- **Related to**: [SecuritiesIdentification](/concepts/fibo/SEC/Securities/SecuritiesIdentification.md)
- **Related to**: [SecuritiesIdentificationIndividuals](/concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.md)
- **Related to**: [SecuritiesIssuance](/concepts/fibo/SEC/Securities/SecuritiesIssuance.md)
- **Related to**: [SecuritiesListings](/concepts/fibo/SEC/Securities/SecuritiesListings.md)
- **Related to**: [SecuritiesRestrictions](/concepts/fibo/SEC/Securities/SecuritiesRestrictions.md)
- **Related to**: [ISO3166-2-SubdivisionCodes](<https://www.omg.org/spec/LCC/Countries/ISO3166-2-SubdivisionCodes/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-AD](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-AD/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-AG](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-AG/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-AL](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-AL/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-AS](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-AS/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-AT](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-AT/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-BA](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BA/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-BB](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BB/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-BE](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BE/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-BG](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BG/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-BQ](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BQ/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-BS](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BS/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-BY](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BY/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-BZ](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-BZ/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-CA](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CA/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-CH](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CH/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-CR](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CR/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-CU](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CU/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-CZ](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CZ/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-DE](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-DE/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-DK](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-DK/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-DM](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-DM/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-DO](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-DO/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-EE](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-EE/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-ES](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-ES/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-FI](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-FI/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-FR](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-FR/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-GB](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GB/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-GD](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GD/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-GG](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GG/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-GL](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GL/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-GP](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GP/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-GR](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GR/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-GT](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-GT/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-HN](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-HN/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-HR](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-HR/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-HT](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-HT/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-HU](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-HU/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-IE](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-IE/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-IS](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-IS/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-IT](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-IT/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-KN](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-KN/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-KY](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-KY/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-LC](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-LC/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-LI](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-LI/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-LT](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-LT/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-LU](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-LU/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-LV](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-LV/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-MC](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MC/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-MD](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MD/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-ME](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-ME/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-MF](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MF/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-MK](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MK/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-MP](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MP/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-MT](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MT/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-MX](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-MX/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-NI](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-NI/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-NL](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-NL/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-NO](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-NO/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-PA](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-PA/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-PL](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-PL/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-PM](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-PM/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-PT](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-PT/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-RO](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-RO/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-RS](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-RS/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-RU](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-RU/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-SE](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SE/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-SI](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SI/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-SJ](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SJ/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-SK](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SK/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-SM](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SM/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-SV](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-SV/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-TC](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-TC/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-TT](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-TT/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-UA](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-UA/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-UM](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-UM/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-US](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-VC](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-VC/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-VG](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-VG/>)
- **Related to**: [ISO3166-2-SubdivisionCodes-VI](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-VI/>)
- **Related to**: [UN-M49-RegionCodes](<https://www.omg.org/spec/LCC/Countries/UN-M49-RegionCodes/>)
- **Related to**: [AboutFIBOProd-IncludingReferenceData](<https://spec.edmcouncil.org/fibo/ontology/20260701/AboutFIBOProd-IncludingReferenceData/>)

## Annotations

- **abstract**: This ontology is provided for the convenience of FIBO users. It loads the latest FIBO production ontologies, including reference data but excluding examples, based on the contents of GitHub, rather than those that comprise a specific version, such as a quarterly release. By reference data we mean ISO currency codes and USPS individuals in FND, juridictions and governments in BE, regulatory agencies and related financial services entities as well as business centers and MIC codes in FBC, FpML interest rates in IND, CFI codes in SEC (incomplete but planned for extension in subsequent releases), and so forth. Note that metadata files and other 'load' files, such as the various domain-specific 'all' files, are intentionally excluded.
- **issued**: 2018-03-31T18:00:00
- **license**: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2018-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **modified**: 2026-07-07T18:00:00
- **label**: About FIBO Production - including Reference Data
- **seeAlso**: https://spec.edmcouncil.org/fibo/
- **copyright**: Copyright (c) 2018-2025 Object Management Group
- **copyright**: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
