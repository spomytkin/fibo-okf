---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This module defines debt securities contracts both cash and synthetic, such as bonds, structured finance instruments,
      short term or money market instruments, and other contracts characterized by the holding of some debt of the issuer
      or primary party by the holder or counterparty.
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
    value: Wells Fargo
  - predicate: http://purl.org/dc/terms/contributor
    value: agnos.ai U.K. Ltd
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: http://opensource.org/licenses/MIT
  - predicate: http://purl.org/dc/terms/title
    value: FIBO SEC Debt Module
  - predicate: http://purl.org/dc/terms/title
    value: Financial Industry Business Ontology (FIBO) Securities and Equities (SEC) Debt Module
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt module
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2024 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2024 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Module
  related_to:
  - concept: /concepts/fibo/SEC/Debt/AssetBackedSecurities.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/
  - concept: /concepts/fibo/SEC/Debt/Bonds.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/
  - concept: /concepts/fibo/SEC/Debt/DistributedLoans.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/
  - concept: /concepts/fibo/SEC/Debt/SyntheticCDOs.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.edmcouncil.org/fibo/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MetadataSECDebt/DebtModule
sources:
- id: fibo-source-a228ff40bc
  resource: references/fibo/SEC/Debt/MetadataSECDebt.rdf
  sha256: a228ff40bca21a0a7ad32442b702a56f195e852776fd20df10e59ae23d3777fa
  title: FIBO source SEC/Debt/MetadataSECDebt.rdf
title: debt module
type: Ontology Individual
---

# debt module

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MetadataSECDebt/DebtModule>

## Relationships

- **Related to**: [AssetBackedSecurities](/concepts/fibo/SEC/Debt/AssetBackedSecurities.md)
- **Related to**: [Bonds](/concepts/fibo/SEC/Debt/Bonds.md)
- **Related to**: [CollateralizedDebtObligations](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations.md)
- **Related to**: [DebtInstruments](/concepts/fibo/SEC/Debt/DebtInstruments.md)
- **Related to**: [DistributedLoans](/concepts/fibo/SEC/Debt/DistributedLoans.md)
- **Related to**: [ExerciseConventions](/concepts/fibo/SEC/Debt/ExerciseConventions.md)
- **Related to**: [MortgageBackedSecurities](/concepts/fibo/SEC/Debt/MortgageBackedSecurities.md)
- **Related to**: [PoolBackedSecurities](/concepts/fibo/SEC/Debt/PoolBackedSecurities.md)
- **Related to**: [SyntheticCDOs](/concepts/fibo/SEC/Debt/SyntheticCDOs.md)
- **Related to**: [TradedShortTermDebt](/concepts/fibo/SEC/Debt/TradedShortTermDebt.md)
- **See also**: [fibo](<https://www.edmcouncil.org/fibo/>)

## Annotations

- **abstract**: This module defines debt securities contracts both cash and synthetic, such as bonds, structured finance instruments, short term or money market instruments, and other contracts characterized by the holding of some debt of the issuer or primary party by the holder or counterparty.
- **contributor**: Adaptive, Inc.
- **contributor**: BIAN
- **contributor**: Bloomberg LP
- **contributor**: Citigroup
- **contributor**: Credit Suisse
- **contributor**: Dassault Systemes / No Magic
- **contributor**: Deutsche Bank
- **contributor**: Exprentis
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
- **contributor**: Wells Fargo
- **contributor**: agnos.ai U.K. Ltd
- **license**: http://opensource.org/licenses/MIT
- **title**: FIBO SEC Debt Module
- **title**: Financial Industry Business Ontology (FIBO) Securities and Equities (SEC) Debt Module
- **label**: debt module
- **copyright**: Copyright (c) 2018-2024 EDM Council, Inc.
- **copyright**: Copyright (c) 2018-2024 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
