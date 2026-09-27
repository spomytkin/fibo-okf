---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: depository institution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any financial institution engaged in the business of receiving demand deposits from the public or other institutions
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 12 U.S. Code Section 1813 - Definitions, see, for example, http://www.law.cornell.edu/uscode/text/12/1813
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.fdic.gov/regulations/laws/rules/1000-400.html#fdic1000sec.3a
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/provides
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: depository institution
type: Ontology Class
---

# depository institution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution>

## Definition

any financial institution engaged in the business of receiving demand deposits from the public or other institutions

## Relationships

- **Subclass of**: [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Constraints

- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: some values from of type [DepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount.md)

## Annotations

- **label**: depository institution
- **definition**: any financial institution engaged in the business of receiving demand deposits from the public or other institutions
- **adaptedFrom**: 12 U.S. Code Section 1813 - Definitions, see, for example, http://www.law.cornell.edu/uscode/text/12/1813
- **adaptedFrom**: https://www.fdic.gov/regulations/laws/rules/1000-400.html#fdic1000sec.3a

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
