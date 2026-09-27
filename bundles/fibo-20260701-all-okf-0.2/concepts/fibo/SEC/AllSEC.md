---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: The FIBO Securities (SEC) domain provides a model of concepts that are common to financial instruments that are
      also securities, including but not limited to exchange-traded securities. High-level concepts relevant to securities
      classification, identification, issuance, and registration of securities generally are covered, as well as additional
      detail for equities, debt instruments, and funds. More details defining derivatives in particular are covered in a separate
      derivatives domain area.
  - predicate: http://purl.org/dc/terms/contributor
    value: Adaptive, Inc.
  - predicate: http://purl.org/dc/terms/contributor
    value: BIAN
  - predicate: http://purl.org/dc/terms/contributor
    value: Bloomberg LP
  - predicate: http://purl.org/dc/terms/contributor
    value: Citigroup
  - predicate: http://purl.org/dc/terms/contributor
    value: Credit Suisse
  - predicate: http://purl.org/dc/terms/contributor
    value: Dassault Systemes / No Magic
  - predicate: http://purl.org/dc/terms/contributor
    value: Deutsche Bank
  - predicate: http://purl.org/dc/terms/contributor
    value: Exprentis
  - predicate: http://purl.org/dc/terms/contributor
    value: FIÙTUR
  - predicate: http://purl.org/dc/terms/contributor
    value: Federated Knowledge LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: Goldman Sachs
  - predicate: http://purl.org/dc/terms/contributor
    value: HP Enterprise / Mphasis
  - predicate: http://purl.org/dc/terms/contributor
    value: John F. Gemski
  - predicate: http://purl.org/dc/terms/contributor
    value: John F. Tierney
  - predicate: http://purl.org/dc/terms/contributor
    value: Mizuho
  - predicate: http://purl.org/dc/terms/contributor
    value: Nordea Bank AB
  - predicate: http://purl.org/dc/terms/contributor
    value: Office of Financial Research (US Dept of the Treasury)
  - predicate: http://purl.org/dc/terms/contributor
    value: ProBanker Simulations, LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: Quarule
  - predicate: http://purl.org/dc/terms/contributor
    value: State Street Bank and Trust
  - predicate: http://purl.org/dc/terms/contributor
    value: Statistics Canada
  - predicate: http://purl.org/dc/terms/contributor
    value: Tahoe Blue Ltd
  - predicate: http://purl.org/dc/terms/contributor
    value: Thematix Partners LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: Wells Fargo Bank, N.A.
  - predicate: http://purl.org/dc/terms/contributor
    value: agnos.ai U.K. Ltd
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/issued
    value: '2018-03-31T18:00:00'
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2018-2025 Object Management Group,\
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
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/modified
    value: '2026-07-08T18:00:00'
  - predicate: http://purl.org/dc/terms/title
    value: EDMC Financial Industry Business Ontology (FIBO) Securities (SEC) Domain
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: all SEC
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The 'all' ontology for SEC is provided for convenience for FIBO users. This ontology does not add new assertions,
      but imports most of the Production (Released) ontologies that comprise the FIBO Foundations (FND), Business Entities
      (BE), Financial Business and Commerce (FBC), Indices and Indicators (IND), and Securities (SEC) domains, excluding most
      individuals for governments and jurisdictions (aside from those used in depositary receipts), financial services, regulatory
      organizations and related registries, and reference individuals, as well as the LCC region-specific ontologies.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/IND/AllIND.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/AllIND/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/20260701/AllSEC/
  - concept: /concepts/fibo/SEC/Debt/AssetBackedSecurities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/
  - concept: /concepts/fibo/SEC/Debt/Bonds.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/
  - concept: /concepts/fibo/SEC/Debt/DistributedLoans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/
  - concept: /concepts/fibo/SEC/Funds/Funds.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/
  - concept: /concepts/fibo/SEC/Securities/Baskets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/
  - concept: /concepts/fibo/SEC/Securities/ParametricSchedules.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/
  - concept: /concepts/fibo/SEC/Securities/Pools.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesClassification.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesRestrictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.edmcouncil.org/fibo/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/AllSEC/
sources:
- id: fibo-source-7c81a9ba20
  resource: references/fibo/SEC/AllSEC.rdf
  sha256: 7c81a9ba20f8086f8773268815710c21f13c0110718baa05bb66da9ae6d3e5ab
  title: FIBO source SEC/AllSEC.rdf
title: all SEC
type: Ontology Definition
---

# all SEC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/AllSEC/>

## Relationships

- **Related to**: [AllIND](/concepts/fibo/IND/AllIND.md)
- **Related to**: [AssetBackedSecurities](/concepts/fibo/SEC/Debt/AssetBackedSecurities.md)
- **Related to**: [Bonds](/concepts/fibo/SEC/Debt/Bonds.md)
- **Related to**: [DebtInstruments](/concepts/fibo/SEC/Debt/DebtInstruments.md)
- **Related to**: [DistributedLoans](/concepts/fibo/SEC/Debt/DistributedLoans.md)
- **Related to**: [ExerciseConventions](/concepts/fibo/SEC/Debt/ExerciseConventions.md)
- **Related to**: [PoolBackedSecurities](/concepts/fibo/SEC/Debt/PoolBackedSecurities.md)
- **Related to**: [TradedShortTermDebt](/concepts/fibo/SEC/Debt/TradedShortTermDebt.md)
- **Related to**: [DepositaryReceipts](/concepts/fibo/SEC/Equities/DepositaryReceipts.md)
- **Related to**: [EquityInstruments](/concepts/fibo/SEC/Equities/EquityInstruments.md)
- **Related to**: [Funds](/concepts/fibo/SEC/Funds/Funds.md)
- **Related to**: [Baskets](/concepts/fibo/SEC/Securities/Baskets.md)
- **Related to**: [ParametricSchedules](/concepts/fibo/SEC/Securities/ParametricSchedules.md)
- **Related to**: [Pools](/concepts/fibo/SEC/Securities/Pools.md)
- **Related to**: [SecuritiesClassification](/concepts/fibo/SEC/Securities/SecuritiesClassification.md)
- **Related to**: [SecuritiesIdentification](/concepts/fibo/SEC/Securities/SecuritiesIdentification.md)
- **Related to**: [SecuritiesIssuance](/concepts/fibo/SEC/Securities/SecuritiesIssuance.md)
- **Related to**: [SecuritiesListings](/concepts/fibo/SEC/Securities/SecuritiesListings.md)
- **Related to**: [SecuritiesRestrictions](/concepts/fibo/SEC/Securities/SecuritiesRestrictions.md)
- **Related to**: [AllSEC](<https://spec.edmcouncil.org/fibo/ontology/SEC/20260701/AllSEC/>)
- **See also**: [fibo](<https://www.edmcouncil.org/fibo/>)

## Annotations

- **abstract**: The FIBO Securities (SEC) domain provides a model of concepts that are common to financial instruments that are also securities, including but not limited to exchange-traded securities. High-level concepts relevant to securities classification, identification, issuance, and registration of securities generally are covered, as well as additional detail for equities, debt instruments, and funds. More details defining derivatives in particular are covered in a separate derivatives domain area.
- **contributor**: Adaptive, Inc.
- **contributor**: BIAN
- **contributor**: Bloomberg LP
- **contributor**: Citigroup
- **contributor**: Credit Suisse
- **contributor**: Dassault Systemes / No Magic
- **contributor**: Deutsche Bank
- **contributor**: Exprentis
- **contributor**: FIÙTUR
- **contributor**: Federated Knowledge LLC
- **contributor**: Goldman Sachs
- **contributor**: HP Enterprise / Mphasis
- **contributor**: John F. Gemski
- **contributor**: John F. Tierney
- **contributor**: Mizuho
- **contributor**: Nordea Bank AB
- **contributor**: Office of Financial Research (US Dept of the Treasury)
- **contributor**: ProBanker Simulations, LLC
- **contributor**: Quarule
- **contributor**: State Street Bank and Trust
- **contributor**: Statistics Canada
- **contributor**: Tahoe Blue Ltd
- **contributor**: Thematix Partners LLC
- **contributor**: Wells Fargo Bank, N.A.
- **contributor**: agnos.ai U.K. Ltd
- **issued**: 2018-03-31T18:00:00
- **license**: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2018-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **modified**: 2026-07-08T18:00:00
- **title**: EDMC Financial Industry Business Ontology (FIBO) Securities (SEC) Domain
- **label**: all SEC
- **copyright**: Copyright (c) 2018-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.
- **explanatoryNote**: The 'all' ontology for SEC is provided for convenience for FIBO users. This ontology does not add new assertions, but imports most of the Production (Released) ontologies that comprise the FIBO Foundations (FND), Business Entities (BE), Financial Business and Commerce (FBC), Indices and Indicators (IND), and Securities (SEC) domains, excluding most individuals for governments and jurisdictions (aside from those used in depositary receipts), financial services, regulatory organizations and related registries, and reference individuals, as well as the LCC region-specific ontologies.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
