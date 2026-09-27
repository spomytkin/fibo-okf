---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SIX Group AG
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: SIX Group AG legal entity
  - predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation
    value: Public Limited Company
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasTradingOrOperationalName
    value: SIX Group Ltd
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasTradingOrOperationalName
    value: SIX Group SA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: SIX Group AG
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The company name SIX is an abbreviation and stands for Swiss Infrastructure and Exchange.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/hasSubsidiary
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXGroupAGHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXGroupAGHeadquartersAddress
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.six-group.com/en/home.html
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXGroupAG
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: SIX Group AG
type: Ontology Individual
---

# SIX Group AG

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXGroupAG>

## Definition

SIX Group AG legal entity

## Relationships

- **Related to**: [SIXGroupAGHeadquartersAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXGroupAGHeadquartersAddress.md)
- **Related to**: [SIXFinancialInformation](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation.md)
- **See also**: [home.html](<https://www.six-group.com/en/home.html>)

## Annotations

- **label**: SIX Group AG
- **definition**: SIX Group AG legal entity
- **hasLegalFormAbbreviation**: Public Limited Company
- **hasTradingOrOperationalName**: SIX Group Ltd
- **hasTradingOrOperationalName**: SIX Group SA
- **hasLegalName**: SIX Group AG
- **explanatoryNote**: The company name SIX is an abbreviation and stands for Swiss Infrastructure and Exchange.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
