---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology is provided for the convenience of FIBO users. It loads the latest FIBO development ontologies, excluding
      reference data and examples, based on the contents of GitHub, rather than those that comprise a specific version, such
      as a quarterly release. Note that metadata files and other 'load' files, such as the various domain-specific 'all' files,
      are intentionally excluded.
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/issued
    value: '2026-06-02T18:00:00'
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2026 EDM Association dba EDM Council, Inc.\n\t\t\nPermission is hereby granted, free of charge,\
      \ to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the\
      \ Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute,\
      \ sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,\
      \ subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in\
      \ all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,\
      \ EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE\
      \ AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\
      \ LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE\
      \ OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/modified
    value: '2026-07-07T18:00:00'
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: About FIBO Development - T-Box Only
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    value: https://spec.edmcouncil.org/fibo/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2026 EDM Association dba EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: As of the Q1 2026 release of FIBO, there is one ontology, Bonds, in Securities, that brings in some reference individuals.
      The intent is to address this in a future release.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/20260701/AboutFIBODev-TBoxOnly/
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/
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
  - concept: /concepts/fibo/BP/Process/FinancialContextAndProcess.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/Process/FinancialContextAndProcess/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MBSIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MBSIssuance/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/
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
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditRatings.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/
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
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CAFinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CAFinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/RegulatoryAgencies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CashFlows.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
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
  - concept: /concepts/fibo/FND/TransactionsExt/MarketTransactions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/
  - concept: /concepts/fibo/FND/TransactionsExt/SecuritiesTransactions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/
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
  - concept: /concepts/fibo/IND/InterestRates/InterestRates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanApplications.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanEvents.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoansRegulatory.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/
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
  - concept: /concepts/fibo/LOAN/LoansSpecific/LoanProducts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/
  - concept: /concepts/fibo/LOAN/LoansSpecific/MarineFinance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/
  - concept: /concepts/fibo/LOAN/LoansSpecific/StudentLoans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/
  - concept: /concepts/fibo/LOAN/RealEstateLoans/ConstructionLoans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/ConstructionLoans/
  - concept: /concepts/fibo/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/
  - concept: /concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/
  - concept: /concepts/fibo/MD/CIVTemporal/FundsTemporal.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/CIVTemporal/FundsTemporal/
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/
  - concept: /concepts/fibo/MD/DerivativesTemporal/ETOptionsTemporal.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/
  - concept: /concepts/fibo/MD/DerivativesTemporal/FuturesTemporal.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/
  - concept: /concepts/fibo/MD/TemporalCore/SecurityCreditStatuses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityCreditStatuses/
  - concept: /concepts/fibo/MD/TemporalCore/SecurityTradingStatuses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/
  - concept: /concepts/fibo/SEC/Debt/AssetBackedSecurities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/
  - concept: /concepts/fibo/SEC/Debt/Bonds.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/
  - concept: /concepts/fibo/SEC/Debt/DistributedLoans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/
  - concept: /concepts/fibo/SEC/Debt/SyntheticCDOs.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/
  - concept: /concepts/fibo/SEC/Funds/Funds.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/
  - concept: /concepts/fibo/SEC/Securities/Baskets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/
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
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/
resource: https://spec.edmcouncil.org/fibo/ontology/AboutFIBODev-TBoxOnly/
sources:
- id: fibo-source-c1616ea76d
  resource: references/fibo/AboutFIBODev-TBoxOnly.rdf
  sha256: c1616ea76d51f1d68d65b77cb364f3644871a6f8458c63d8e91d8123f7c0d9b3
  title: FIBO source AboutFIBODev-TBoxOnly.rdf
title: About FIBO Development - T-Box Only
type: Ontology Definition
---

# About FIBO Development - T-Box Only

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/AboutFIBODev-TBoxOnly/>

## Relationships

- **Related to**: [FunctionalEntities](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md)
- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [GovernmentEntities](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md)
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
- **Related to**: [FinancialContextAndProcess](/concepts/fibo/BP/Process/FinancialContextAndProcess.md)
- **Related to**: [AgencyMBSIssuance](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.md)
- **Related to**: [DebtIssuance](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance.md)
- **Related to**: [EquitiesIPOIssuance](/concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance.md)
- **Related to**: [IssuanceDocuments](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments.md)
- **Related to**: [IssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess.md)
- **Related to**: [MBSIssuance](/concepts/fibo/BP/SecuritiesIssuance/MBSIssuance.md)
- **Related to**: [MuniIssuance](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance.md)
- **Related to**: [PrivateLabelMBSIssuance](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.md)
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
- **Related to**: [IRSwaps](/concepts/fibo/DER/RateDerivatives/IRSwaps.md)
- **Related to**: [RateDerivatives](/concepts/fibo/DER/RateDerivatives/RateDerivatives.md)
- **Related to**: [EquitySwaps](/concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps.md)
- **Related to**: [SecurityBasedDerivatives](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.md)
- **Related to**: [CreditEvents](/concepts/fibo/FBC/DebtAndEquities/CreditEvents.md)
- **Related to**: [CreditRatings](/concepts/fibo/FBC/DebtAndEquities/CreditRatings.md)
- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [InstrumentPricing](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md)
- **Related to**: [Settlement](/concepts/fibo/FBC/FinancialInstruments/Settlement.md)
- **Related to**: [BusinessCenters](/concepts/fibo/FBC/FunctionalEntities/BusinessCenters.md)
- **Related to**: [BusinessRegistries](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md)
- **Related to**: [EUFinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [Markets](/concepts/fibo/FBC/FunctionalEntities/Markets.md)
- **Related to**: [CAFinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CAFinancialServicesEntities.md)
- **Related to**: [RegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/RegulatoryAgencies.md)
- **Related to**: [ClientsAndAccounts](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CashFlows](/concepts/fibo/FND/Accounting/CashFlows.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
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
- **Related to**: [RealProperty](/concepts/fibo/FND/Places/RealProperty.md)
- **Related to**: [VirtualPlaces](/concepts/fibo/FND/Places/VirtualPlaces.md)
- **Related to**: [PaymentsAndSchedules](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules.md)
- **Related to**: [ProductsAndServices](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [MarketTransactions](/concepts/fibo/FND/TransactionsExt/MarketTransactions.md)
- **Related to**: [REATransactions](/concepts/fibo/FND/TransactionsExt/REATransactions.md)
- **Related to**: [SecuritiesTransactions](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions.md)
- **Related to**: [Analytics](/concepts/fibo/FND/Utilities/Analytics.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [EconomicIndicators](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators.md)
- **Related to**: [CAEconomicIndicators](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.md)
- **Related to**: [USEconomicIndicators](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.md)
- **Related to**: [ForeignExchange](/concepts/fibo/IND/ForeignExchange/ForeignExchange.md)
- **Related to**: [Indicators](/concepts/fibo/IND/Indicators/Indicators.md)
- **Related to**: [InterestRates](/concepts/fibo/IND/InterestRates/InterestRates.md)
- **Related to**: [BasketIndices](/concepts/fibo/IND/MarketIndices/BasketIndices.md)
- **Related to**: [LoanApplications](/concepts/fibo/LOAN/LoansGeneral/LoanApplications.md)
- **Related to**: [LoanEvents](/concepts/fibo/LOAN/LoansGeneral/LoanEvents.md)
- **Related to**: [Loans](/concepts/fibo/LOAN/LoansGeneral/Loans.md)
- **Related to**: [LoansRegulatory](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory.md)
- **Related to**: [CardAccounts](/concepts/fibo/LOAN/LoansSpecific/CardAccounts.md)
- **Related to**: [CommercialLoans](/concepts/fibo/LOAN/LoansSpecific/CommercialLoans.md)
- **Related to**: [ConsumerLoans](/concepts/fibo/LOAN/LoansSpecific/ConsumerLoans.md)
- **Related to**: [GreenLoans](/concepts/fibo/LOAN/LoansSpecific/GreenLoans.md)
- **Related to**: [LoanProducts](/concepts/fibo/LOAN/LoansSpecific/LoanProducts.md)
- **Related to**: [MarineFinance](/concepts/fibo/LOAN/LoansSpecific/MarineFinance.md)
- **Related to**: [StudentLoans](/concepts/fibo/LOAN/LoansSpecific/StudentLoans.md)
- **Related to**: [ConstructionLoans](/concepts/fibo/LOAN/RealEstateLoans/ConstructionLoans.md)
- **Related to**: [HomeMortgageDisclosureActCoveredMortgages](/concepts/fibo/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.md)
- **Related to**: [MortgageOrigination](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination.md)
- **Related to**: [Mortgages](/concepts/fibo/LOAN/RealEstateLoans/Mortgages.md)
- **Related to**: [FundsTemporal](/concepts/fibo/MD/CIVTemporal/FundsTemporal.md)
- **Related to**: [DebtAnalytics](/concepts/fibo/MD/DebtTemporal/DebtAnalytics.md)
- **Related to**: [ETOptionsTemporal](/concepts/fibo/MD/DerivativesTemporal/ETOptionsTemporal.md)
- **Related to**: [FuturesTemporal](/concepts/fibo/MD/DerivativesTemporal/FuturesTemporal.md)
- **Related to**: [SecurityCreditStatuses](/concepts/fibo/MD/TemporalCore/SecurityCreditStatuses.md)
- **Related to**: [SecurityTradingStatuses](/concepts/fibo/MD/TemporalCore/SecurityTradingStatuses.md)
- **Related to**: [AssetBackedSecurities](/concepts/fibo/SEC/Debt/AssetBackedSecurities.md)
- **Related to**: [Bonds](/concepts/fibo/SEC/Debt/Bonds.md)
- **Related to**: [CollateralizedDebtObligations](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations.md)
- **Related to**: [DebtInstruments](/concepts/fibo/SEC/Debt/DebtInstruments.md)
- **Related to**: [DistributedLoans](/concepts/fibo/SEC/Debt/DistributedLoans.md)
- **Related to**: [ExerciseConventions](/concepts/fibo/SEC/Debt/ExerciseConventions.md)
- **Related to**: [MortgageBackedSecurities](/concepts/fibo/SEC/Debt/MortgageBackedSecurities.md)
- **Related to**: [PoolBackedSecurities](/concepts/fibo/SEC/Debt/PoolBackedSecurities.md)
- **Related to**: [SyntheticCDOs](/concepts/fibo/SEC/Debt/SyntheticCDOs.md)
- **Related to**: [TradedShortTermDebt](/concepts/fibo/SEC/Debt/TradedShortTermDebt.md)
- **Related to**: [DepositaryReceipts](/concepts/fibo/SEC/Equities/DepositaryReceipts.md)
- **Related to**: [EquityInstruments](/concepts/fibo/SEC/Equities/EquityInstruments.md)
- **Related to**: [CollectiveInvestmentVehicles](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles.md)
- **Related to**: [Funds](/concepts/fibo/SEC/Funds/Funds.md)
- **Related to**: [Baskets](/concepts/fibo/SEC/Securities/Baskets.md)
- **Related to**: [ParametricSchedules](/concepts/fibo/SEC/Securities/ParametricSchedules.md)
- **Related to**: [Pools](/concepts/fibo/SEC/Securities/Pools.md)
- **Related to**: [SecuritiesClassification](/concepts/fibo/SEC/Securities/SecuritiesClassification.md)
- **Related to**: [SecuritiesIdentification](/concepts/fibo/SEC/Securities/SecuritiesIdentification.md)
- **Related to**: [SecuritiesIssuance](/concepts/fibo/SEC/Securities/SecuritiesIssuance.md)
- **Related to**: [SecuritiesListings](/concepts/fibo/SEC/Securities/SecuritiesListings.md)
- **Related to**: [AboutFIBODev-TBoxOnly](<https://spec.edmcouncil.org/fibo/ontology/20260701/AboutFIBODev-TBoxOnly/>)

## Annotations

- **abstract**: This ontology is provided for the convenience of FIBO users. It loads the latest FIBO development ontologies, excluding reference data and examples, based on the contents of GitHub, rather than those that comprise a specific version, such as a quarterly release. Note that metadata files and other 'load' files, such as the various domain-specific 'all' files, are intentionally excluded.
- **issued**: 2026-06-02T18:00:00
- **license**: Copyright (c) 2026 EDM Association dba EDM Council, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **modified**: 2026-07-07T18:00:00
- **label**: About FIBO Development - T-Box Only
- **seeAlso**: https://spec.edmcouncil.org/fibo/
- **copyright**: Copyright (c) 2026 EDM Association dba EDM Council, Inc.
- **usageNote**: As of the Q1 2026 release of FIBO, there is one ontology, Bonds, in Securities, that brings in some reference individuals. The intent is to address this in a future release.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
