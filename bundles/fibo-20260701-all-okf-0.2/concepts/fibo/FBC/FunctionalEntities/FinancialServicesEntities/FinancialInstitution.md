---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial institution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial service provider identified as either a government agency or privately owned entity that collects funds
      from the public and from other institutions, and invests those funds in financial assets, such as loans, securities,
      bank deposits, and income-generating property
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Banking Terms, Sixth Edition, 2012
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Financial institutions are differentiated by the way they obtain and invest funds. Depository institutions accept
      public deposits, which are insured by the government against loss, and channel those deposits into lending activities.
      Non-depository institutions, such as brokerage firms, life insurance companies, pension funds, and investment companies,
      fund their investment activities directly from financial markets by selling securities to the public or by selling insurance
      policies, in the case of insurance companies.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: financial intermediary
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/provides
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isRegulatedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: financial institution
type: Ontology Class
---

# financial institution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution>

## Definition

financial service provider identified as either a government agency or privately owned entity that collects funds from the public and from other institutions, and invests those funds in financial assets, such as loans, securities, bank deposits, and income-generating property

## Relationships

- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Constraints

- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: some values from of type [FinancialService](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)
- **[isRegulatedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isRegulatedBy>)**: some values from of type [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)

## Annotations

- **label**: financial institution
- **definition**: financial service provider identified as either a government agency or privately owned entity that collects funds from the public and from other institutions, and invests those funds in financial assets, such as loans, securities, bank deposits, and income-generating property
- **adaptedFrom**: Barron's Dictionary of Banking Terms, Sixth Edition, 2012
- **explanatoryNote**: Financial institutions are differentiated by the way they obtain and invest funds. Depository institutions accept public deposits, which are insured by the government against loss, and channel those deposits into lending activities. Non-depository institutions, such as brokerage firms, life insurance companies, pension funds, and investment companies, fund their investment activities directly from financial markets by selling securities to the public or by selling insurance policies, in the case of insurance companies.
- **synonym**: financial intermediary

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
