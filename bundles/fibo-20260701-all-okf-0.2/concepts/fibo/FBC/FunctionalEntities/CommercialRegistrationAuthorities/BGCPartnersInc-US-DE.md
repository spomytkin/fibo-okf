---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BGC Partners, Inc. US-DE
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal entity that is a Delaware Corporation
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasPriorLegalName
    value: Cantor Fitzgerald
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: BGC Partners, Inc. US-DE
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/StockCorporation
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BGCPartnersIncDateEstablished.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasDateEstablished
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BGCPartnersIncDateEstablished
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BGCPartnersIncHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BGCPartnersIncHeadquartersAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BGCPartnersInc-US-DE
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: BGC Partners, Inc. US-DE
type: Ontology Individual
---

# BGC Partners, Inc. US-DE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BGCPartnersInc-US-DE>

## Definition

legal entity that is a Delaware Corporation

## Relationships

- **Related to**: [BGCPartnersIncHeadquartersAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BGCPartnersIncHeadquartersAddress.md)
- **Related to**: [BGCPartnersIncDateEstablished](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BGCPartnersIncDateEstablished.md)
- **Related to**: [CorporationServiceCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany.md)

## Annotations

- **label**: BGC Partners, Inc. US-DE
- **definition**: legal entity that is a Delaware Corporation
- **hasPriorLegalName**: Cantor Fitzgerald
- **hasLegalName**: BGC Partners, Inc. US-DE

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
