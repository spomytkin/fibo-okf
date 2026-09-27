---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non-depository trust company - non-member institution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: non-depository trust company that is not a member of the Federal Reserve system
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NonDepositoryTrustCompany-MemberInstitution.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NonDepositoryTrustCompany-MemberInstitution
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-NTC
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NonDepositoryTrustCompany.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NonDepositoryTrustCompany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NonDepositoryTrustCompany-NonMemberInstitution
sources:
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: non-depository trust company - non-member institution
type: Ontology Class
---

# non-depository trust company - non-member institution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NonDepositoryTrustCompany-NonMemberInstitution>

## Definition

non-depository trust company that is not a member of the Federal Reserve system

## Relationships

- **Subclass of**: [NonDepositoryTrustCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NonDepositoryTrustCompany.md)

## Constraints

- **Disjoint with**: [NonDepositoryTrustCompany-MemberInstitution](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NonDepositoryTrustCompany-MemberInstitution.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-NTC`

## Annotations

- **label**: non-depository trust company - non-member institution
- **definition**: non-depository trust company that is not a member of the Federal Reserve system
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
