---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: New York Article XII investment company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specialized non-depository lending institution that has broad borrowing and lending powers and may invest in stocks
      and bonds
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.dfs.ny.gov/institution_definition
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An Article XII Investment Company is not an 'investment company' subject to registration under the Investment Company
      Act of 1940. An Article XII Investment Company may accept credit balances in New York that are incidental to the exercise
      of its other powers and may accept deposits outside New York with the approval of the Superintendent. Article XII Investment
      Companies may specialize in commercial or retail sales finance; others are involved in domestic and international commercial
      and merchant banking.
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-NYI
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NewYorkArticleXIIInvestmentCompany
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
title: New York Article XII investment company
type: Ontology Class
---

# New York Article XII investment company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NewYorkArticleXIIInvestmentCompany>

## Definition

specialized non-depository lending institution that has broad borrowing and lending powers and may invest in stocks and bonds

## Relationships

- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)

## Constraints

- **Disjoint with**: [InvestmentCompany](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-NYI`

## Annotations

- **label**: New York Article XII investment company
- **definition**: specialized non-depository lending institution that has broad borrowing and lending powers and may invest in stocks and bonds
- **adaptedFrom**: https://www.dfs.ny.gov/institution_definition
- **explanatoryNote**: An Article XII Investment Company is not an 'investment company' subject to registration under the Investment Company Act of 1940. An Article XII Investment Company may accept credit balances in New York that are incidental to the exercise of its other powers and may accept deposits outside New York with the approval of the Superintendent. Article XII Investment Companies may specialize in commercial or retail sales finance; others are involved in domestic and international commercial and merchant banking.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
