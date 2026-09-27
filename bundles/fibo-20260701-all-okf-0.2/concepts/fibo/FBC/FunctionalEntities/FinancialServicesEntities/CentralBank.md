---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: central bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution that is the monetary authority and major regulatory bank for a country (or group of countries)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Its functions include issuing and managing the country's currency, controlling monetary policy and supervising
      money market operations, managing exchange and gold reserves, acting as lender of last resort to commercial banks, and
      providing banking services to the government. Central banks are state-controlled but are increasingly being given an
      independent status to insulate them from partisan politics.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Instrumentality
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Bank
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/MonetaryAuthority.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/MonetaryAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralBank
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: central bank
type: Ontology Class
---

# central bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralBank>

## Definition

financial institution that is the monetary authority and major regulatory bank for a country (or group of countries)

## Relationships

- **Subclass of**: [Bank](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md)
- **Subclass of**: [MonetaryAuthority](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/MonetaryAuthority.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: all values from of type [Instrumentality](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Instrumentality.md)

## Annotations

- **label**: central bank
- **definition**: financial institution that is the monetary authority and major regulatory bank for a country (or group of countries)
- **explanatoryNote**: Its functions include issuing and managing the country's currency, controlling monetary policy and supervising money market operations, managing exchange and gold reserves, acting as lender of last resort to commercial banks, and providing banking services to the government. Central banks are state-controlled but are increasingly being given an independent status to insulate them from partisan politics.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
