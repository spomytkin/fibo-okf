---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ICE Trade Vault
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap data repository that collects, validates, stores, and provides regulated access to derivatives transaction
      data for reporting entities under jurisdiction-specific derivatives reporting rules, and operates as a registered SDR
      service within Intercontinental Exchange (ICE)
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ICE Trade Vault is part of ICE's broader market infrastructure ecosystem and supports derivatives reporting mandates
      under Dodd-Frank, EMIR, and other jurisdictional regimes. It (1) receives and validates derivatives trade data from
      reporting counterparties, (2) maintains a centralized, regulator-accessible record of reported transactions and lifecycle
      events, (3) provides data access to authorized regulators and public aggregate reporting, and (4) operates under registration
      and oversight of relevant authorities (e.g., CFTC, ESMA, MAS, depending on jurisdiction). ICE Trade Vault offers multi-asset
      class reporting (e.g., credit, interest rate, FX, commodity derivatives, integrates with ICE's clearing and trading
      infrastructure, and provides reconciliation and data quality tools.
  defined_by:
  - concept: /concepts/fibo/DER/DerivativesContracts/SwapsIndividuals.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapDataRepository
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ICETradeVaultLLC-US-DE.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ICETradeVaultLLC-US-DE
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator.md
    predicate: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/ICETradeVault
sources:
- id: fibo-source-2b1a72c3a1
  resource: references/fibo/DER/DerivativesContracts/SwapsIndividuals.rdf
  sha256: 2b1a72c3a1db9285b93e97db0ac5f55555a206893741495827272209f11ad849
  title: FIBO source DER/DerivativesContracts/SwapsIndividuals.rdf
title: ICE Trade Vault
type: Ontology Individual
---

# ICE Trade Vault

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/ICETradeVault>

## Definition

swap data repository that collects, validates, stores, and provides regulated access to derivatives transaction data for reporting entities under jurisdiction-specific derivatives reporting rules, and operates as a registered SDR service within Intercontinental Exchange (ICE)

## Relationships

- **Defined by**: [SwapsIndividuals](/concepts/fibo/DER/DerivativesContracts/SwapsIndividuals.md)
- **Related to**: [CommoditiesFuturesAndDerivativesRegulator](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator.md)
- **Related to**: [ICETradeVaultLLC-US-DE](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ICETradeVaultLLC-US-DE.md)

## Annotations

- **label**: ICE Trade Vault
- **definition**: swap data repository that collects, validates, stores, and provides regulated access to derivatives transaction data for reporting entities under jurisdiction-specific derivatives reporting rules, and operates as a registered SDR service within Intercontinental Exchange (ICE)
- **note**: ICE Trade Vault is part of ICE's broader market infrastructure ecosystem and supports derivatives reporting mandates under Dodd-Frank, EMIR, and other jurisdictional regimes. It (1) receives and validates derivatives trade data from reporting counterparties, (2) maintains a centralized, regulator-accessible record of reported transactions and lifecycle events, (3) provides data access to authorized regulators and public aggregate reporting, and (4) operates under registration and oversight of relevant authorities (e.g., CFTC, ESMA, MAS, depending on jurisdiction). ICE Trade Vault offers multi-asset class reporting (e.g., credit, interest rate, FX, commodity derivatives, integrates with ICE's clearing and trading infrastructure, and provides reconciliation and data quality tools.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
