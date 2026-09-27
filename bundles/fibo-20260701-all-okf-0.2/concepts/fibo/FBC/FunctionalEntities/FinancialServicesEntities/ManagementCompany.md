---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: management company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment company that sells and manages a portfolio of securities other than a face-amount certificate company
      or unit investment fund
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: Section 4, definition of investment companies, Investment Company Act of 1940 as amended and approved as of 3 January
      2012, see https://www.sec.gov/about/laws/ica40.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Management companies allow investors to pool their capital with that of other investors in order to purchase professionally-managed
      groups of diversified securities.
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/UnitInvestmentTrust.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/UnitInvestmentTrust
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ManagementCompany
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: management company
type: Ontology Class
---

# management company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ManagementCompany>

## Definition

investment company that sells and manages a portfolio of securities other than a face-amount certificate company or unit investment fund

## Relationships

- **Subclass of**: [InvestmentCompany](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany.md)

## Constraints

- **Disjoint with**: [UnitInvestmentTrust](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/UnitInvestmentTrust.md)

## Annotations

- **label**: management company
- **definition**: investment company that sells and manages a portfolio of securities other than a face-amount certificate company or unit investment fund
- **definitionOrigin**: Section 4, definition of investment companies, Investment Company Act of 1940 as amended and approved as of 3 January 2012, see https://www.sec.gov/about/laws/ica40.pdf
- **explanatoryNote**: Management companies allow investors to pool their capital with that of other investors in order to purchase professionally-managed groups of diversified securities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
