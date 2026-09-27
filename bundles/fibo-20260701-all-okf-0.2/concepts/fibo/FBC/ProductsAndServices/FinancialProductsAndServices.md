---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts that extend the Foundations (FND) Products and Services concepts specifically for
      the financial industry, including financial product, financial service, and financial service provider.
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
    value: Financial Products and Services Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to reflect issue resolutions detailed in the FIBO FBC 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified by the FIBO 2.0 RFC, including, but not limited to, the addition of lifecycle events,
      concepts related to trade settlement, and the definition of a unique transaction identifier (UTI).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified as a part of organizational hierarchy simplification and to correct a logical inconsistency
      with respect to the representation of baskets.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190601/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to replace hasDefinition with isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190701/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to add the notion of a weighted basket, whose consituents are weighted.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20191101/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to eliminate duplication with concepts in LCC and eliminated a redundant superclass on
      FinancialServiceProvider.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200401/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to replace the property 'characterizes' with 'describes' with respect to restrictions
      on catalogs, and to correct the label on terminated trade.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200701/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to eliminate references to external dictionary sites that no longer resolve, eliminate
      circular and ambiguous definitions, and revise definitions that referenced 'face value' improperly.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210301/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to rename ownership related properties for consistent alignment with the ownership situational
      pattern, add a definition for trading strategy, and loosen the constraint on offeree for offering to be optional.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210601/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to add a property to describe the criteria for including something in a basket, if that
      criteria is known, and to point to a party that is responsible for determining that criteria.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210901/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to fix spelling errors.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211201/ProductsAndServices/FinancialProductsAndServices/ version
      of this ontology was modified to revise the definition of a unique transaction identifier to align with ISO 23897 and
      to address text formatting issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/ProductsAndServices/FinancialProductsAndServices.rdf
      version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than
      the OMG's Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/ProductsAndServices/FinancialProductsAndServices.rdf
      version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages,
      Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/ProductsAndServices/FinancialProductsAndServices.rdf
      version of this ontology was revised to augment the representation of institutions based on their definitions in the
      law, and to clarify and extend definitions related to non-bank financial institutions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230401/ProductsAndServices/FinancialProductsAndServices.rdf
      version of the ontology was modified to eliminate deprecations that are more than 6 months old and to replace content
      that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231201/ProductsAndServices/FinancialProductsAndServices.rdf
      version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology
      Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/ProductsAndServices/FinancialProductsAndServices.rdf
      version of the ontology was modified to add the concept of a contract lifecycle, as distinct from a product or trade
      lifecycle (FBC-317).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240201/ProductsAndServices/FinancialProductsAndServices.rdf
      version of the ontology was modified to eliminate a redundant restriction (GitHub-2028).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240901/ProductsAndServices/FinancialProductsAndServices.rdf
      version of the ontology was modified to eliminate certain constructs that are redundant and will never be materialized
      to reduce the number of nodes required for various contract-related constructs (FND-391).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240901/ProductsAndServices/FinancialProductsAndServices.rdf
      version of the ontology was modified to reconcile shareholding with equity position (BE-254), and to replace additional
      content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250501/ProductsAndServices/FinancialProductsAndServices.rdf
      version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250701/ProductsAndServices/FinancialProductsAndServices.rdf
      version of the ontology was modified to leverage new constructs from the Commons 1.3 Business Authorizations ontology
      (FND-401).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/ProductsAndServices/FinancialProductsAndServices.rdf
      version of the ontology was modified to make the concept of a holding more generally applicable and available in the
      ownership ontology and refine the definition of position (SEC-219).
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
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - concept: /concepts/fibo/BE/LegalEntities/LEIEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/Law/LegalCapacity.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
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
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
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
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/TextDatatype/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: Financial Products and Services Ontology
type: Ontology Definition
---

# Financial Products and Services Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/>

## Relationships

- **Related to**: [FunctionalEntities](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md)
- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [LEIEntities](/concepts/fibo/BE/LegalEntities/LEIEntities.md)
- **Related to**: [OwnershipParties](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Lifecycles](/concepts/fibo/FND/Arrangements/Lifecycles.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [ProductsAndServices](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [Analytics](/concepts/fibo/FND/Utilities/Analytics.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [BusinessAuthorizations](<https://www.omg.org/spec/Commons/BusinessAuthorizations/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [TextDatatype](<https://www.omg.org/spec/Commons/TextDatatype/>)
- **Related to**: [FinancialProductsAndServices](<https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/ProductsAndServices/FinancialProductsAndServices/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts that extend the Foundations (FND) Products and Services concepts specifically for the financial industry, including financial product, financial service, and financial service provider.
- **license**: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Financial Products and Services Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to reflect issue resolutions detailed in the FIBO FBC 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified by the FIBO 2.0 RFC, including, but not limited to, the addition of lifecycle events, concepts related to trade settlement, and the definition of a unique transaction identifier (UTI).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified as a part of organizational hierarchy simplification and to correct a logical inconsistency with respect to the representation of baskets.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190601/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to replace hasDefinition with isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190701/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to add the notion of a weighted basket, whose consituents are weighted.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20191101/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to eliminate duplication with concepts in LCC and eliminated a redundant superclass on FinancialServiceProvider.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200401/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to replace the property 'characterizes' with 'describes' with respect to restrictions on catalogs, and to correct the label on terminated trade.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200701/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to eliminate references to external dictionary sites that no longer resolve, eliminate circular and ambiguous definitions, and revise definitions that referenced 'face value' improperly.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210301/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to rename ownership related properties for consistent alignment with the ownership situational pattern, add a definition for trading strategy, and loosen the constraint on offeree for offering to be optional.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210601/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to add a property to describe the criteria for including something in a basket, if that criteria is known, and to point to a party that is responsible for determining that criteria.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210901/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to fix spelling errors.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211201/ProductsAndServices/FinancialProductsAndServices/ version of this ontology was modified to revise the definition of a unique transaction identifier to align with ISO 23897 and to address text formatting issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/ProductsAndServices/FinancialProductsAndServices.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/ProductsAndServices/FinancialProductsAndServices.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/ProductsAndServices/FinancialProductsAndServices.rdf version of this ontology was revised to augment the representation of institutions based on their definitions in the law, and to clarify and extend definitions related to non-bank financial institutions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230401/ProductsAndServices/FinancialProductsAndServices.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231201/ProductsAndServices/FinancialProductsAndServices.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/ProductsAndServices/FinancialProductsAndServices.rdf version of the ontology was modified to add the concept of a contract lifecycle, as distinct from a product or trade lifecycle (FBC-317).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240201/ProductsAndServices/FinancialProductsAndServices.rdf version of the ontology was modified to eliminate a redundant restriction (GitHub-2028).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240901/ProductsAndServices/FinancialProductsAndServices.rdf version of the ontology was modified to eliminate certain constructs that are redundant and will never be materialized to reduce the number of nodes required for various contract-related constructs (FND-391).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240901/ProductsAndServices/FinancialProductsAndServices.rdf version of the ontology was modified to reconcile shareholding with equity position (BE-254), and to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250501/ProductsAndServices/FinancialProductsAndServices.rdf version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250701/ProductsAndServices/FinancialProductsAndServices.rdf version of the ontology was modified to leverage new constructs from the Commons 1.3 Business Authorizations ontology (FND-401).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/ProductsAndServices/FinancialProductsAndServices.rdf version of the ontology was modified to make the concept of a holding more generally applicable and available in the ownership ontology and refine the definition of position (SEC-219).
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
