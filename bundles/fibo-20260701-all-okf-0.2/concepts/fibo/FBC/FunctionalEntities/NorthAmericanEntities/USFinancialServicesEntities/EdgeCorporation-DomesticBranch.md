---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: edge corporation - domestic branch
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: branch of an edge corporation that is located in the United States
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-EBR
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isPartOf
    value: N1d99548dfe714ba898976adacdaec28d
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Organizations/isDomiciledIn
    value: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/Branch.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/Branch
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/EdgeCorporation-DomesticBranch
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
title: edge corporation - domestic branch
type: Ontology Class
---

# edge corporation - domestic branch

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/EdgeCorporation-DomesticBranch>

## Definition

branch of an edge corporation that is located in the United States

## Relationships

- **Subclass of**: [Branch](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/Branch.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-EBR`
- **[isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)**: some values from value `N1d99548dfe714ba898976adacdaec28d`
- **[isDomiciledIn](<https://www.omg.org/spec/Commons/Organizations/isDomiciledIn>)**: has value value `https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica`

## Annotations

- **label**: edge corporation - domestic branch
- **definition**: branch of an edge corporation that is located in the United States
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
