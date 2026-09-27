---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: S & P Dow Jones Indices LLC US-DE
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the S & P Dow Jones Indices LLC legal entity that is a Delaware limited liability company
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://us.spindices.com/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SPGlobal.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasDomesticUltimateParent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SPGlobal
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SPGlobalHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SPGlobalHeadquartersAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/SPDowJonesIndicesLLC-US-DE
sources:
- id: fibo-source-c9fb5c672c
  resource: references/fibo/EXMP/Securities/EquityIndexExamples.rdf
  sha256: c9fb5c672cbb6dc4ba551074dd33b7e27294259b5a24a6064670bc5c0205149d
  title: FIBO source EXMP/Securities/EquityIndexExamples.rdf
title: S & P Dow Jones Indices LLC US-DE
type: Ontology Individual
---

# S & P Dow Jones Indices LLC US-DE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/SPDowJonesIndicesLLC-US-DE>

## Definition

the S & P Dow Jones Indices LLC legal entity that is a Delaware limited liability company

## Relationships

- **Related to**: [SPGlobalHeadquartersAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SPGlobalHeadquartersAddress.md)
- **Related to**: [SPGlobal](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SPGlobal.md)
- **Related to**: [CorporationServiceCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationServiceCompany.md)

## Annotations

- **label**: S & P Dow Jones Indices LLC US-DE
- **definition**: the S & P Dow Jones Indices LLC legal entity that is a Delaware limited liability company
- **hasWebsite**: https://us.spindices.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
