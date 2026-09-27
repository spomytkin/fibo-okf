---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: Core terms are those fundamental to all equity instruments. This ontology also distinguishes between privately
      held and publicly traded equity instruments, and defines a number of related concepts, such as voting rights.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2018-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\nSee https://opensource.org/licenses/MIT."
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Equity Instruments Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20180801/Equities/EquityInstruments.rdf version of this ontology
      was revised to replace 'publicly-traded share' with 'exchange-specific share', which is the more commonly used designation
      and corresponds better with the intended semantics of this concept, to merge in concepts that were formerly in a separate
      ShareTerms ontology, and eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190901/Equities/EquityInstruments.rdf version of this ontology
      was revised to refine the definition of listed share, update definitions to remove leading articles, add missing properties
      and restrictions, revise the definition of dividend.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20191201/Equities/EquityInstruments.rdf version of this ontology
      was revised to refine the definition of share to include a restriction for hasSharesOutstanding, eliminate duplication
      of concepts in LCC, and add the concept of an equity issuer.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200301/Equities/EquityInstruments.rdf version of this ontology
      was revised to incorporate additional features required to map the CFI classification scheme to equity instruments,
      including features specific to preferred shares.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200801/Equities/EquityInstruments.rdf version of this ontology
      was revised to incorporate a property allowing representation of the share class, streamline the representation of voting
      rights and payment form, clean up ambiguous definitions, and eliminate redundant restrictions related to security form.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20201201/Equities/EquityInstruments.rdf version of this ontology
      was revised to add concepts covering additional features of preferred shares, move the two exhaustive CFI-specific classes
      to the Equity CFI individuals ontology, rename EquityIssuer to ShareIssuer to be clearer about the intent, and add the
      concept of a price per share.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210301/Equities/EquityInstruments.rdf version of this ontology
      was revised to rename ownership related properties for consistent alignment with the ownership situational pattern and
      to move properties / restrictions that define how many shares have been issued from the issuer to the share.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210601/Equities/EquityInstruments.rdf version of this ontology
      was revised to revise the definition of dividend to explicitly state that it reflects the announced commitment of a
      specific dividend rather than a more general policy.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210701/Equities/EquityInstruments.rdf version of this ontology
      was revised to reflect the move of hasMaturityDate from FinancialInstruments to Debt in FBC and eliminate named individuals
      for specifying voting rights, which caused issues for some tools.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220101/Equities/EquityInstruments.rdf version of this ontology
      was revised to deprecate the notion of a securities restriction specific to a limited partnership fund unit, which required
      import of unnecessary content and would not be used in practice.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220301/Equities/EquityInstruments.rdf version of this ontology
      was revised to clean up deprecated elements, most of which had been in the ontology for awhile.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220501/Equities/EquityInstruments.rdf version of this ontology
      was revised to address text formatting hygiene issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220801/Equities/EquityInstruments.rdf version of this ontology
      was revised to add the notion of a VIE share and integrate dividend distribution method with strategy.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20221001/Equities/EquityInstruments.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Equities/EquityInstruments.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC),
      eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Equities/EquityInstruments.rdf version of this ontology
      was modified to clarify a restriction on perpetual preferred share, add extendible preferred share, and add the CFI
      definition for limited partnership unit.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230601/Equities/EquityInstruments.rdf version of the ontology
      was modified to eliminate deprecations that are more than 6 months old and to replace content that is now available
      in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20231201/Equities/EquityInstruments.rdf version of the ontology
      was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380) and
      to clean up details related to regular schedules (FBC-317).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240301/Equities/EquityInstruments.rdf version of the ontology
      was modified to add a link to the formula used to calculate an adjustable rate dividend and loosen some constraints
      to make the ontology more useful in cases where one could have information about a preferred share, such as having an
      adjustable rate dividend, but not necessarily having the details (SEC-138).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240401/Equities/EquityInstruments.rdf version of the ontology
      was modified to add a property for the number of available shares, required for MiFID reporting (SEC-97).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240701/Equities/EquityInstruments.rdf version of the ontology
      was modified to reconcile shareholding with equity position (BE-254), and make other small changes such as renaming
      has floating shares to has floating stock (SEC-200).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250901/Equities/EquityInstruments.rdf version of the ontology
      was modified to merge details from the old corporations ontology into corporate bodies for consistency and useability
      (BE-259).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20251001/Equities/EquityInstruments.rdf version of the ontology
      was modified to clean up older deprecations (FND-399).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20251201/Equities/EquityInstruments.rdf version of the ontology
      was modified to reflect migration of concepts from accounting equity to ownership in FND (FND-409).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/
  - concept: /concepts/fibo/BE/Partnerships/Partnerships.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Agreements/Agreements.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/Law/LegalCapacity.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
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
  - concept: /concepts/fibo/IND/InterestRates/InterestRates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/20260701/Equities/EquityInstruments/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: Equity Instruments Ontology
type: Ontology Definition
---

# Equity Instruments Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/>

## Relationships

- **Related to**: [CorporateBodies](/concepts/fibo/BE/LegalEntities/CorporateBodies.md)
- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [CorporateOwnership](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md)
- **Related to**: [Partnerships](/concepts/fibo/BE/Partnerships/Partnerships.md)
- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [InstrumentPricing](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Agreements](/concepts/fibo/FND/Agreements/Agreements.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Lifecycles](/concepts/fibo/FND/Arrangements/Lifecycles.md)
- **Related to**: [BusinessDates](/concepts/fibo/FND/DatesAndTimes/BusinessDates.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [PaymentsAndSchedules](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [InterestRates](/concepts/fibo/IND/InterestRates/InterestRates.md)
- **Related to**: [SecuritiesIssuance](/concepts/fibo/SEC/Securities/SecuritiesIssuance.md)
- **Related to**: [SecuritiesListings](/concepts/fibo/SEC/Securities/SecuritiesListings.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [EquityInstruments](<https://spec.edmcouncil.org/fibo/ontology/SEC/20260701/Equities/EquityInstruments/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: Core terms are those fundamental to all equity instruments. This ontology also distinguishes between privately held and publicly traded equity instruments, and defines a number of related concepts, such as voting rights.
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2018-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **label** (en): Equity Instruments Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20180801/Equities/EquityInstruments.rdf version of this ontology was revised to replace 'publicly-traded share' with 'exchange-specific share', which is the more commonly used designation and corresponds better with the intended semantics of this concept, to merge in concepts that were formerly in a separate ShareTerms ontology, and eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190901/Equities/EquityInstruments.rdf version of this ontology was revised to refine the definition of listed share, update definitions to remove leading articles, add missing properties and restrictions, revise the definition of dividend.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20191201/Equities/EquityInstruments.rdf version of this ontology was revised to refine the definition of share to include a restriction for hasSharesOutstanding, eliminate duplication of concepts in LCC, and add the concept of an equity issuer.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200301/Equities/EquityInstruments.rdf version of this ontology was revised to incorporate additional features required to map the CFI classification scheme to equity instruments, including features specific to preferred shares.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200801/Equities/EquityInstruments.rdf version of this ontology was revised to incorporate a property allowing representation of the share class, streamline the representation of voting rights and payment form, clean up ambiguous definitions, and eliminate redundant restrictions related to security form.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20201201/Equities/EquityInstruments.rdf version of this ontology was revised to add concepts covering additional features of preferred shares, move the two exhaustive CFI-specific classes to the Equity CFI individuals ontology, rename EquityIssuer to ShareIssuer to be clearer about the intent, and add the concept of a price per share.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210301/Equities/EquityInstruments.rdf version of this ontology was revised to rename ownership related properties for consistent alignment with the ownership situational pattern and to move properties / restrictions that define how many shares have been issued from the issuer to the share.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210601/Equities/EquityInstruments.rdf version of this ontology was revised to revise the definition of dividend to explicitly state that it reflects the announced commitment of a specific dividend rather than a more general policy.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210701/Equities/EquityInstruments.rdf version of this ontology was revised to reflect the move of hasMaturityDate from FinancialInstruments to Debt in FBC and eliminate named individuals for specifying voting rights, which caused issues for some tools.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220101/Equities/EquityInstruments.rdf version of this ontology was revised to deprecate the notion of a securities restriction specific to a limited partnership fund unit, which required import of unnecessary content and would not be used in practice.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220301/Equities/EquityInstruments.rdf version of this ontology was revised to clean up deprecated elements, most of which had been in the ontology for awhile.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220501/Equities/EquityInstruments.rdf version of this ontology was revised to address text formatting hygiene issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220801/Equities/EquityInstruments.rdf version of this ontology was revised to add the notion of a VIE share and integrate dividend distribution method with strategy.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20221001/Equities/EquityInstruments.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Equities/EquityInstruments.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Equities/EquityInstruments.rdf version of this ontology was modified to clarify a restriction on perpetual preferred share, add extendible preferred share, and add the CFI definition for limited partnership unit.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230601/Equities/EquityInstruments.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20231201/Equities/EquityInstruments.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380) and to clean up details related to regular schedules (FBC-317).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240301/Equities/EquityInstruments.rdf version of the ontology was modified to add a link to the formula used to calculate an adjustable rate dividend and loosen some constraints to make the ontology more useful in cases where one could have information about a preferred share, such as having an adjustable rate dividend, but not necessarily having the details (SEC-138).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240401/Equities/EquityInstruments.rdf version of the ontology was modified to add a property for the number of available shares, required for MiFID reporting (SEC-97).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240701/Equities/EquityInstruments.rdf version of the ontology was modified to reconcile shareholding with equity position (BE-254), and make other small changes such as renaming has floating shares to has floating stock (SEC-200).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250901/Equities/EquityInstruments.rdf version of the ontology was modified to merge details from the old corporations ontology into corporate bodies for consistency and useability (BE-259).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20251001/Equities/EquityInstruments.rdf version of the ontology was modified to clean up older deprecations (FND-399).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20251201/Equities/EquityInstruments.rdf version of the ontology was modified to reflect migration of concepts from accounting equity to ownership in FND (FND-409).
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
