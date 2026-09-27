---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Accuity Inc. US-DE
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Accuity Inc. legal entity that is a Delaware corporation and subsidiary of Wolters Kluwer
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Accuity Inc.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://accuity.com/
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isIncorporatedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AccuityIncHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AccuityIncHeadquartersAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AccuityInc-US-DE
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Accuity Inc. US-DE
type: Ontology Individual
---

# Accuity Inc. US-DE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AccuityInc-US-DE>

## Definition

Accuity Inc. legal entity that is a Delaware corporation and subsidiary of Wolters Kluwer

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [StateOfDelawareJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md)
- **Related to**: [AccuityIncHeadquartersAddress](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AccuityIncHeadquartersAddress.md)
- **Related to**: [CorporationTrustCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany.md)

## Annotations

- **label**: Accuity Inc. US-DE
- **definition**: Accuity Inc. legal entity that is a Delaware corporation and subsidiary of Wolters Kluwer
- **hasLegalName**: Accuity Inc.
- **hasWebsite**: https://accuity.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
