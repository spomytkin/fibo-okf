---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bloomberg L.P. US-DE
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Bloomberg L.P. legal entity that is a Delaware Limited Partnership
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Bloomberg L.P.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedPartnership
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergDateEstablished.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasDateEstablished
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergDateEstablished
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergFinanceLP.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasSubsidiary
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergFinanceLP
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergHeadquartersAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.bloomberg.com/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP-US-DE
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Bloomberg L.P. US-DE
type: Ontology Individual
---

# Bloomberg L.P. US-DE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP-US-DE>

## Definition

Bloomberg L.P. legal entity that is a Delaware Limited Partnership

## Relationships

- **Related to**: [BloombergHeadquartersAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergHeadquartersAddress.md)
- **Related to**: [BloombergFinanceLP](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergFinanceLP.md)
- **Related to**: [BloombergDateEstablished](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergDateEstablished.md)
- **Related to**: [CorporationServiceCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany.md)
- **See also**: [http://www.bloomberg.com/](<http://www.bloomberg.com/>)

## Annotations

- **label**: Bloomberg L.P. US-DE
- **definition**: Bloomberg L.P. legal entity that is a Delaware Limited Partnership
- **hasLegalName**: Bloomberg L.P.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
