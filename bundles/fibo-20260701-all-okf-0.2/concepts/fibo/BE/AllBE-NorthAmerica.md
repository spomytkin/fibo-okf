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
    value: EDMC Financial Industry Business Ontology (FIBO) Business Entities (BE) Domain, North American Extension
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Business Entities Domain, North American Extension
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    value: https://spec.edmcouncil.org/fibo/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The 'all' ontology for BE (North American Extension) is provided for convenience for FIBO users.  This ontology
      does not add new assertions, but imports most of the Production (Released) ontologies that comprise the FIBO Business
      Entities (BE) domain, including all of FND but excluding individuals for European governments and jurisdictions, and
      the related LCC region-specific ontologies. Note that the U.N. M49 Codes do not distinguish North and South America,
      and thus this ontology defines North America as the landmass north of the Panama-Colombia border (Northern America and
      Central America from an M49 code perspective), and the islands of the Caribbean (also identified as the Caribbean in
      the M49 subregion codes).  North American government entities and jurisdictions are provided for a subset of these countries
      and regions in FIBO 2.0, with the anticipation that additional entities will be added over time.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20250501/AllBE-NorthAmerica/
  - concept: /concepts/fibo/BE/AllBE.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/AllBE/
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CaribbeanGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/CaribbeanGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/MXGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/MXGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/FND/AllFND-NorthAmerica.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AllFND-NorthAmerica/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/AllBE-NorthAmerica/
sources:
- id: fibo-source-a016a5aa79
  resource: references/fibo/BE/AllBE-NorthAmerica.rdf
  sha256: a016a5aa7925d9cd2dcc963045e2cb947a9f726d0648489cf352a7053555a988
  title: FIBO source BE/AllBE-NorthAmerica.rdf
title: Business Entities Domain, North American Extension
type: Ontology Definition
---

# Business Entities Domain, North American Extension

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/AllBE-NorthAmerica/>

## Relationships

- **Related to**: [AllBE](/concepts/fibo/BE/AllBE.md)
- **Related to**: [CAGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [CaribbeanGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CaribbeanGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [MXGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/MXGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [USGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [AllFND-NorthAmerica](/concepts/fibo/FND/AllFND-NorthAmerica.md)
- **Related to**: [AllBE-NorthAmerica](<https://spec.edmcouncil.org/fibo/ontology/BE/20250501/AllBE-NorthAmerica/>)

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
- **title**: EDMC Financial Industry Business Ontology (FIBO) Business Entities (BE) Domain, North American Extension
- **label**: Business Entities Domain, North American Extension
- **seeAlso**: https://spec.edmcouncil.org/fibo/
- **copyright**: Copyright (c) 2018-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2018-2025 Object Management Group, Inc.
- **explanatoryNote**: The 'all' ontology for BE (North American Extension) is provided for convenience for FIBO users.  This ontology does not add new assertions, but imports most of the Production (Released) ontologies that comprise the FIBO Business Entities (BE) domain, including all of FND but excluding individuals for European governments and jurisdictions, and the related LCC region-specific ontologies. Note that the U.N. M49 Codes do not distinguish North and South America, and thus this ontology defines North America as the landmass north of the Panama-Colombia border (Northern America and Central America from an M49 code perspective), and the islands of the Caribbean (also identified as the Caribbean in the M49 subregion codes).  North American government entities and jurisdictions are provided for a subset of these countries and regions in FIBO 2.0, with the anticipation that additional entities will be added over time.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
