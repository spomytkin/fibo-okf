---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: self-regulating organization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: non-governmental organization that has the power to create and exercise some degree of regulatory authority over
      an industry or profession in some country or group of countries
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SRO
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NonGovernmentalOrganization
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/SelfRegulatingOrganization
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: self-regulating organization
type: Ontology Class
---

# self-regulating organization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/SelfRegulatingOrganization>

## Definition

non-governmental organization that has the power to create and exercise some degree of regulatory authority over an industry or profession in some country or group of countries

## Relationships

- **Subclass of**: [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [NonGovernmentalOrganization](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/NonGovernmentalOrganization.md)

## Annotations

- **label**: self-regulating organization
- **definition**: non-governmental organization that has the power to create and exercise some degree of regulatory authority over an industry or profession in some country or group of countries
- **abbreviation**: SRO

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
