---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: face amount certificate company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment company which is engaged or proposes to engage in the business of issuing face-amount certificates of
      the installment type, or which has been engaged in such business and has any such certificate outstanding
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: Section 4, definition of investment companies, Investment Company Act of 1940 as amended and approved as of 3 January
      2012, see https://www.sec.gov/about/laws/ica40.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An investor may enter into a contract with an issuer of a face amount certificate to contract to receive a stated
      or fixed amount of money (the face amount) at a stated date in the future. In exchange for this future sum, the investor
      must deposit an agreed lump sum or make scheduled installment payments over time. Face amount certificates are rarely
      issued these days, as most of the tax advantages that the investment once offered have been lost through changes in
      the tax laws.
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ManagementCompany.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ManagementCompany
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FaceAmountCertificateCompany
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: face amount certificate company
type: Ontology Class
---

# face amount certificate company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FaceAmountCertificateCompany>

## Definition

investment company which is engaged or proposes to engage in the business of issuing face-amount certificates of the installment type, or which has been engaged in such business and has any such certificate outstanding

## Relationships

- **Subclass of**: [InvestmentCompany](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany.md)

## Constraints

- **Disjoint with**: [ManagementCompany](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ManagementCompany.md)

## Annotations

- **label**: face amount certificate company
- **definition**: investment company which is engaged or proposes to engage in the business of issuing face-amount certificates of the installment type, or which has been engaged in such business and has any such certificate outstanding
- **definitionOrigin**: Section 4, definition of investment companies, Investment Company Act of 1940 as amended and approved as of 3 January 2012, see https://www.sec.gov/about/laws/ica40.pdf
- **explanatoryNote**: An investor may enter into a contract with an issuer of a face amount certificate to contract to receive a stated or fixed amount of money (the face amount) at a stated date in the future. In exchange for this future sum, the investor must deposit an agreed lump sum or make scheduled installment payments over time. Face amount certificates are rarely issued these days, as most of the tax advantages that the investment once offered have been lost through changes in the tax laws.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
