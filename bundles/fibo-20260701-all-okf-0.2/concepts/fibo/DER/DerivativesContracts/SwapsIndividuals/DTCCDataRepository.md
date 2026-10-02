---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: DTCC Data Repository
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap data repository that receives, validates, maintains, and provides regulated access to derivatives transaction
      data for reporting entities under U.S. and global derivatives market regulations, and operates as a registered SDR subsidiary
      of the Depository Trust & Clearing Corporation
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: DDR is part of DTCC's Global Trade Repository architecture and supports multi-jurisdictional derivatives reporting
      mandates (e.g., Dodd-Frank, EMIR, ASIC, MAS, HKMA, JFSA). It (1) receives and validates derivatives trade data from
      reporting counterparties, (2) maintains a centralized, regulator-accessible record of reported transactions, (3) provides
      data access to authorized regulators, and (4) operates under registration and oversight of relevant authorities (e.g.,
      CFTC, MAS, JFSA, ESMA depending on jurisdiction). DDR operates multiple jurisdiction-specific legal entities, provides
      reconciliation and lifecycle event processing, offers public aggregate reporting, and integrates with DTCC's Global
      Trade Repository (GTR) service.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: DDR
  defined_by:
  - concept: /concepts/fibo/DER/DerivativesContracts/SwapsIndividuals.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapDataRepository
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCDataRepositoryLLC-US-NY.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCDataRepositoryLLC-US-NY
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator.md
    predicate: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/DTCCDataRepository
sources:
- id: fibo-source-2b1a72c3a1
  resource: references/fibo/DER/DerivativesContracts/SwapsIndividuals.rdf
  sha256: 2b1a72c3a1db9285b93e97db0ac5f55555a206893741495827272209f11ad849
  title: FIBO source DER/DerivativesContracts/SwapsIndividuals.rdf
title: DTCC Data Repository
type: Ontology Individual
---

# DTCC Data Repository

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/DTCCDataRepository>

## Definition

swap data repository that receives, validates, maintains, and provides regulated access to derivatives transaction data for reporting entities under U.S. and global derivatives market regulations, and operates as a registered SDR subsidiary of the Depository Trust & Clearing Corporation

## Relationships

- **Defined by**: [SwapsIndividuals](/concepts/fibo/DER/DerivativesContracts/SwapsIndividuals.md)
- **Related to**: [CommoditiesFuturesAndDerivativesRegulator](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator.md)
- **Related to**: [DTCCDataRepositoryLLC-US-NY](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCDataRepositoryLLC-US-NY.md)

## Annotations

- **label**: DTCC Data Repository
- **definition**: swap data repository that receives, validates, maintains, and provides regulated access to derivatives transaction data for reporting entities under U.S. and global derivatives market regulations, and operates as a registered SDR subsidiary of the Depository Trust & Clearing Corporation
- **note**: DDR is part of DTCC's Global Trade Repository architecture and supports multi-jurisdictional derivatives reporting mandates (e.g., Dodd-Frank, EMIR, ASIC, MAS, HKMA, JFSA). It (1) receives and validates derivatives trade data from reporting counterparties, (2) maintains a centralized, regulator-accessible record of reported transactions, (3) provides data access to authorized regulators, and (4) operates under registration and oversight of relevant authorities (e.g., CFTC, MAS, JFSA, ESMA depending on jurisdiction). DDR operates multiple jurisdiction-specific legal entities, provides reconciliation and lifecycle event processing, offers public aggregate reporting, and integrates with DTCC's Global Trade Repository (GTR) service.
- **abbreviation**: DDR

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
