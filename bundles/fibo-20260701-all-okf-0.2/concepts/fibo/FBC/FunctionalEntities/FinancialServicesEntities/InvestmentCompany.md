---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investment company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'any issuer which: (a) is or holds itself out as being engaged primarily, or proposes to engage primarily, in the
      business of investing, reinvesting, or trading in securities; (b) is engaged or proposes to engage in the business of
      issuing face-amount certificates of the installment type, or has been engaged in such business and has any such certificate
      outstanding; or (c) is engaged or proposes to engage in the business of investing, reinvesting, owning, holding, or
      trading in securities, and owns or proposes to acquire investment securities having a value exceeding 40 per centum
      of the value of such issuer&apos;s total assets (exclusive of Government securities and cash items) on an unconsolidated
      basis'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: Section 3a of the Investment Company Act of 1940 as amended in January, 2012, https://www.sec.gov/about/laws/ica40.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An investment company is organized as either a corporation or as a trust. Individual investors' money is then pooled
      together in a single account and used to purchase securities that will have the greatest chance of helping the investment
      company reach its objectives. All investors jointly own the portfolio that is created through these pooled funds, and
      each investor has an undivided interest in the securities.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the US, all investment company offerings are subject to the Securities Act of 1933, which requires the investment
      company to register with the Securities Exchange Commission (SEC) and to give all purchasers a prospectus. Investment
      companies are also subject to the Investment Company Act of 1940, which sets forth guidelines on how investment companies
      must operate.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: investment company
type: Ontology Class
---

# investment company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany>

## Definition

any issuer which: (a) is or holds itself out as being engaged primarily, or proposes to engage primarily, in the business of investing, reinvesting, or trading in securities; (b) is engaged or proposes to engage in the business of issuing face-amount certificates of the installment type, or has been engaged in such business and has any such certificate outstanding; or (c) is engaged or proposes to engage in the business of investing, reinvesting, owning, holding, or trading in securities, and owns or proposes to acquire investment securities having a value exceeding 40 per centum of the value of such issuer&apos;s total assets (exclusive of Government securities and cash items) on an unconsolidated basis

## Relationships

- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)

## Annotations

- **label**: investment company
- **definition**: any issuer which: (a) is or holds itself out as being engaged primarily, or proposes to engage primarily, in the business of investing, reinvesting, or trading in securities; (b) is engaged or proposes to engage in the business of issuing face-amount certificates of the installment type, or has been engaged in such business and has any such certificate outstanding; or (c) is engaged or proposes to engage in the business of investing, reinvesting, owning, holding, or trading in securities, and owns or proposes to acquire investment securities having a value exceeding 40 per centum of the value of such issuer&apos;s total assets (exclusive of Government securities and cash items) on an unconsolidated basis
- **definitionOrigin**: Section 3a of the Investment Company Act of 1940 as amended in January, 2012, https://www.sec.gov/about/laws/ica40.pdf
- **explanatoryNote**: An investment company is organized as either a corporation or as a trust. Individual investors' money is then pooled together in a single account and used to purchase securities that will have the greatest chance of helping the investment company reach its objectives. All investors jointly own the portfolio that is created through these pooled funds, and each investor has an undivided interest in the securities.
- **explanatoryNote**: In the US, all investment company offerings are subject to the Securities Act of 1933, which requires the investment company to register with the Securities Exchange Commission (SEC) and to give all purchasers a prospectus. Investment companies are also subject to the Investment Company Act of 1940, which sets forth guidelines on how investment companies must operate.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
