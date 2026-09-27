---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: insured federal branch of foreign banking organization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any office or any place of business of a foreign bank located in any State of the United States at which deposits
      are received established and operating under section 4 of the International Banking Act of 1978 that is insured and
      regulated by the Federal Deposit Insurance Corporation (FDIC)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.govinfo.gov/content/pkg/COMPS-275/pdf/COMPS-275.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-IFB
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FederalBranchOfForeignBankingOrganization.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FederalBranchOfForeignBankingOrganization
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/InsuredFederalBranchOfForeignBankingOrganization
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
title: insured federal branch of foreign banking organization
type: Ontology Class
---

# insured federal branch of foreign banking organization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/InsuredFederalBranchOfForeignBankingOrganization>

## Definition

any office or any place of business of a foreign bank located in any State of the United States at which deposits are received established and operating under section 4 of the International Banking Act of 1978 that is insured and regulated by the Federal Deposit Insurance Corporation (FDIC)

## Relationships

- **Subclass of**: [FederalBranchOfForeignBankingOrganization](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FederalBranchOfForeignBankingOrganization.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-IFB`

## Annotations

- **label**: insured federal branch of foreign banking organization
- **definition**: any office or any place of business of a foreign bank located in any State of the United States at which deposits are received established and operating under section 4 of the International Banking Act of 1978 that is insured and regulated by the Federal Deposit Insurance Corporation (FDIC)
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes
- **adaptedFrom**: https://www.govinfo.gov/content/pkg/COMPS-275/pdf/COMPS-275.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
