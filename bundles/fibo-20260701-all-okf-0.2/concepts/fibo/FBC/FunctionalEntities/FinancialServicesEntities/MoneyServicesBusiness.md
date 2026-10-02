---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: money services business
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'any person doing business, whether or not on a regular basis or as an organized business concern, in one of the
      following capacities: (1) currency dealer or exchanger, (2) check casher, (3) issuer of traveler''s checks, money orders,
      or stored value, (4) seller or redeemer of traveler''s checks, money orders, or stored value, (5) money transmitter,
      or (6) postal service'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: MSB
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This definition excludes banks and persons registered with or examined by the Securities and Exchange Commission
      or the Commodities Futures Trading Commission.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.fincen.gov/money-services-business-definition
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/MoneyServicesBusiness
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: money services business
type: Ontology Class
---

# money services business

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/MoneyServicesBusiness>

## Definition

any person doing business, whether or not on a regular basis or as an organized business concern, in one of the following capacities: (1) currency dealer or exchanger, (2) check casher, (3) issuer of traveler's checks, money orders, or stored value, (4) seller or redeemer of traveler's checks, money orders, or stored value, (5) money transmitter, or (6) postal service

## Relationships

- **See also**: [money-services-business-definition](<https://www.fincen.gov/money-services-business-definition>)
- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)

## Annotations

- **label**: money services business
- **definition**: any person doing business, whether or not on a regular basis or as an organized business concern, in one of the following capacities: (1) currency dealer or exchanger, (2) check casher, (3) issuer of traveler's checks, money orders, or stored value, (4) seller or redeemer of traveler's checks, money orders, or stored value, (5) money transmitter, or (6) postal service
- **abbreviation**: MSB
- **explanatoryNote**: This definition excludes banks and persons registered with or examined by the Securities and Exchange Commission or the Commodities Futures Trading Commission.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
