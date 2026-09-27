---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Canadian credit union
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: not-for-profit financial institution, typically formed by the employees of a company, labor union, or religious
      group, operated as a cooperative association organized for the purpose of promoting thrift among its members and creating
      a source of credit for provident or productive purposes
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.investopedia.com/terms/c/creditunion.asp
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CreditUnion.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CreditUnion
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CAFinancialServicesEntities/CanadianCreditUnion
sources:
- id: fibo-source-71b2e78204
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CAFinancialServicesEntities.rdf
  sha256: 71b2e78204a9772413bd836fdb53f48c80c90c1e195e3be33ffd7dda62399d1e
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/CAFinancialServicesEntities.rdf
title: Canadian credit union
type: Ontology Class
---

# Canadian credit union

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CAFinancialServicesEntities/CanadianCreditUnion>

## Definition

not-for-profit financial institution, typically formed by the employees of a company, labor union, or religious group, operated as a cooperative association organized for the purpose of promoting thrift among its members and creating a source of credit for provident or productive purposes

## Relationships

- **See also**: [creditunion.asp](<http://www.investopedia.com/terms/c/creditunion.asp>)
- **Subclass of**: [CreditUnion](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CreditUnion.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1

## Annotations

- **label**: Canadian credit union
- **definition**: not-for-profit financial institution, typically formed by the employees of a company, labor union, or religious group, operated as a cooperative association organized for the purpose of promoting thrift among its members and creating a source of credit for provident or productive purposes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
