---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides basic concepts related to accounts, including internal accounts such as ledger accounts
      as well as accounts managed for external parties, that are commonly used by financial services providers.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2015-2025 Object Management Group,\
      \ Inc.\n\t\t\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\t\
      See https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Clients and Accounts Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised per the FIBO 2.0 RFC with respect to the definitions for accounts and account identifiers,
      such as BBAN and IBAN identifiers, including but not limited to bank accounts.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/ProductsAndServices/ClientsAndAccounts/ version of this
      ontology was modified to support the addition of maturity-related properties to financial instruments.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20181101/ProductsAndServices/ClientsAndAccounts/ version of this
      ontology was modified to replace hasDefinition with isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190701/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to eliminate the disjointness between a deposit account and investment account to allow for
      certain portfolio management accounts that have characteristics of both.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20191201/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to add definitions for balance, fee, general ledger, ledger account, income and related properties,
      revise definitions to be ISO 704 compliant, and eliminate duplication with concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200201/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to add definitions for transaction records, which are needed to represent statements of various
      sorts, to add the concept of an account statement, and to clean up and augment definitions related to accounts, account
      holders, etc. as required for the purpose of representing credit card accounts.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200901/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to generalize the definition of customer account and eliminate ambiguity in others.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20201201/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to change a property on CertificateOfDeposit from has notional amount to has nominal value
      for the sake of consistency.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210301/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to rename ownership related properties for consistent alignment with the ownership situational
      pattern.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210401/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to reflect the move of certain organization-specific concepts from BE to FND, to incorporate
      the concept of a composite identifier for BBAN and IBAN definition, loosen the definition of bank identifier with respect
      to the nature of the functional entity it identifies, and clarify the identifier hierarchy and fix spelling.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211201/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to reflect the move of hasTerm from FinancialInstruments to Contracts and add the definition
      of a lending officer.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220101/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to link a credit agreement with an account and loosen transaction-related constraints such
      that the notion of a transaction can be applied to credit agreements generally.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220301/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to clean up dead links and address text formatting hygiene issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/ProductsAndServices/ClientsAndAccounts.rdf version of
      the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/ProductsAndServices/ClientsAndAccounts.rdf version of
      this ontology was revised to clarify and extend definitions related to non-bank financial institutions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230401/ProductsAndServices/ClientsAndAccounts.rdf version of
      the ontology was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the
      Commons Ontology Library (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231201/ProductsAndServices/ClientsAndAccounts.rdf version of
      the ontology was modified to replace additional concepts from several FIBO FND ontologies with their counterparts added
      to the Commons Ontology Library (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/ProductsAndServices/ClientsAndAccounts.rdf version of
      the ontology was modified to eliminate deprecated elements that were deprecated more than six months ago (FND-386).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20241101/ProductsAndServices/ClientsAndAccounts.rdf version of
      the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/ProductsAndServices/ClientsAndAccounts.rdf version of
      the ontology was modified to use new constructs from the Commons 1.3 Business Authorizations ontology (FND-401).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/ProductsAndServices/ClientsAndAccounts.rdf version of
      the ontology was modified to add the concept of a chart of accounts (FND-398).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/ProductsAndServices/ClientsAndAccounts.rdf version of
      the ontology was modified to reflect migration of concepts from accounting equity to ownership in FND (FND-409), to
      reflect definition refinement in financial products and services (SEC-219), and to replace references to the now deprecated
      hasTag property in Relations with its equivalent in OMG Commons (FND-412).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/ProductsAndServices/ClientsAndAccounts/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/Arrangements/Documents.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
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
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/TextDatatype/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: Clients and Accounts Ontology
type: Ontology Definition
---

# Clients and Accounts Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/>

## Relationships

- **Related to**: [FunctionalEntities](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md)
- **Related to**: [Executives](/concepts/fibo/BE/OwnershipAndControl/Executives.md)
- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [BusinessRegistries](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Documents](/concepts/fibo/FND/Arrangements/Documents.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Occurrences](/concepts/fibo/FND/DatesAndTimes/Occurrences.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [ProductsAndServices](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [BusinessAuthorizations](<https://www.omg.org/spec/Commons/BusinessAuthorizations/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [CodesAndCodeSets](<https://www.omg.org/spec/Commons/CodesAndCodeSets/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [ContextualIdentifiers](<https://www.omg.org/spec/Commons/ContextualIdentifiers/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RegistrationAuthorities](<https://www.omg.org/spec/Commons/RegistrationAuthorities/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [TextDatatype](<https://www.omg.org/spec/Commons/TextDatatype/>)
- **Related to**: [ClientsAndAccounts](<https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/ProductsAndServices/ClientsAndAccounts/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides basic concepts related to accounts, including internal accounts such as ledger accounts as well as accounts managed for external parties, that are commonly used by financial services providers.
- **license**: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Clients and Accounts Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised per the FIBO 2.0 RFC with respect to the definitions for accounts and account identifiers, such as BBAN and IBAN identifiers, including but not limited to bank accounts.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/ProductsAndServices/ClientsAndAccounts/ version of this ontology was modified to support the addition of maturity-related properties to financial instruments.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20181101/ProductsAndServices/ClientsAndAccounts/ version of this ontology was modified to replace hasDefinition with isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190701/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to eliminate the disjointness between a deposit account and investment account to allow for certain portfolio management accounts that have characteristics of both.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20191201/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to add definitions for balance, fee, general ledger, ledger account, income and related properties, revise definitions to be ISO 704 compliant, and eliminate duplication with concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200201/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to add definitions for transaction records, which are needed to represent statements of various sorts, to add the concept of an account statement, and to clean up and augment definitions related to accounts, account holders, etc. as required for the purpose of representing credit card accounts.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200901/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to generalize the definition of customer account and eliminate ambiguity in others.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20201201/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to change a property on CertificateOfDeposit from has notional amount to has nominal value for the sake of consistency.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210301/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to rename ownership related properties for consistent alignment with the ownership situational pattern.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210401/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to reflect the move of certain organization-specific concepts from BE to FND, to incorporate the concept of a composite identifier for BBAN and IBAN definition, loosen the definition of bank identifier with respect to the nature of the functional entity it identifies, and clarify the identifier hierarchy and fix spelling.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211201/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to reflect the move of hasTerm from FinancialInstruments to Contracts and add the definition of a lending officer.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220101/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to link a credit agreement with an account and loosen transaction-related constraints such that the notion of a transaction can be applied to credit agreements generally.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220301/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to clean up dead links and address text formatting hygiene issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/ProductsAndServices/ClientsAndAccounts.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/ProductsAndServices/ClientsAndAccounts.rdf version of this ontology was revised to clarify and extend definitions related to non-bank financial institutions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230401/ProductsAndServices/ClientsAndAccounts.rdf version of the ontology was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231201/ProductsAndServices/ClientsAndAccounts.rdf version of the ontology was modified to replace additional concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/ProductsAndServices/ClientsAndAccounts.rdf version of the ontology was modified to eliminate deprecated elements that were deprecated more than six months ago (FND-386).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20241101/ProductsAndServices/ClientsAndAccounts.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/ProductsAndServices/ClientsAndAccounts.rdf version of the ontology was modified to use new constructs from the Commons 1.3 Business Authorizations ontology (FND-401).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/ProductsAndServices/ClientsAndAccounts.rdf version of the ontology was modified to add the concept of a chart of accounts (FND-398).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/ProductsAndServices/ClientsAndAccounts.rdf version of the ontology was modified to reflect migration of concepts from accounting equity to ownership in FND (FND-409), to reflect definition refinement in financial products and services (SEC-219), and to replace references to the now deprecated hasTag property in Relations with its equivalent in OMG Commons (FND-412).
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
