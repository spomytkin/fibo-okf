---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: The FIBO Indices and Indicators (IND) Domain covers market indices and reference rates including economic indicators,
      foreign exchange, interest rates, and other benchmarks. The ontologies cover quoted interest rates, economic measures
      such as employment rates, and quoted indices required to support baskets of securities, including specific kinds of
      securities in share indices or bond indices, as well as credit indices.
  - predicate: http://purl.org/dc/terms/contributor
    value: 88 Solutions
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
    value: '2018-08-27T18:00:00'
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/modified
    value: '2023-02-06T18:00:00'
  - predicate: http://purl.org/dc/terms/title
    value: Financial Industry Business Ontology (FIBO) Indices and Indicators (IND) Domain
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Indices and Indicators Domain
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2023 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2023 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The 'all' ontology for IND is provided for convenience for FIBO users. It imports most of the Production (Released)
      ontologies that comprise the FIBO Foundations (FND), Business Entities (BE), Financial Business and Commerce (FBC),
      and Indices and Indicators (IND) domains, excluding individuals for governments and jurisdictions, financial services,
      regulatory organizations and related registries, and reference individuals, as well as the LCC region-specific ontologies.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/FBC/AllFBC.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/AllFBC/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/20230201/AllIND/
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/
  - concept: /concepts/fibo/IND/Indicators/Indicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/
  - concept: /concepts/fibo/IND/InterestRates/InterestRates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/
  - concept: /concepts/fibo/SEC/Securities/Baskets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesClassification.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.edmcouncil.org/fibo/
resource: https://spec.edmcouncil.org/fibo/ontology/IND/AllIND/
sources:
- id: fibo-source-3cdd040011
  resource: references/fibo/IND/AllIND.rdf
  sha256: 3cdd04001173c2fe857a18bc5b2ee6d016a929c667bf468e814b161dae3a7220
  title: FIBO source IND/AllIND.rdf
title: Indices and Indicators Domain
type: Ontology Definition
---

# Indices and Indicators Domain

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/AllIND/>

## Relationships

- **Related to**: [AllFBC](/concepts/fibo/FBC/AllFBC.md)
- **Related to**: [EconomicIndicators](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators.md)
- **Related to**: [ForeignExchange](/concepts/fibo/IND/ForeignExchange/ForeignExchange.md)
- **Related to**: [Indicators](/concepts/fibo/IND/Indicators/Indicators.md)
- **Related to**: [InterestRates](/concepts/fibo/IND/InterestRates/InterestRates.md)
- **Related to**: [BasketIndices](/concepts/fibo/IND/MarketIndices/BasketIndices.md)
- **Related to**: [EquityInstruments](/concepts/fibo/SEC/Equities/EquityInstruments.md)
- **Related to**: [Baskets](/concepts/fibo/SEC/Securities/Baskets.md)
- **Related to**: [SecuritiesClassification](/concepts/fibo/SEC/Securities/SecuritiesClassification.md)
- **Related to**: [AllIND](<https://spec.edmcouncil.org/fibo/ontology/IND/20230201/AllIND/>)
- **See also**: [fibo](<https://www.edmcouncil.org/fibo/>)

## Annotations

- **abstract**: The FIBO Indices and Indicators (IND) Domain covers market indices and reference rates including economic indicators, foreign exchange, interest rates, and other benchmarks. The ontologies cover quoted interest rates, economic measures such as employment rates, and quoted indices required to support baskets of securities, including specific kinds of securities in share indices or bond indices, as well as credit indices.
- **contributor**: 88 Solutions
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
- **issued**: 2018-08-27T18:00:00
- **license**: https://opensource.org/licenses/MIT
- **modified**: 2023-02-06T18:00:00
- **title**: Financial Industry Business Ontology (FIBO) Indices and Indicators (IND) Domain
- **label**: Indices and Indicators Domain
- **copyright**: Copyright (c) 2014-2023 EDM Council, Inc.
- **copyright**: Copyright (c) 2014-2023 Object Management Group, Inc.
- **explanatoryNote**: The 'all' ontology for IND is provided for convenience for FIBO users. It imports most of the Production (Released) ontologies that comprise the FIBO Foundations (FND), Business Entities (BE), Financial Business and Commerce (FBC), and Indices and Indicators (IND) domains, excluding individuals for governments and jurisdictions, financial services, regulatory organizations and related registries, and reference individuals, as well as the LCC region-specific ontologies.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
