---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depository institution, usually a corporation, that accepts deposits, makes loans, pays checks, and performs related
      services, for individual members of the public, businesses or other organizations
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Banking Terms, Sixth Edition, 2012
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CommercialLendingService
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/provides
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/DemandDepositAccount
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/provides
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.sec.gov/about/laws/ica40.pdf
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Bank
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: bank
type: Ontology Class
---

# bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Bank>

## Definition

depository institution, usually a corporation, that accepts deposits, makes loans, pays checks, and performs related services, for individual members of the public, businesses or other organizations

## Relationships

- **See also**: [ica40.pdf](<https://www.sec.gov/about/laws/ica40.pdf>)
- **Subclass of**: [DepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)

## Constraints

- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: some values from of type [CommercialLendingService](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CommercialLendingService.md)
- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: some values from of type [DemandDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/DemandDepositAccount.md)

## Annotations

- **label**: bank
- **definition**: depository institution, usually a corporation, that accepts deposits, makes loans, pays checks, and performs related services, for individual members of the public, businesses or other organizations
- **adaptedFrom**: Barron's Dictionary of Banking Terms, Sixth Edition, 2012

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
