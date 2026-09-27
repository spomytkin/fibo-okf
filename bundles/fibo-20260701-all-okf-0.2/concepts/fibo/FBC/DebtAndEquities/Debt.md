---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts that are common to all debt instruments, such as debt, borrower, lender, debtor,
      creditor, interest, principal, and the like. It is designed to be used by various other FIBO specifications, including
      but not limited to SEC/Debt and LOAN.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2016-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
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
    value: Debt Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/DebtAndEquities/Debt/ version of this ontology was added
      to the FBC domain via the FIBO 2.0 RFC in support of several FIBO debt-oriented initiatives.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/DebtAndEquities/Debt/ version of this ontology was modified
      to use the generic statistical measures and measurements now in FND.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190501/DebtAndEquities/Debt/ version of this ontology was modified
      to add several common day count conventions used to calculate the amount of accrued interest or the present value when
      the next coupon payment is less than a full coupon period away, to support collateral agreements such as deeds of trust,
      UCC filings and the like, to add the concept of a rate reset time of day, to eliminate duplication of concepts in LCC,
      to simplify addresses, and to merge countries with locations.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200301/DebtAndEquities/Debt/ version of this ontology was modified
      to make redemption provision a child of contractual commitment and move it to financial instruments, as such provisions
      apply to preferred shares and other instruments in addition to debt.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200801/DebtAndEquities/Debt/ version of this ontology was modified
      to move the concept of an extension provision from Debt to Contracts to support representation of preferred shares and
      other extendable contracts, eliminate remaining circular definitions, integrate concepts defining credit facilities,
      and refine the concept of collateral to differentiate collateral that is real property from financial assets such as
      cash, various accounts, securities, and receivables.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210301/DebtAndEquities/Debt/ version of this ontology was modified
      to (1) add concepts including credit agreement whose principal is repaid at maturity and those whose principal is repaid
      over the course of the agreement, (2) move properties related to maturity to this ontology from FinancialInstruments
      and restructure the relationship between these two ontologies, (3) add the concept of a borrower identifier and the
      related scheme, (4) add the concept of an interest rate cap as a potential provision with respect to interest rate terms,
      and (5) clarified the definition of promissory note.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220301/DebtAndEquities/Debt/ version of this ontology was modified
      to add more detailed schedule information to support management of the various kinds of events that can impact a given
      contract as well as the concept of a revolving line of credit.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220601/DebtAndEquities/Debt/ version of this ontology was modified
      to address text formatting issues uncovered by hygiene testing.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/DebtAndEquities/Debt.rdf version of the ontology was
      modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata
      vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/DebtAndEquities/Debt.rdf version of this ontology was
      modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating
      redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/DebtAndEquities/Debt.rdf version of this ontology was
      modified to address a punning issue due to the use of hasMethod as the parent property for hasAccrualBasis that was
      not detected before the latest Commons ontologies were posted to the OMG site.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230601/DebtAndEquities/Debt.rdf version of this ontology was
      extended to incorporate the concept of a lease.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230901/DebtAndEquities/Debt.rdf version of this ontology was
      modified to add the starting point value of some collateral when it was acquired (DER-138) and to replace content that
      is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231201/DebtAndEquities/Debt.rdf version of this ontology was
      modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/DebtAndEquities/Debt.rdf version of this ontology was
      modified to incorporate certain general debt schedule terms that were previously in more specific ontologies (FBC-317).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240301/DebtAndEquities/Debt.rdf version of this ontology was
      modified to include a definition for accrued interest, needed for pricing, and correct certain process (methodology)
      issues in the class hierarchy (SEC-185).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240701/DebtAndEquities/Debt.rdf version of this ontology was
      modified to include a synonym of 'has dated date' for 'has initial interest accrual date' (FBC-322), to move the definition
      of promissory note to financial instruments and clarify the definitions of collateral and collateral agreement(LOAN-168),
      and to add a use of proceeds provision, optionally, to any credit agreement (LOAN-169).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20241101/DebtAndEquities/Debt.rdf version of this ontology was
      modified to add initial exchange date to any credit agreement.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20241201/DebtAndEquities/Debt.rdf version of this ontology was
      modified to add several properties needed to define certain credit facilities (FBC-324) and replace additional content
      that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/DebtAndEquities/Debt.rdf version of this ontology was
      modified to add the currency pertinent to a credit agreement (DER-55).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250401/DebtAndEquities/Debt.rdf version of this ontology was
      modified to add concepts related to credit enhancement agreements (DER-55a), and to eliminate certain constructs that
      are redundant and will never be materialized to reduce the number of nodes required for various contract-related constructs
      (FND-391).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250501/DebtAndEquities/Debt.rdf version of the ontology was
      modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250701/DebtAndEquities/Debt.rdf version of the ontology was
      modified to correct a typo in the definition of hasAnticipatedNumberOfPayments (GitHub-2154).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250801/DebtAndEquities/Debt.rdf version of the ontology was
      modified to eliminate long-time deprecated elements (FND-399).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/DebtAndEquities/Debt.rdf version of the ontology was
      modified to reflect migration of concepts from accounting equity to ownership in FND (FND-409).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/DebtAndEquities/Debt/
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
  - concept: /concepts/fibo/FND/Arrangements/Assessments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/
  - concept: /concepts/fibo/FND/Law/LegalCapacity.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
  - concept: /concepts/fibo/FND/Parties/Parties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/
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
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
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
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: Debt Ontology
type: Ontology Definition
---

# Debt Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/>

## Relationships

- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Agreements](/concepts/fibo/FND/Agreements/Agreements.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Assessments](/concepts/fibo/FND/Arrangements/Assessments.md)
- **Related to**: [BusinessDates](/concepts/fibo/FND/DatesAndTimes/BusinessDates.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Occurrences](/concepts/fibo/FND/DatesAndTimes/Occurrences.md)
- **Related to**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [Parties](/concepts/fibo/FND/Parties/Parties.md)
- **Related to**: [PaymentsAndSchedules](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules.md)
- **Related to**: [ProductsAndServices](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [Debt](<https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/DebtAndEquities/Debt/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts that are common to all debt instruments, such as debt, borrower, lender, debtor, creditor, interest, principal, and the like. It is designed to be used by various other FIBO specifications, including but not limited to SEC/Debt and LOAN.
- **license**: Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2016-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Debt Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/DebtAndEquities/Debt/ version of this ontology was added to the FBC domain via the FIBO 2.0 RFC in support of several FIBO debt-oriented initiatives.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/DebtAndEquities/Debt/ version of this ontology was modified to use the generic statistical measures and measurements now in FND.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190501/DebtAndEquities/Debt/ version of this ontology was modified to add several common day count conventions used to calculate the amount of accrued interest or the present value when the next coupon payment is less than a full coupon period away, to support collateral agreements such as deeds of trust, UCC filings and the like, to add the concept of a rate reset time of day, to eliminate duplication of concepts in LCC, to simplify addresses, and to merge countries with locations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200301/DebtAndEquities/Debt/ version of this ontology was modified to make redemption provision a child of contractual commitment and move it to financial instruments, as such provisions apply to preferred shares and other instruments in addition to debt.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200801/DebtAndEquities/Debt/ version of this ontology was modified to move the concept of an extension provision from Debt to Contracts to support representation of preferred shares and other extendable contracts, eliminate remaining circular definitions, integrate concepts defining credit facilities, and refine the concept of collateral to differentiate collateral that is real property from financial assets such as cash, various accounts, securities, and receivables.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210301/DebtAndEquities/Debt/ version of this ontology was modified to (1) add concepts including credit agreement whose principal is repaid at maturity and those whose principal is repaid over the course of the agreement, (2) move properties related to maturity to this ontology from FinancialInstruments and restructure the relationship between these two ontologies, (3) add the concept of a borrower identifier and the related scheme, (4) add the concept of an interest rate cap as a potential provision with respect to interest rate terms, and (5) clarified the definition of promissory note.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220301/DebtAndEquities/Debt/ version of this ontology was modified to add more detailed schedule information to support management of the various kinds of events that can impact a given contract as well as the concept of a revolving line of credit.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220601/DebtAndEquities/Debt/ version of this ontology was modified to address text formatting issues uncovered by hygiene testing.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/DebtAndEquities/Debt.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/DebtAndEquities/Debt.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/DebtAndEquities/Debt.rdf version of this ontology was modified to address a punning issue due to the use of hasMethod as the parent property for hasAccrualBasis that was not detected before the latest Commons ontologies were posted to the OMG site.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230601/DebtAndEquities/Debt.rdf version of this ontology was extended to incorporate the concept of a lease.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230901/DebtAndEquities/Debt.rdf version of this ontology was modified to add the starting point value of some collateral when it was acquired (DER-138) and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231201/DebtAndEquities/Debt.rdf version of this ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/DebtAndEquities/Debt.rdf version of this ontology was modified to incorporate certain general debt schedule terms that were previously in more specific ontologies (FBC-317).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240301/DebtAndEquities/Debt.rdf version of this ontology was modified to include a definition for accrued interest, needed for pricing, and correct certain process (methodology) issues in the class hierarchy (SEC-185).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240701/DebtAndEquities/Debt.rdf version of this ontology was modified to include a synonym of 'has dated date' for 'has initial interest accrual date' (FBC-322), to move the definition of promissory note to financial instruments and clarify the definitions of collateral and collateral agreement(LOAN-168), and to add a use of proceeds provision, optionally, to any credit agreement (LOAN-169).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20241101/DebtAndEquities/Debt.rdf version of this ontology was modified to add initial exchange date to any credit agreement.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20241201/DebtAndEquities/Debt.rdf version of this ontology was modified to add several properties needed to define certain credit facilities (FBC-324) and replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/DebtAndEquities/Debt.rdf version of this ontology was modified to add the currency pertinent to a credit agreement (DER-55).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250401/DebtAndEquities/Debt.rdf version of this ontology was modified to add concepts related to credit enhancement agreements (DER-55a), and to eliminate certain constructs that are redundant and will never be materialized to reduce the number of nodes required for various contract-related constructs (FND-391).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250501/DebtAndEquities/Debt.rdf version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250701/DebtAndEquities/Debt.rdf version of the ontology was modified to correct a typo in the definition of hasAnticipatedNumberOfPayments (GitHub-2154).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250801/DebtAndEquities/Debt.rdf version of the ontology was modified to eliminate long-time deprecated elements (FND-399).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/DebtAndEquities/Debt.rdf version of the ontology was modified to reflect migration of concepts from accounting equity to ownership in FND (FND-409).
- **copyright**: Copyright (c) 2016-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
