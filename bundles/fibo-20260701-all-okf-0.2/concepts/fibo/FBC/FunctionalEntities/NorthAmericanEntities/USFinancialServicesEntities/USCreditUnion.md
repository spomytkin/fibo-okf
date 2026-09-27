---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: U.S. credit union
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: cooperative association organized for the purpose of promoting thrift among its members and creating a source of
      credit for provident or productive purposes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: As soon as you deposit funds into a credit union account, you become a partial owner and participate in the union's
      profitability. Credit unions may be formed by large corporations and organizations for their employees and members.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/NotForProfitCorporation
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CreditUnion.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CreditUnion
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ThriftInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ThriftInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USCreditUnion
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: U.S. credit union
type: Ontology Class
---

# U.S. credit union

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USCreditUnion>

## Definition

cooperative association organized for the purpose of promoting thrift among its members and creating a source of credit for provident or productive purposes

## Relationships

- **Subclass of**: [CreditUnion](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CreditUnion.md)
- **Subclass of**: [ThriftInstitution](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ThriftInstitution.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [NotForProfitCorporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/NotForProfitCorporation.md)

## Annotations

- **label**: U.S. credit union
- **definition**: cooperative association organized for the purpose of promoting thrift among its members and creating a source of credit for provident or productive purposes
- **explanatoryNote**: As soon as you deposit funds into a credit union account, you become a partial owner and participate in the union's profitability. Credit unions may be formed by large corporations and organizations for their employees and members.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
