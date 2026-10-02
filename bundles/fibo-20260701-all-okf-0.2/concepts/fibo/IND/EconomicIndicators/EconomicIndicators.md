---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides the parameters which make up the various types of market economic indicators, along with
      basic facts about these such as the economies or countries they apply to.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2014-2025 EDM Council, Inc.\nCopyright (c) 2014-2025 Object Management Group, Inc.\n\nPermission\
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
    value: Economic Indicators Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20140601/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified per the issue resolutions identified in the FIBO IND 1.0 FTF 1 report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20150501/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified per the issue resolutions identified in the FIBO IND 1.0 FTF 3 report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20160801/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified per the FIBO 2.0 RFC. Primary changes include the addition of a number of statistical measures
      (mean, total, etc.) and their use in existing and new indicators, and the addition of several more economic indicators.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20180801/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to use natural person rather than legally capable person.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20181101/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to use hasCoverageArea rather than appliesTo in the restriction on an economic indicator
      relating it to a statistical area, to reflect use of actualExpression as an annotation rather than datatype property,
      and to migrate the general statistics concepts to FND (deprecated herein).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20190501/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20190901/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to eliminate duplicatation with concepts in LCC and merge countries with locations in FND.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20200301/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to reflect the change in name and definition of numeric index to numeric index value in FND.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20200401/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to add definitions for alternative unemployment calculations and correct a circular property
      definition.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20200901/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to eliminate references to external dictionary sites that no longer resolve, added a synonym
      to fixed basket and eliminated the restriction with respect to date period, which is not the primary concern of a fixed
      basket, revised the name of the 'goods or services population' to 'goods population' to eliminate a hygiene issue and
      reflect the synonym of 'basket of goods', and merged the statistical information publisher class from economic indicator
      publishers into this ontology.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/2021001/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to fix spelling errors.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20210301/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to eliminate the restriction on economic indicator (and its subclasses) that it has an indicator
      value - the restriction should be on the quantity value such that the value refers to the indicator it represents, and
      to revise the definition of civilian non-institutional population to correctly represent civilian non-institutional
      person (added).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20211201/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to address text formatting hygiene issues and clean up external links.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20220801/EconomicIndicators/EconomicIndicators.rdf version of
      the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20230201/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20230301/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1
      (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20231201/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20240101/EconomicIndicators/EconomicIndicators.rdf version of
      this ontology was modified to eliminate punning in the use of several indicators, eliminate 'obsolete' restrictions
      through refinement, and normalize certain definitions to be ISO 704 compliant (GitHub-2038 and GitHub-2028).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20240901/EconomicIndicators/EconomicIndicators.rdf version of
      the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20250301/EconomicIndicators/EconomicIndicators.rdf version of
      the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/AgentsAndPeople/People.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/
  - concept: /concepts/fibo/FND/Arrangements/Documents.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/
  - concept: /concepts/fibo/FND/Places/Addresses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/
  - concept: /concepts/fibo/FND/Utilities/Analytics.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/20250701/EconomicIndicators/EconomicIndicators/
  - concept: /concepts/fibo/IND/Indicators/Indicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/
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
    resource: https://www.omg.org/spec/Commons/Documents/
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
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: Economic Indicators Ontology
type: Ontology Definition
---

# Economic Indicators Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/>

## Relationships

- **Related to**: [FunctionalEntities](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md)
- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [GovernmentEntities](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md)
- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [People](/concepts/fibo/FND/AgentsAndPeople/People.md)
- **Related to**: [ClassificationSchemes](/concepts/fibo/FND/Arrangements/ClassificationSchemes.md)
- **Related to**: [Documents](/concepts/fibo/FND/Arrangements/Documents.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Occurrences](/concepts/fibo/FND/DatesAndTimes/Occurrences.md)
- **Related to**: [Addresses](/concepts/fibo/FND/Places/Addresses.md)
- **Related to**: [ProductsAndServices](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md)
- **Related to**: [Analytics](/concepts/fibo/FND/Utilities/Analytics.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [Indicators](/concepts/fibo/IND/Indicators/Indicators.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [EconomicIndicators](<https://spec.edmcouncil.org/fibo/ontology/IND/20250701/EconomicIndicators/EconomicIndicators/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides the parameters which make up the various types of market economic indicators, along with basic facts about these such as the economies or countries they apply to.
- **license**: Copyright (c) 2014-2025 EDM Council, Inc. Copyright (c) 2014-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Economic Indicators Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20140601/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified per the issue resolutions identified in the FIBO IND 1.0 FTF 1 report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20150501/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified per the issue resolutions identified in the FIBO IND 1.0 FTF 3 report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20160801/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified per the FIBO 2.0 RFC. Primary changes include the addition of a number of statistical measures (mean, total, etc.) and their use in existing and new indicators, and the addition of several more economic indicators.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20180801/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to use natural person rather than legally capable person.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20181101/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to use hasCoverageArea rather than appliesTo in the restriction on an economic indicator relating it to a statistical area, to reflect use of actualExpression as an annotation rather than datatype property, and to migrate the general statistics concepts to FND (deprecated herein).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20190501/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20190901/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to eliminate duplicatation with concepts in LCC and merge countries with locations in FND.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20200301/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to reflect the change in name and definition of numeric index to numeric index value in FND.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20200401/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to add definitions for alternative unemployment calculations and correct a circular property definition.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20200901/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to eliminate references to external dictionary sites that no longer resolve, added a synonym to fixed basket and eliminated the restriction with respect to date period, which is not the primary concern of a fixed basket, revised the name of the 'goods or services population' to 'goods population' to eliminate a hygiene issue and reflect the synonym of 'basket of goods', and merged the statistical information publisher class from economic indicator publishers into this ontology.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/2021001/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to fix spelling errors.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20210301/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to eliminate the restriction on economic indicator (and its subclasses) that it has an indicator value - the restriction should be on the quantity value such that the value refers to the indicator it represents, and to revise the definition of civilian non-institutional population to correctly represent civilian non-institutional person (added).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20211201/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to address text formatting hygiene issues and clean up external links.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20220801/EconomicIndicators/EconomicIndicators.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20230201/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20230301/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20231201/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20240101/EconomicIndicators/EconomicIndicators.rdf version of this ontology was modified to eliminate punning in the use of several indicators, eliminate 'obsolete' restrictions through refinement, and normalize certain definitions to be ISO 704 compliant (GitHub-2038 and GitHub-2028).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20240901/EconomicIndicators/EconomicIndicators.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20250301/EconomicIndicators/EconomicIndicators.rdf version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
- **copyright**: Copyright (c) 2014-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2014-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
