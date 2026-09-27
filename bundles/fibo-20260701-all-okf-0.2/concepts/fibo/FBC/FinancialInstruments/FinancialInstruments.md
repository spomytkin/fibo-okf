---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines the fundamental concepts for financial instruments in general, providing the high-level hooks
      for build-out in more detail in the relevant domain areas. These include, but are not limited to, equities, options,
      debt instruments, and so forth, some of which may be negotiable.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2015-2025 EDM Council, Inc.\nCopyright (c) 2015-2025 Object Management Group, Inc.\n\nPermission\
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
    value: Financial Instruments Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to reflect issue resolutions detailed in the FIBO FBC 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified for the FIBO 2.0 RFC, including minor bug fixes.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified as a part of organizational hierarchy simplification, to add maturity-related properties,
      and to add exempt security.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190401/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to correct the label on packaged financial product.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190701/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to change the restriction on financial instrument identifier from some values to min 0, to
      allow for cases when an instrument identifier identifies a listing, eliminate duplication of concepts in LCC, and simplify
      addresses.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200301/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to move redemption provision from debt to financial instruments, given that it is a broader
      concept needed for equities.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200801/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to add a property indicating the currency that an instrument is issued in, simplify the contract
      party hierarchy and add properties relating financial instruments to shareholders.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20201201/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to incorporate a hasMaturityDate property given that it can apply to debt instruments and
      preferred shares, as well as to other financial instruments, eliminated the redundant hasScheduledMaturityDate property,
      cleaned up circular definitions, eliminated the property 'mayBeTradedIn', which was only used in one place and was redundant
      with the concept of a ListedSecurity / Listing in SEC, added a synonym and additional explanatory note to packaged financial
      product, added hasNominalValue, which was a gap, and added back restrictions on debt instrument for hasMaturityDate
      (min 0 to account for rare instruments (e.g., consul) that have no maturity date), hasDurationToMaturity and hasTimeToMaturity.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210301/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to add the concept of a spot contract and clarify the definition of time to maturity, as
      well as add a property for days to maturity.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210701/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to make Entitlement a subclass of Security and fix spelling.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211201/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to move properties and restrictions related to maturity to the Debt ontology, on credit agreement,
      and deprecate them here as well as to restructure the relationship between the two ontologies.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220101/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to eliminate deprecated content, i.e., properties related to maturity that are now in the
      Debt ontology and revise the definition of a securities transaction identifier to align with ISO 23897.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220601/FinancialInstruments/FinancialInstruments/ version of
      this ontology was modified to address dead links and text formatting issues uncovered by hygiene testing.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FinancialInstruments/FinancialInstruments.rdf version
      of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary and to add a new property, has underlier, which is needed in both securities and derivatives.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FinancialInstruments/FinancialInstruments.rdf version
      of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FinancialInstruments/FinancialInstruments.rdf version
      of this ontology was modified to augment the definition of a commodity contract with a quantity and price as of contract
      execution.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230501/FinancialInstruments/FinancialInstruments.rdf version
      of the ontology was modified to eliminate deprecations that are more than 6 months old.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231101/FinancialInstruments/FinancialInstruments.rdf version
      of this ontology was modified to tease out the distinction between the nominal and notional amount, which were confused
      (DER-127)and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231201/FinancialInstruments/FinancialInstruments.rdf version
      of this ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library
      (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FinancialInstruments/FinancialInstruments.rdf version
      of this ontology was modified to augment the definition of currency instrument with the notions of buying and selling
      currencies as well as the source(s) for anticipated rates (DER-143).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FinancialInstruments/FinancialInstruments.rdf version
      of this ontology was modified to refine the definition of issuer (FBC-284).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240801/FinancialInstruments/FinancialInstruments.rdf version
      of this ontology was modified to loosen the constraint on financial instrument with respect to having exactly 1 currency
      (DER-113), and to move the definition of promissory note from debt to financial instruments (LOAN-168).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20241001/FinancialInstruments/FinancialInstruments.rdf version
      of this ontology was modified to add a restriction related to initial exchange date.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20241201/FinancialInstruments/FinancialInstruments.rdf version
      of this ontology was modified to unify and simplify the notion of an underlier across FIBO (DER-112).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250201/FinancialInstruments/FinancialInstruments.rdf version
      of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library
      (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FinancialInstruments/FinancialInstruments.rdf version
      of the ontology was modified to add calculation agent, which may appear at a higher level than derivatives (DER-55).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250501/FinancialInstruments/FinancialInstruments.rdf version
      of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396) and
      to reclassify entitlement under financial instrument, since not all entitlements are securities.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250901/FinancialInstruments/FinancialInstruments.rdf version
      of the ontology was modified to eliminate long-time deprecated elements (FND-399).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/Arrangements/IdentifiersAndIndices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/
  - concept: /concepts/fibo/FND/Places/Addresses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: Financial Instruments Ontology
type: Ontology Definition
---

# Financial Instruments Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/>

## Relationships

- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [CorporateOwnership](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md)
- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [IdentifiersAndIndices](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices.md)
- **Related to**: [Addresses](/concepts/fibo/FND/Places/Addresses.md)
- **Related to**: [ProductsAndServices](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [FinancialInstruments](<https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/FinancialInstruments/FinancialInstruments/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines the fundamental concepts for financial instruments in general, providing the high-level hooks for build-out in more detail in the relevant domain areas. These include, but are not limited to, equities, options, debt instruments, and so forth, some of which may be negotiable.
- **license**: Copyright (c) 2015-2025 EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Financial Instruments Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to reflect issue resolutions detailed in the FIBO FBC 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/FinancialInstruments/FinancialInstruments/ version of this ontology was modified for the FIBO 2.0 RFC, including minor bug fixes.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FinancialInstruments/FinancialInstruments/ version of this ontology was modified as a part of organizational hierarchy simplification, to add maturity-related properties, and to add exempt security.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190401/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to correct the label on packaged financial product.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190701/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to change the restriction on financial instrument identifier from some values to min 0, to allow for cases when an instrument identifier identifies a listing, eliminate duplication of concepts in LCC, and simplify addresses.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200301/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to move redemption provision from debt to financial instruments, given that it is a broader concept needed for equities.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200801/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to add a property indicating the currency that an instrument is issued in, simplify the contract party hierarchy and add properties relating financial instruments to shareholders.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20201201/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to incorporate a hasMaturityDate property given that it can apply to debt instruments and preferred shares, as well as to other financial instruments, eliminated the redundant hasScheduledMaturityDate property, cleaned up circular definitions, eliminated the property 'mayBeTradedIn', which was only used in one place and was redundant with the concept of a ListedSecurity / Listing in SEC, added a synonym and additional explanatory note to packaged financial product, added hasNominalValue, which was a gap, and added back restrictions on debt instrument for hasMaturityDate (min 0 to account for rare instruments (e.g., consul) that have no maturity date), hasDurationToMaturity and hasTimeToMaturity.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210301/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to add the concept of a spot contract and clarify the definition of time to maturity, as well as add a property for days to maturity.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210701/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to make Entitlement a subclass of Security and fix spelling.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211201/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to move properties and restrictions related to maturity to the Debt ontology, on credit agreement, and deprecate them here as well as to restructure the relationship between the two ontologies.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220101/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to eliminate deprecated content, i.e., properties related to maturity that are now in the Debt ontology and revise the definition of a securities transaction identifier to align with ISO 23897.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220601/FinancialInstruments/FinancialInstruments/ version of this ontology was modified to address dead links and text formatting issues uncovered by hygiene testing.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FinancialInstruments/FinancialInstruments.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary and to add a new property, has underlier, which is needed in both securities and derivatives.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FinancialInstruments/FinancialInstruments.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FinancialInstruments/FinancialInstruments.rdf version of this ontology was modified to augment the definition of a commodity contract with a quantity and price as of contract execution.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230501/FinancialInstruments/FinancialInstruments.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231101/FinancialInstruments/FinancialInstruments.rdf version of this ontology was modified to tease out the distinction between the nominal and notional amount, which were confused (DER-127)and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231201/FinancialInstruments/FinancialInstruments.rdf version of this ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FinancialInstruments/FinancialInstruments.rdf version of this ontology was modified to augment the definition of currency instrument with the notions of buying and selling currencies as well as the source(s) for anticipated rates (DER-143).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FinancialInstruments/FinancialInstruments.rdf version of this ontology was modified to refine the definition of issuer (FBC-284).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240801/FinancialInstruments/FinancialInstruments.rdf version of this ontology was modified to loosen the constraint on financial instrument with respect to having exactly 1 currency (DER-113), and to move the definition of promissory note from debt to financial instruments (LOAN-168).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20241001/FinancialInstruments/FinancialInstruments.rdf version of this ontology was modified to add a restriction related to initial exchange date.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20241201/FinancialInstruments/FinancialInstruments.rdf version of this ontology was modified to unify and simplify the notion of an underlier across FIBO (DER-112).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250201/FinancialInstruments/FinancialInstruments.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FinancialInstruments/FinancialInstruments.rdf version of the ontology was modified to add calculation agent, which may appear at a higher level than derivatives (DER-55).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250501/FinancialInstruments/FinancialInstruments.rdf version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396) and to reclassify entitlement under financial instrument, since not all entitlements are securities.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250901/FinancialInstruments/FinancialInstruments.rdf version of the ontology was modified to eliminate long-time deprecated elements (FND-399).
- **copyright**: Copyright (c) 2015-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
