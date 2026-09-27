---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: "This ontology provides metadata about the FIBO Business Entities (BE) Domain, which covers defines business concepts\
      \ that are used for data governance, interoperability, and in regulatory reporting about business entities.\n\nThe business\
      \ scope of the BE ontologies covers a range of business and legal entities that are considered by financial industry\
      \ firms, regulators and other industry participants to be of relevance in the financial services domain, including:\n\
      \ - Legal entities generally\n - Corporate structure, ownership and control, including primary executive roles for businesses,\n\
      \ - Functional entities such as governments and government entities, non-governmental organizations, international organizations,\
      \ not-for-profit organization, etc.\n - Concepts specific to corporations, partnerships, private limited companies,\
      \ sole proprietorships, and trusts."
  - predicate: http://purl.org/dc/terms/contributor
    value: Adaptive, Inc.
  - predicate: http://purl.org/dc/terms/contributor
    value: Bloomberg LP
  - predicate: http://purl.org/dc/terms/contributor
    value: Citigroup
  - predicate: http://purl.org/dc/terms/contributor
    value: Credit Suisse
  - predicate: http://purl.org/dc/terms/contributor
    value: Deutsche Bank
  - predicate: http://purl.org/dc/terms/contributor
    value: EDM Council, Inc.
  - predicate: http://purl.org/dc/terms/contributor
    value: Exprentis
  - predicate: http://purl.org/dc/terms/contributor
    value: Federated Knowledge LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: Hypercube Ltd.
  - predicate: http://purl.org/dc/terms/contributor
    value: John F. Gemski
  - predicate: http://purl.org/dc/terms/contributor
    value: Nordea Bank AB
  - predicate: http://purl.org/dc/terms/contributor
    value: Office of Financial Research (US Dept of the Treasury)
  - predicate: http://purl.org/dc/terms/contributor
    value: Pinnacle Bank (Morgan Hill, California)
  - predicate: http://purl.org/dc/terms/contributor
    value: State Street Bank and Trust
  - predicate: http://purl.org/dc/terms/contributor
    value: Statistics Canada
  - predicate: http://purl.org/dc/terms/contributor
    value: Tahoe Blue Ltd
  - predicate: http://purl.org/dc/terms/contributor
    value: Thematix Partners LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: Wells Fargo
  - predicate: http://purl.org/dc/terms/contributor
    value: Working Ontologist
  - predicate: http://purl.org/dc/terms/contributor
    value: agnos.ai UK Ltd.
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/issued
    value: '2018-08-27T18:00:00'
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2018-2025 EDM Council, Inc.\nCopyright (c) 2018-2025 Object Management Group, Inc.\n\t\t\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/modified
    value: '2025-05-27T18:00:00'
  - predicate: http://purl.org/dc/terms/title
    value: EDMC Financial Industry Business Ontology (FIBO) Business Entities (BE) Domain, European Extension
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Business Entities Domain, European Extension
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    value: https://spec.edmcouncil.org/fibo/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The 'all' ontology for BE (European Extension) is provided for convenience for FIBO users.  This ontology does
      not add new assertions, but imports most of the Production (Released) ontologies that comprise the FIBO Business Entities
      (BE) domain, including all individuals for European governments and jurisdictions, and the related LCC region-specific
      ontologies. Note that the 45 ISO 3166-2 subdivision ontologies included are those defined as being part of Europe in
      the U.N. M49 Codes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20250501/AllBE-Europe/
  - concept: /concepts/fibo/BE/AllBE.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/AllBE/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EasternEuropeGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/EasternEuropeGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/NorthernEuropeGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/NorthernEuropeGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/SouthernEuropeGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/SouthernEuropeGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/UKGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/UKGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/AllBE-Europe/
sources:
- id: fibo-source-9c32fb3923
  resource: references/fibo/BE/AllBE-Europe.rdf
  sha256: 9c32fb39230b6617d9a94e3873a297da5717946958d75443a414c78e60ad49ad
  title: FIBO source BE/AllBE-Europe.rdf
title: Business Entities Domain, European Extension
type: Ontology Definition
---

# Business Entities Domain, European Extension

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/AllBE-Europe/>

## Relationships

- **Related to**: [AllBE](/concepts/fibo/BE/AllBE.md)
- **Related to**: [EUGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [EasternEuropeGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EasternEuropeGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [NorthernEuropeGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/NorthernEuropeGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [SouthernEuropeGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/SouthernEuropeGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [UKGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/UKGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [WesternEuropeGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [AllBE-Europe](<https://spec.edmcouncil.org/fibo/ontology/BE/20250501/AllBE-Europe/>)

## Annotations

- **abstract**: This ontology provides metadata about the FIBO Business Entities (BE) Domain, which covers defines business concepts that are used for data governance, interoperability, and in regulatory reporting about business entities.  The business scope of the BE ontologies covers a range of business and legal entities that are considered by financial industry firms, regulators and other industry participants to be of relevance in the financial services domain, including:  - Legal entities generally  - Corporate structure, ownership and control, including primary executive roles for businesses,  - Functional entities such as governments and government entities, non-governmental organizations, international organizations, not-for-profit organization, etc.  - Concepts specific to corporations, partnerships, private limited companies, sole proprietorships, and trusts.
- **contributor**: Adaptive, Inc.
- **contributor**: Bloomberg LP
- **contributor**: Citigroup
- **contributor**: Credit Suisse
- **contributor**: Deutsche Bank
- **contributor**: EDM Council, Inc.
- **contributor**: Exprentis
- **contributor**: Federated Knowledge LLC
- **contributor**: Hypercube Ltd.
- **contributor**: John F. Gemski
- **contributor**: Nordea Bank AB
- **contributor**: Office of Financial Research (US Dept of the Treasury)
- **contributor**: Pinnacle Bank (Morgan Hill, California)
- **contributor**: State Street Bank and Trust
- **contributor**: Statistics Canada
- **contributor**: Tahoe Blue Ltd
- **contributor**: Thematix Partners LLC
- **contributor**: Wells Fargo
- **contributor**: Working Ontologist
- **contributor**: agnos.ai UK Ltd.
- **issued**: 2018-08-27T18:00:00
- **license**: Copyright (c) 2018-2025 EDM Council, Inc. Copyright (c) 2018-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **modified**: 2025-05-27T18:00:00
- **title**: EDMC Financial Industry Business Ontology (FIBO) Business Entities (BE) Domain, European Extension
- **label**: Business Entities Domain, European Extension
- **seeAlso**: https://spec.edmcouncil.org/fibo/
- **copyright**: Copyright (c) 2018-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2018-2025 Object Management Group, Inc.
- **explanatoryNote**: The 'all' ontology for BE (European Extension) is provided for convenience for FIBO users.  This ontology does not add new assertions, but imports most of the Production (Released) ontologies that comprise the FIBO Business Entities (BE) domain, including all individuals for European governments and jurisdictions, and the related LCC region-specific ontologies. Note that the 45 ISO 3166-2 subdivision ontologies included are those defined as being part of Europe in the U.N. M49 Codes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
