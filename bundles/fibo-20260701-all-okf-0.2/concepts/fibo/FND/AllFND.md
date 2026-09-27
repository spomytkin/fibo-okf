---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: "The Foundations (FND) domain includes ontologies that define general purpose concepts required to support other\
      \ FIBO domains. These include concepts and relationships about people, organizations, places, and most importantly,\
      \ contracts that are essential to domains such as Business Entities (BE), Financial Business and Commerce (FBC), Indices\
      \ and Indicators (IND), and Securities (SEC). \n\nThe scope of the definitions provided in FND is limited to coverage\
      \ of exactly those concepts needed by other FIBO domain areas. They may be useful for other domains, such as insurance,\
      \ but are intentionally underspecified to avoid unintended consequences and thus do not provide exhaustive coverage\
      \ for any concept contained herein. However, Foundations is designed for growth over time. The expectation is that as\
      \ additional foundational knowledge is needed to define concepts in other FIBO domain areas, additional ontologies and/or\
      \ concepts will be integrated into Foundations as required."
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/issued
    value: '2017-12-28T18:00:00'
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2017-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2017-2025 Object Management Group,\
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
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/modified
    value: '2026-07-07T18:00:00'
  - predicate: http://purl.org/dc/terms/title
    value: FIBO FND Domain
  - predicate: http://purl.org/dc/terms/title
    value: Financial Industry Business Ontology (FIBO) Foundations (FND) Domain
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: all FND
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    value: https://spec.edmcouncil.org/fibo/
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/AllFND.rdf version of this ontology was modified to
      incorporate the recently released assessments and ratings ontologies.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190601/AllFND.rdf version of this ontology was modified to
      eliminate the unused legitimate organizations ontology, thereby simplifying the overal organization hierarchy, eliminate
      duplication with LCC, and merge countries with locations.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/AllFND.rdf version of this ontology was modified to
      merge goals with objectives.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20201101/AllFND.rdf version of the ontology was modified to use
      the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary
      and to eliminate unnecessary imports statements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/AllFND.rdf version of the ontology was modified to add
      an ontology for real property (LOAN-168).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20241001/AllFND.rdf version of the ontology was modified to eliminate
      the now redundant Roles and Quantities and Units ontologies (FND-386).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/AllFND.rdf version of the ontology was modified to eliminate
      the now redundant Jurisdictions and Organizations ontologies (FND-399) and to reuse concepts from the Commons 1.3 sites
      and facilities ontology (FND-401).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20251201/AllFND.rdf version of the ontology was modified to eliminate
      the now redundant Agents ontology (FND-411) and to reflect migration of concepts from accounting equity to ownership
      in FND (FND-409).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2017-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2017-2026 EDM Association dba EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The 'all' FND ontology is provided for convenience for FIBO users. It imports all of the Production (Released)
      ontologies that comprise the FIBO Foundations (FND) domain, and can be loaded directly in tools such as Protege with
      the expectation that all of the accompanying content will be loaded.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20260701/AllFND/
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
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AllFND/
sources:
- id: fibo-source-90d8b7ff52
  resource: references/fibo/FND/AllFND.rdf
  sha256: 90d8b7ff527a736a1b76d2b7175a2b8f46fc8b0bf6375dcd6575a0867e35429e
  title: FIBO source FND/AllFND.rdf
title: all FND
type: Ontology Definition
---

# all FND

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AllFND/>

## Relationships

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
- **Related to**: [RealProperty](/concepts/fibo/FND/Places/RealProperty.md)
- **Related to**: [VirtualPlaces](/concepts/fibo/FND/Places/VirtualPlaces.md)
- **Related to**: [PaymentsAndSchedules](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules.md)
- **Related to**: [ProductsAndServices](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [Analytics](/concepts/fibo/FND/Utilities/Analytics.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [AllFND](<https://spec.edmcouncil.org/fibo/ontology/FND/20260701/AllFND/>)

## Annotations

- **abstract**: The Foundations (FND) domain includes ontologies that define general purpose concepts required to support other FIBO domains. These include concepts and relationships about people, organizations, places, and most importantly, contracts that are essential to domains such as Business Entities (BE), Financial Business and Commerce (FBC), Indices and Indicators (IND), and Securities (SEC).   The scope of the definitions provided in FND is limited to coverage of exactly those concepts needed by other FIBO domain areas. They may be useful for other domains, such as insurance, but are intentionally underspecified to avoid unintended consequences and thus do not provide exhaustive coverage for any concept contained herein. However, Foundations is designed for growth over time. The expectation is that as additional foundational knowledge is needed to define concepts in other FIBO domain areas, additional ontologies and/or concepts will be integrated into Foundations as required.
- **issued**: 2017-12-28T18:00:00
- **license**: Copyright (c) 2017-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2017-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **modified**: 2026-07-07T18:00:00
- **title**: FIBO FND Domain
- **title**: Financial Industry Business Ontology (FIBO) Foundations (FND) Domain
- **label**: all FND
- **seeAlso**: https://spec.edmcouncil.org/fibo/
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/AllFND.rdf version of this ontology was modified to incorporate the recently released assessments and ratings ontologies.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190601/AllFND.rdf version of this ontology was modified to eliminate the unused legitimate organizations ontology, thereby simplifying the overal organization hierarchy, eliminate duplication with LCC, and merge countries with locations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/AllFND.rdf version of this ontology was modified to merge goals with objectives.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20201101/AllFND.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary and to eliminate unnecessary imports statements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/AllFND.rdf version of the ontology was modified to add an ontology for real property (LOAN-168).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20241001/AllFND.rdf version of the ontology was modified to eliminate the now redundant Roles and Quantities and Units ontologies (FND-386).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/AllFND.rdf version of the ontology was modified to eliminate the now redundant Jurisdictions and Organizations ontologies (FND-399) and to reuse concepts from the Commons 1.3 sites and facilities ontology (FND-401).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20251201/AllFND.rdf version of the ontology was modified to eliminate the now redundant Agents ontology (FND-411) and to reflect migration of concepts from accounting equity to ownership in FND (FND-409).
- **copyright**: Copyright (c) 2017-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2017-2026 EDM Association dba EDM Council, Inc.
- **explanatoryNote**: The 'all' FND ontology is provided for convenience for FIBO users. It imports all of the Production (Released) ontologies that comprise the FIBO Foundations (FND) domain, and can be loaded directly in tools such as Protege with the expectation that all of the accompanying content will be loaded.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
