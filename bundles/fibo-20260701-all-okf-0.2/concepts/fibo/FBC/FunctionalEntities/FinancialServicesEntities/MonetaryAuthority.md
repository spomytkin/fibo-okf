---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: monetary authority
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: regulatory agency that controls the monetary policy, regulation and supply of money in some country or group of
      countries
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: a central bank, the executive branch of a government, a central bank for several nations, a currency board
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investordictionary.com/definition/monetary-authority
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/regulatesSupplyOf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/MonetaryAuthority
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: monetary authority
type: Ontology Class
---

# monetary authority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/MonetaryAuthority>

## Definition

regulatory agency that controls the monetary policy, regulation and supply of money in some country or group of countries

## Relationships

- **Subclass of**: [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)

## Constraints

- **[regulatesSupplyOf](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/regulatesSupplyOf.md)**: some values from of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label**: monetary authority
- **definition**: regulatory agency that controls the monetary policy, regulation and supply of money in some country or group of countries
- **example**: a central bank, the executive branch of a government, a central bank for several nations, a currency board
- **adaptedFrom**: http://www.investordictionary.com/definition/monetary-authority

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
