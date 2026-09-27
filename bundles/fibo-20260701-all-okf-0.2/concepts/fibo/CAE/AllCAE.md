---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides metadata about the FIBO Corporate Actions and Events (CAE) Domain, which covers actions
      including corporate, market, and regulatory actions, ranging from business oriented events such as address and name
      changes, to those that are more specific to securities.
  - predicate: http://purl.org/dc/terms/contributor
    value: Adaptive, Inc.
  - predicate: http://purl.org/dc/terms/contributor
    value: Bank of New York Mellon
  - predicate: http://purl.org/dc/terms/contributor
    value: Bloomberg LP
  - predicate: http://purl.org/dc/terms/contributor
    value: Bureau of Economic Analysis (BEA, US Department of Commerce)
  - predicate: http://purl.org/dc/terms/contributor
    value: Bureau of Labor Statistics (BLS, US Department of Commerce)
  - predicate: http://purl.org/dc/terms/contributor
    value: Census Bureau (US Department of Commerce)
  - predicate: http://purl.org/dc/terms/contributor
    value: Citigroup
  - predicate: http://purl.org/dc/terms/contributor
    value: Dassault Systemes/No Magic
  - predicate: http://purl.org/dc/terms/contributor
    value: Deutsche Bank
  - predicate: http://purl.org/dc/terms/contributor
    value: Federal Reserve Bank of Kansas City
  - predicate: http://purl.org/dc/terms/contributor
    value: HP Enterprise / Mphasis
  - predicate: http://purl.org/dc/terms/contributor
    value: John F. Gemski
  - predicate: http://purl.org/dc/terms/contributor
    value: John F. Tierney
  - predicate: http://purl.org/dc/terms/contributor
    value: Nordea Bank AB
  - predicate: http://purl.org/dc/terms/contributor
    value: Office of Financial Research (OFR), U.S. Department of the Treasury
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
    value: Wells Fargo Bank, N. A.
  - predicate: http://purl.org/dc/terms/contributor
    value: agnos.ai UK Ltd
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/issued
    value: '2018-03-31T18:00:00'
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: http://opensource.org/licenses/MIT
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/modified
    value: '2023-02-03T18:00:00'
  - predicate: http://purl.org/dc/terms/title
    value: Financial Industry Business Ontology (FIBO) Corporate Actions and Events (CAE) Domain
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Corporate Actions and Events Domain
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    value: https://spec.edmcouncil.org/fibo/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2023 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2023 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The 'all' ontology for CAE is provided for convenience for FIBO users. This ontology does not add new assertions,
      but imports the Production (Released) ontologies that comprise the FIBO Corporate Actions and Events (CAE) domain, including
      all of SEC but excluding reference and example individuals.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/20230201/AllCAE/
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/
  - concept: /concepts/fibo/SEC/AllSEC.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/AllSEC/
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/AllCAE/
sources:
- id: fibo-source-f5787e78b1
  resource: references/fibo/CAE/AllCAE.rdf
  sha256: f5787e78b103f21dbcc7822a1a1ab8370426e9d82347877f44118760be7062b1
  title: FIBO source CAE/AllCAE.rdf
title: Corporate Actions and Events Domain
type: Ontology Definition
---

# Corporate Actions and Events Domain

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/AllCAE/>

## Relationships

- **Related to**: [CorporateActions](/concepts/fibo/CAE/CorporateEvents/CorporateActions.md)
- **Related to**: [AllSEC](/concepts/fibo/SEC/AllSEC.md)
- **Related to**: [AllCAE](<https://spec.edmcouncil.org/fibo/ontology/CAE/20230201/AllCAE/>)

## Annotations

- **abstract**: This ontology provides metadata about the FIBO Corporate Actions and Events (CAE) Domain, which covers actions including corporate, market, and regulatory actions, ranging from business oriented events such as address and name changes, to those that are more specific to securities.
- **contributor**: Adaptive, Inc.
- **contributor**: Bank of New York Mellon
- **contributor**: Bloomberg LP
- **contributor**: Bureau of Economic Analysis (BEA, US Department of Commerce)
- **contributor**: Bureau of Labor Statistics (BLS, US Department of Commerce)
- **contributor**: Census Bureau (US Department of Commerce)
- **contributor**: Citigroup
- **contributor**: Dassault Systemes/No Magic
- **contributor**: Deutsche Bank
- **contributor**: Federal Reserve Bank of Kansas City
- **contributor**: HP Enterprise / Mphasis
- **contributor**: John F. Gemski
- **contributor**: John F. Tierney
- **contributor**: Nordea Bank AB
- **contributor**: Office of Financial Research (OFR), U.S. Department of the Treasury
- **contributor**: Pinnacle Bank (Morgan Hill, California)
- **contributor**: State Street Bank and Trust
- **contributor**: Statistics Canada
- **contributor**: Tahoe Blue Ltd
- **contributor**: Thematix Partners LLC
- **contributor**: Wells Fargo Bank, N. A.
- **contributor**: agnos.ai UK Ltd
- **issued**: 2018-03-31T18:00:00
- **license**: http://opensource.org/licenses/MIT
- **modified**: 2023-02-03T18:00:00
- **title**: Financial Industry Business Ontology (FIBO) Corporate Actions and Events (CAE) Domain
- **label**: Corporate Actions and Events Domain
- **seeAlso**: https://spec.edmcouncil.org/fibo/
- **copyright**: Copyright (c) 2018-2023 EDM Council, Inc.
- **copyright**: Copyright (c) 2018-2023 Object Management Group, Inc.
- **explanatoryNote**: The 'all' ontology for CAE is provided for convenience for FIBO users. This ontology does not add new assertions, but imports the Production (Released) ontologies that comprise the FIBO Corporate Actions and Events (CAE) domain, including all of SEC but excluding reference and example individuals.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
