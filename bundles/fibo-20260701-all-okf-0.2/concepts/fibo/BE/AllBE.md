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
    value: Adaptive Analytics, Inc.
  - predicate: http://purl.org/dc/terms/contributor
    value: Bloomberg LP
  - predicate: http://purl.org/dc/terms/contributor
    value: Citigroup
  - predicate: http://purl.org/dc/terms/contributor
    value: Credit Suisse
  - predicate: http://purl.org/dc/terms/contributor
    value: Deutsche Bank
  - predicate: http://purl.org/dc/terms/contributor
    value: Exprentis
  - predicate: http://purl.org/dc/terms/contributor
    value: Federated Knowledge, LLC
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
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/creator
    value: https://wiki.edmcouncil.org/display/BE/FIBO+-+FCT+-+Business+Entities+Home
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/issued
    value: '2018-08-27T18:00:00'
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group, Inc.\n\nPermission\
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
    value: '2025-10-15T18:00:00'
  - predicate: http://purl.org/dc/terms/title
    value: EDMC Financial Industry Business Ontology (FIBO) Business Entities (BE) Domain
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: All Business Entities (BE) Domain
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    value: https://spec.edmcouncil.org/fibo/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The 'all' ontology for BE is provided for convenience for FIBO users. This ontology does not add new assertions,
      but imports most of the Production (Released) ontologies that comprise the FIBO Business Entities (BE) domain, including
      all of FND but excluding individuals for governments and jurisdictions, and the related LCC region-specific ontologies.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20251001/AllBE/
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/LegalEntities/LEIEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/
  - concept: /concepts/fibo/BE/Partnerships/Partnerships.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/
  - concept: /concepts/fibo/BE/SoleProprietorships/SoleProprietorships.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/SoleProprietorships/SoleProprietorships/
  - concept: /concepts/fibo/BE/Trusts/Trusts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/
  - concept: /concepts/fibo/FND/AllFND.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AllFND/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/AllBE/
sources:
- id: fibo-source-9ce4eb1677
  resource: references/fibo/BE/AllBE.rdf
  sha256: 9ce4eb1677f2fca4791b3427470f302450001eb93fc3ac6c41939a80a567a463
  title: FIBO source BE/AllBE.rdf
title: All Business Entities (BE) Domain
type: Ontology Definition
---

# All Business Entities (BE) Domain

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/AllBE/>

## Relationships

- **Related to**: [FunctionalEntities](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md)
- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [GovernmentEntities](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md)
- **Related to**: [CorporateBodies](/concepts/fibo/BE/LegalEntities/CorporateBodies.md)
- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [LEIEntities](/concepts/fibo/BE/LegalEntities/LEIEntities.md)
- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [ControlParties](/concepts/fibo/BE/OwnershipAndControl/ControlParties.md)
- **Related to**: [CorporateControl](/concepts/fibo/BE/OwnershipAndControl/CorporateControl.md)
- **Related to**: [CorporateOwnership](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md)
- **Related to**: [Executives](/concepts/fibo/BE/OwnershipAndControl/Executives.md)
- **Related to**: [OwnershipParties](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md)
- **Related to**: [Partnerships](/concepts/fibo/BE/Partnerships/Partnerships.md)
- **Related to**: [PrivateLimitedCompanies](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.md)
- **Related to**: [SoleProprietorships](/concepts/fibo/BE/SoleProprietorships/SoleProprietorships.md)
- **Related to**: [Trusts](/concepts/fibo/BE/Trusts/Trusts.md)
- **Related to**: [AllFND](/concepts/fibo/FND/AllFND.md)
- **Related to**: [AllBE](<https://spec.edmcouncil.org/fibo/ontology/BE/20251001/AllBE/>)

## Annotations

- **abstract**: This ontology provides metadata about the FIBO Business Entities (BE) Domain, which covers defines business concepts that are used for data governance, interoperability, and in regulatory reporting about business entities.  The business scope of the BE ontologies covers a range of business and legal entities that are considered by financial industry firms, regulators and other industry participants to be of relevance in the financial services domain, including:  - Legal entities generally  - Corporate structure, ownership and control, including primary executive roles for businesses,  - Functional entities such as governments and government entities, non-governmental organizations, international organizations, not-for-profit organization, etc.  - Concepts specific to corporations, partnerships, private limited companies, sole proprietorships, and trusts.
- **contributor**: Adaptive Analytics, Inc.
- **contributor**: Bloomberg LP
- **contributor**: Citigroup
- **contributor**: Credit Suisse
- **contributor**: Deutsche Bank
- **contributor**: Exprentis
- **contributor**: Federated Knowledge, LLC
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
- **creator**: https://wiki.edmcouncil.org/display/BE/FIBO+-+FCT+-+Business+Entities+Home
- **issued**: 2018-08-27T18:00:00
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **modified**: 2025-10-15T18:00:00
- **title**: EDMC Financial Industry Business Ontology (FIBO) Business Entities (BE) Domain
- **label**: All Business Entities (BE) Domain
- **seeAlso**: https://spec.edmcouncil.org/fibo/
- **copyright**: Copyright (c) 2015-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.
- **explanatoryNote**: The 'all' ontology for BE is provided for convenience for FIBO users. This ontology does not add new assertions, but imports most of the Production (Released) ontologies that comprise the FIBO Business Entities (BE) domain, including all of FND but excluding individuals for governments and jurisdictions, and the related LCC region-specific ontologies.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
