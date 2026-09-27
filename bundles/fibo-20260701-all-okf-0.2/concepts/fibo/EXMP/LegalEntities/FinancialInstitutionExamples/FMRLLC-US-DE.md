---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: FMR LLC US-DE
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: private company with limited liability legal entity for FMR LLC that is a Delaware Limited Liability Company
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasPriorLegalName
    value: Fidelity Management and Research Company
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: FMR LLC
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.fidelity.com/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/FMRLLCHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/FMRLLCHeadquartersAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/FMRLLC-US-DE
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: FMR LLC US-DE
type: Ontology Individual
---

# FMR LLC US-DE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/FMRLLC-US-DE>

## Definition

private company with limited liability legal entity for FMR LLC that is a Delaware Limited Liability Company

## Relationships

- **Related to**: [FMRLLCHeadquartersAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/FMRLLCHeadquartersAddress.md)
- **Related to**: [CorporationTrustCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/CorporationTrustCompany.md)

## Annotations

- **label**: FMR LLC US-DE
- **definition**: private company with limited liability legal entity for FMR LLC that is a Delaware Limited Liability Company
- **hasPriorLegalName**: Fidelity Management and Research Company
- **hasLegalName**: FMR LLC
- **hasWebsite**: https://www.fidelity.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
