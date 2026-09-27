---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Euroclear SA/NV
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Euroclear legal entity that is the parent company of the international and national central securities depositories
      ((I)CSDs) of the Euroclear group of companies; it owns the group's shared securities processing platforms and delivers
      a range of services to the group's depositories
  - predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation
    value: Societe Anonyme/Naamloze Vennootschap
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Euroclear SA/NV
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/StockCorporation
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingHeadquartersAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingLegalAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingLegalAddress
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.euroclear.com/en/about/our-structure.html
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/EuroclearSANV
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: Euroclear SA/NV
type: Ontology Individual
---

# Euroclear SA/NV

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/EuroclearSANV>

## Definition

Euroclear legal entity that is the parent company of the international and national central securities depositories ((I)CSDs) of the Euroclear group of companies; it owns the group's shared securities processing platforms and delivers a range of services to the group's depositories

## Relationships

- **Related to**: [ClearstreamBankingHeadquartersAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingHeadquartersAddress.md)
- **Related to**: [ClearstreamBankingLegalAddress](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingLegalAddress.md)
- **See also**: [our-structure.html](<https://www.euroclear.com/en/about/our-structure.html>)

## Annotations

- **label**: Euroclear SA/NV
- **definition**: Euroclear legal entity that is the parent company of the international and national central securities depositories ((I)CSDs) of the Euroclear group of companies; it owns the group's shared securities processing platforms and delivers a range of services to the group's depositories
- **hasLegalFormAbbreviation**: Societe Anonyme/Naamloze Vennootschap
- **hasLegalName**: Euroclear SA/NV

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
