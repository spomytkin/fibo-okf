---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bloomberg SDR
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap data repository that receives, validates, maintains, and provides regulator-authorized access to derivatives
      transaction data submitted under jurisdiction-specific reporting rules, and operates as a registered SDR service within
      the Bloomberg group of entities
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: BSDR
  defined_by:
  - concept: /concepts/fibo/DER/DerivativesContracts/SwapsIndividuals.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapDataRepository
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BSDRLLC-US-DE.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BSDRLLC-US-DE
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator.md
    predicate: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/BloombergSDR
sources:
- id: fibo-source-2b1a72c3a1
  resource: references/fibo/DER/DerivativesContracts/SwapsIndividuals.rdf
  sha256: 2b1a72c3a1db9285b93e97db0ac5f55555a206893741495827272209f11ad849
  title: FIBO source DER/DerivativesContracts/SwapsIndividuals.rdf
title: Bloomberg SDR
type: Ontology Individual
---

# Bloomberg SDR

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/BloombergSDR>

## Definition

swap data repository that receives, validates, maintains, and provides regulator-authorized access to derivatives transaction data submitted under jurisdiction-specific reporting rules, and operates as a registered SDR service within the Bloomberg group of entities

## Relationships

- **Defined by**: [SwapsIndividuals](/concepts/fibo/DER/DerivativesContracts/SwapsIndividuals.md)
- **Related to**: [CommoditiesFuturesAndDerivativesRegulator](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CommoditiesFuturesAndDerivativesRegulator.md)
- **Related to**: [BSDRLLC-US-DE](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BSDRLLC-US-DE.md)

## Annotations

- **label**: Bloomberg SDR
- **definition**: swap data repository that receives, validates, maintains, and provides regulator-authorized access to derivatives transaction data submitted under jurisdiction-specific reporting rules, and operates as a registered SDR service within the Bloomberg group of entities
- **abbreviation**: BSDR

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
