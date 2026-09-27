---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non-depository trust company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: trust company that accepts and executes trusts, but does not issue currency; non-depository trust companies can
      either be Federal Reserve Members or Federal Reserve Non-members
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/TrustCompany.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/TrustCompany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NonDepositoryTrustCompany
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: non-depository trust company
type: Ontology Class
---

# non-depository trust company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NonDepositoryTrustCompany>

## Definition

trust company that accepts and executes trusts, but does not issue currency; non-depository trust companies can either be Federal Reserve Members or Federal Reserve Non-members

## Relationships

- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)
- **Subclass of**: [TrustCompany](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/TrustCompany.md)

## Annotations

- **label**: non-depository trust company
- **definition**: trust company that accepts and executes trusts, but does not issue currency; non-depository trust companies can either be Federal Reserve Members or Federal Reserve Non-members
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
