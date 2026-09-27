---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines the basic concept of a bond and a number of bond variants including convertible and callable
      bonds. Medium term notes (MTNs) and debentures are also defined.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2016-2025 EDM Council, Inc.\nCopyright (c) 2018-2025 Object Management Group, Inc.\n\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bonds Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190901/Securities/Debt/Bonds.rdf version of this ontology was
      revised to reflect the refactored definition of a listing and improve the definition of corporate bond.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20191201/Securities/Debt/Bonds.rdf version of this ontology was
      revised to eliminate duplication of concepts in LCC and eliminate a redundant superclass from RegularCouponSchedule.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200401/Securities/Debt/Bonds.rdf version of this ontology was
      revised to eliminate a duplicate 'isBasedOn' property and replace it with the property of the same name in the debt
      ontology, to revise the inheritance hierarchy for bond conversion terms to reflect changes in the representation of
      redemption more generally, to reflect the move of redemption provision from debt to financial instruments, and eliminate
      circular and ambiguous definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200901/Securities/Debt/Bonds.rdf version of this ontology was
      revised to eliminate false positives in hygiene tests due to concept names containing words, such as 'and', which might
      indicate that the concept actually reflects more than one thing, including distinguishing zero coupon from original
      issue discount bonds, and replace the use of call price and put price, which are overly constrained, with monetary price.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210301/Securities/Debt/Bonds.rdf version of this ontology was
      revised to eliminate references to the exercise conventions ontology, which are not needed for bonds.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210501/Securities/Debt/Bonds.rdf version of this ontology was
      revised to allow for variation in index-linked bonds, such as those whose interest payments vary with an index in addition
      to those that have a variable principal linked to an index and to make a number of corrections to the class hierarchy.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20211001/Securities/Debt/Bonds.rdf version of this ontology was
      revised to incorporate the concept of a credit agreement repaid at maturity, which is a component assumed to be part
      of the definition of a bond, and to add an explanatory note to the definition of Treasury Bill.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220201/Securities/Debt/Bonds.rdf version of this ontology was
      revised to address text formatting hygiene issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220801/Debt/Bonds.rdf version of the ontology was modified
      to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Debt/Bonds.rdf version of this ontology was modified
      to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating
      redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Debt/Bonds.rdf version of the ontology was modified
      to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons)
      v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20231201/Debt/Bonds.rdf version of the ontology was modified
      to replace concepts from additional FIBO FND ontologies with their counterparts added to the Commons Ontology Library
      (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240101/Debt/Bonds.rdf version of this ontology was modified
      to add an optional restriction on bond for 'has series' (FBC-322).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240101/Debt/Bonds.rdf version of this ontology was modified
      to move details regarding step schedules to the debt instruments ontology for broader use and deprecate the use of a
      'coupon' schedule in favor of interest payment schedule, which is the more modern terminology, aligning with other uses
      of the related terms in FIBO (FBC-317).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20241001/Debt/Bonds.rdf version of the ontology was modified
      to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250301/Debt/Bonds.rdf version of the ontology was modified
      to align the definition of 'bond with warrant' with the CFI definition (SEC-207).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250701/Debt/Bonds.rdf version of the ontology was modified
      to align the definition of 'bond with warrant' with the CFI definition (SEC-207).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/
  - concept: /concepts/fibo/BE/Trusts/Trusts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/
  - concept: /concepts/fibo/FND/Agreements/Agreements.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
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
  - concept: /concepts/fibo/FND/Parties/Parties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/
  - concept: /concepts/fibo/IND/Indicators/Indicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/
  - concept: /concepts/fibo/IND/InterestRates/InterestRates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/20251201/Debt/Bonds/
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: Bonds Ontology
type: Ontology Definition
---

# Bonds Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/>

## Relationships

- **Related to**: [FunctionalEntities](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md)
- **Related to**: [GovernmentEntities](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md)
- **Related to**: [CorporateBodies](/concepts/fibo/BE/LegalEntities/CorporateBodies.md)
- **Related to**: [Trusts](/concepts/fibo/BE/Trusts/Trusts.md)
- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [ISO4217-CurrencyCodes](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes.md)
- **Related to**: [Agreements](/concepts/fibo/FND/Agreements/Agreements.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [BusinessDates](/concepts/fibo/FND/DatesAndTimes/BusinessDates.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Occurrences](/concepts/fibo/FND/DatesAndTimes/Occurrences.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [Parties](/concepts/fibo/FND/Parties/Parties.md)
- **Related to**: [PaymentsAndSchedules](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [EconomicIndicators](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators.md)
- **Related to**: [Indicators](/concepts/fibo/IND/Indicators/Indicators.md)
- **Related to**: [InterestRates](/concepts/fibo/IND/InterestRates/InterestRates.md)
- **Related to**: [DebtInstruments](/concepts/fibo/SEC/Debt/DebtInstruments.md)
- **Related to**: [TradedShortTermDebt](/concepts/fibo/SEC/Debt/TradedShortTermDebt.md)
- **Related to**: [EquityInstruments](/concepts/fibo/SEC/Equities/EquityInstruments.md)
- **Related to**: [SecuritiesIssuance](/concepts/fibo/SEC/Securities/SecuritiesIssuance.md)
- **Related to**: [SecuritiesListings](/concepts/fibo/SEC/Securities/SecuritiesListings.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [RegistrationAuthorities](<https://www.omg.org/spec/Commons/RegistrationAuthorities/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [Bonds](<https://spec.edmcouncil.org/fibo/ontology/SEC/20251201/Debt/Bonds/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines the basic concept of a bond and a number of bond variants including convertible and callable bonds. Medium term notes (MTNs) and debentures are also defined.
- **license**: Copyright (c) 2016-2025 EDM Council, Inc. Copyright (c) 2018-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Bonds Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190901/Securities/Debt/Bonds.rdf version of this ontology was revised to reflect the refactored definition of a listing and improve the definition of corporate bond.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20191201/Securities/Debt/Bonds.rdf version of this ontology was revised to eliminate duplication of concepts in LCC and eliminate a redundant superclass from RegularCouponSchedule.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200401/Securities/Debt/Bonds.rdf version of this ontology was revised to eliminate a duplicate 'isBasedOn' property and replace it with the property of the same name in the debt ontology, to revise the inheritance hierarchy for bond conversion terms to reflect changes in the representation of redemption more generally, to reflect the move of redemption provision from debt to financial instruments, and eliminate circular and ambiguous definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200901/Securities/Debt/Bonds.rdf version of this ontology was revised to eliminate false positives in hygiene tests due to concept names containing words, such as 'and', which might indicate that the concept actually reflects more than one thing, including distinguishing zero coupon from original issue discount bonds, and replace the use of call price and put price, which are overly constrained, with monetary price.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210301/Securities/Debt/Bonds.rdf version of this ontology was revised to eliminate references to the exercise conventions ontology, which are not needed for bonds.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210501/Securities/Debt/Bonds.rdf version of this ontology was revised to allow for variation in index-linked bonds, such as those whose interest payments vary with an index in addition to those that have a variable principal linked to an index and to make a number of corrections to the class hierarchy.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20211001/Securities/Debt/Bonds.rdf version of this ontology was revised to incorporate the concept of a credit agreement repaid at maturity, which is a component assumed to be part of the definition of a bond, and to add an explanatory note to the definition of Treasury Bill.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220201/Securities/Debt/Bonds.rdf version of this ontology was revised to address text formatting hygiene issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220801/Debt/Bonds.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Debt/Bonds.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Debt/Bonds.rdf version of the ontology was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20231201/Debt/Bonds.rdf version of the ontology was modified to replace concepts from additional FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240101/Debt/Bonds.rdf version of this ontology was modified to add an optional restriction on bond for 'has series' (FBC-322).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240101/Debt/Bonds.rdf version of this ontology was modified to move details regarding step schedules to the debt instruments ontology for broader use and deprecate the use of a 'coupon' schedule in favor of interest payment schedule, which is the more modern terminology, aligning with other uses of the related terms in FIBO (FBC-317).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20241001/Debt/Bonds.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250301/Debt/Bonds.rdf version of the ontology was modified to align the definition of 'bond with warrant' with the CFI definition (SEC-207).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250701/Debt/Bonds.rdf version of the ontology was modified to align the definition of 'bond with warrant' with the CFI definition (SEC-207).
- **copyright**: Copyright (c) 2016-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2018-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
