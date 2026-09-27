---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Federal Reserve System non-member institution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depository institution that is not member of the Federal Reserve System (FRS)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A non-member bank is a commercial bank that is state-chartered and NOT a member of the Federal Reserve System.
      It includes all insured commercial banks and industrial banks.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: non-member bank
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystemMember.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystemMember
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-NMB
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nbf742bf0f738449898469bfc3a4e9792
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystemNonMemberInstitution
sources:
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Federal Reserve System non-member institution
type: Ontology Class
---

# Federal Reserve System non-member institution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystemNonMemberInstitution>

## Definition

depository institution that is not member of the Federal Reserve System (FRS)

## Relationships

- **Subclass of**: [DepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)

## Constraints

- **Disjoint with**: [FederalReserveSystemMember](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystemMember.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-NMB`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nbf742bf0f738449898469bfc3a4e9792`

## Annotations

- **label**: Federal Reserve System non-member institution
- **definition**: depository institution that is not member of the Federal Reserve System (FRS)
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes
- **explanatoryNote**: A non-member bank is a commercial bank that is state-chartered and NOT a member of the Federal Reserve System. It includes all insured commercial banks and industrial banks.
- **synonym**: non-member bank

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
