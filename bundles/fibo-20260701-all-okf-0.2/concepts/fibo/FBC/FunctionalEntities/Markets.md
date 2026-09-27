---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines the fundamental concepts for markets, exchanges, regulated markets, and multilateral trading
      facilities.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2015-2025 Object Management Group,\
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
    value: Markets Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/FunctionalEntities/Markets/ version of this ontology
      was modified to reflect issue resolutions detailed in the FIBO FBC 1.0 RTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20170201/FunctionalEntities/Markets/ version of this ontology
      was modified per the FIBO 2.0 RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/Markets/ version of this ontology
      was modified to generalize certain unions where they were no longer required and to move international registration
      authorities individuals to a separate ontology for better modularity.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190501/FunctionalEntities/Markets/ version of this ontology
      was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/FunctionalEntities/Markets/ version of this ontology
      was modified to integrated details from the redundant 'securities exchange' concept with 'exchange'.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20191201/FunctionalEntities/Markets/ version of this ontology
      was modified to eliminate duplication of concepts in LCC, simplify addresses, merge countries with locations in FND,
      and correct the declaration of the property 'operates in municipality' to be an object property.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200301/FunctionalEntities/Markets/ version of this ontology
      was modified to replace the hasTag property in Relations with the LCC equivalent on nominals.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200601/FunctionalEntities/Markets/ version of this ontology
      was modified to add the definition of an exchange participant and loosen constraints on the location in which a given
      exchange operates, given that there are cases when an exchange may operate in multiple locations.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: 'The https://spec.edmcouncil.org/fibo/ontology/FBC/20210601/FunctionalEntities/Markets/ version of this ontology
      was modified to add: ''off-market'', with synonyms of ''off-facility'' and ''off-book'', ''auction market'' for periodic
      or on-demand auction markets, ''dark pool'', and ''quote-driven market'' for those that have QUOTE or RFQ in their name
      excluding QUOTED FUNDS, and other ''alternative trading system''s; also moved ''designated contract market'' and ''swap
      execution facility'' from DER to the this ontology for use in generating proper classification of the ISO MIC codes.'
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210701/FunctionalEntities/Markets/ version of this ontology
      was modified to revise the number and nature of 'market categories' per the latest version of ISO 10383, including the
      addition of ESMA-regulated data reporting service providers and other new categories, augment the representation of
      a market to reference the legal entity that is the market, add their LEI and other details that correspond to the entity
      vs. the market and so forth.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20221201/FunctionalEntities/Markets.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FunctionalEntities/Markets.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC)
      and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FunctionalEntities/Markets.rdf version of the ontology
      was modified to eliminate deprecations that are more than 6 months old, primarily due to the change in the MIC structure
      in 2021.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231101/FunctionalEntities/Markets.rdf version of the ontology
      was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FunctionalEntities/Markets.rdf version of the ontology
      was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2
      (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/Markets.rdf version of the ontology
      was modified to reuse concepts from the Commons 1.3 sites and facilities ontology (FND-401).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/FunctionalEntities/Markets.rdf version of the ontology
      was modified to reflect migration of additional properties to Commons 1.3 (FND-412).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/FunctionalEntities/Markets/
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/
  - concept: /concepts/fibo/FND/Arrangements/Reporting.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/
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
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/SitesAndFacilities/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: Markets Ontology
type: Ontology Definition
---

# Markets Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/>

## Relationships

- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [BusinessRegistries](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [Lifecycles](/concepts/fibo/FND/Arrangements/Lifecycles.md)
- **Related to**: [Reporting](/concepts/fibo/FND/Arrangements/Reporting.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RegistrationAuthorities](<https://www.omg.org/spec/Commons/RegistrationAuthorities/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [SitesAndFacilities](<https://www.omg.org/spec/Commons/SitesAndFacilities/>)
- **Related to**: [Markets](<https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/FunctionalEntities/Markets/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines the fundamental concepts for markets, exchanges, regulated markets, and multilateral trading facilities.
- **license**: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Markets Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/FunctionalEntities/Markets/ version of this ontology was modified to reflect issue resolutions detailed in the FIBO FBC 1.0 RTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20170201/FunctionalEntities/Markets/ version of this ontology was modified per the FIBO 2.0 RFC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/Markets/ version of this ontology was modified to generalize certain unions where they were no longer required and to move international registration authorities individuals to a separate ontology for better modularity.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190501/FunctionalEntities/Markets/ version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/FunctionalEntities/Markets/ version of this ontology was modified to integrated details from the redundant 'securities exchange' concept with 'exchange'.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20191201/FunctionalEntities/Markets/ version of this ontology was modified to eliminate duplication of concepts in LCC, simplify addresses, merge countries with locations in FND, and correct the declaration of the property 'operates in municipality' to be an object property.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200301/FunctionalEntities/Markets/ version of this ontology was modified to replace the hasTag property in Relations with the LCC equivalent on nominals.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200601/FunctionalEntities/Markets/ version of this ontology was modified to add the definition of an exchange participant and loosen constraints on the location in which a given exchange operates, given that there are cases when an exchange may operate in multiple locations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210601/FunctionalEntities/Markets/ version of this ontology was modified to add: 'off-market', with synonyms of 'off-facility' and 'off-book', 'auction market' for periodic or on-demand auction markets, 'dark pool', and 'quote-driven market' for those that have QUOTE or RFQ in their name excluding QUOTED FUNDS, and other 'alternative trading system's; also moved 'designated contract market' and 'swap execution facility' from DER to the this ontology for use in generating proper classification of the ISO MIC codes.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210701/FunctionalEntities/Markets/ version of this ontology was modified to revise the number and nature of 'market categories' per the latest version of ISO 10383, including the addition of ESMA-regulated data reporting service providers and other new categories, augment the representation of a market to reference the legal entity that is the market, add their LEI and other details that correspond to the entity vs. the market and so forth.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20221201/FunctionalEntities/Markets.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FunctionalEntities/Markets.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FunctionalEntities/Markets.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old, primarily due to the change in the MIC structure in 2021.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231101/FunctionalEntities/Markets.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FunctionalEntities/Markets.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/Markets.rdf version of the ontology was modified to reuse concepts from the Commons 1.3 sites and facilities ontology (FND-401).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/FunctionalEntities/Markets.rdf version of the ontology was modified to reflect migration of additional properties to Commons 1.3 (FND-412).
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
