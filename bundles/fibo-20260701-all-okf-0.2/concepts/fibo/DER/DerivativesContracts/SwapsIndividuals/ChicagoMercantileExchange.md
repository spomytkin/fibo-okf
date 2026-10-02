---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Chicago Mercantile Exchange
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial derivatives exchange that offers centralized, regulated trading of futures and options contracts across
      multiple asset classes and forms part of CME Group
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: Chicago Mercantile Exchange was founded in 1898, formerly the Chicago Butter and Egg Board. CME (1) provides a
      marketplace for standardized futures and options, (2) operates under CME rules as a Designated Contract Market, (3)
      supports trading in interest rates, equity indexes, energy, agriculture, FX, metals, and cryptocurrency products, and
      (4) functions as one of the four major exchanges within CME Group. It has been part of CME Group since 2007.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CME
  defined_by:
  - concept: /concepts/fibo/DER/DerivativesContracts/SwapsIndividuals.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapDataRepository
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/SelfRegulatingOrganization
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DesignatedContractMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ChicagoMercantileExchangeInc-US-DE.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ChicagoMercantileExchangeInc-US-DE
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator.md
    predicate: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/ChicagoMercantileExchange
sources:
- id: fibo-source-2b1a72c3a1
  resource: references/fibo/DER/DerivativesContracts/SwapsIndividuals.rdf
  sha256: 2b1a72c3a1db9285b93e97db0ac5f55555a206893741495827272209f11ad849
  title: FIBO source DER/DerivativesContracts/SwapsIndividuals.rdf
title: Chicago Mercantile Exchange
type: Ontology Individual
---

# Chicago Mercantile Exchange

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/ChicagoMercantileExchange>

## Definition

financial derivatives exchange that offers centralized, regulated trading of futures and options contracts across multiple asset classes and forms part of CME Group

## Relationships

- **Defined by**: [SwapsIndividuals](/concepts/fibo/DER/DerivativesContracts/SwapsIndividuals.md)
- **Related to**: [CommoditiesFuturesAndDerivativesRegulator](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator.md)
- **Related to**: [ChicagoMercantileExchangeInc-US-DE](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ChicagoMercantileExchangeInc-US-DE.md)

## Annotations

- **label**: Chicago Mercantile Exchange
- **definition**: financial derivatives exchange that offers centralized, regulated trading of futures and options contracts across multiple asset classes and forms part of CME Group
- **note**: Chicago Mercantile Exchange was founded in 1898, formerly the Chicago Butter and Egg Board. CME (1) provides a marketplace for standardized futures and options, (2) operates under CME rules as a Designated Contract Market, (3) supports trading in interest rates, equity indexes, energy, agriculture, FX, metals, and cryptocurrency products, and (4) functions as one of the four major exchanges within CME Group. It has been part of CME Group since 2007.
- **abbreviation**: CME

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
