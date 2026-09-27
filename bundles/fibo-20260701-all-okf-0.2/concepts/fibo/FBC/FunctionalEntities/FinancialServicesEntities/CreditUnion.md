---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit union
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: not-for-profit depository institution that makes personal loans and offers other consumer banking services, organized
      for the purpose of promoting thrift among its members and creating a source of credit for provident or productive purposes
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/CooperativeSociety.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/CooperativeSociety
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CreditUnion
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: credit union
type: Ontology Class
---

# credit union

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CreditUnion>

## Definition

not-for-profit depository institution that makes personal loans and offers other consumer banking services, organized for the purpose of promoting thrift among its members and creating a source of credit for provident or productive purposes

## Relationships

- **Subclass of**: [CooperativeSociety](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/CooperativeSociety.md)
- **Subclass of**: [DepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [NotForProfitOrganization](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization.md)

## Annotations

- **label**: credit union
- **definition**: not-for-profit depository institution that makes personal loans and offers other consumer banking services, organized for the purpose of promoting thrift among its members and creating a source of credit for provident or productive purposes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
