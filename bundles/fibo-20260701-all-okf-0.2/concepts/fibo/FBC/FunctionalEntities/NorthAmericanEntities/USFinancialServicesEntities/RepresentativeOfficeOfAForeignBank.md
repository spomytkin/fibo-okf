---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: representative office of a foreign bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: office of a foreign bank which is located in any state and is not a federal branch, federal agency, state branch,
      state agency, or commercial lending company subsidiary
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-211/subpart-B/section-211.21
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: representative office
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticBranchOfAForeignBank.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticBranchOfAForeignBank
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-REP
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/AgencyOfAForeignBankingOrganization
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/CommercialLendingCompany
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/OfficeOfAForeignBank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/OfficeOfAForeignBank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/RepresentativeOfficeOfAForeignBank
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
title: representative office of a foreign bank
type: Ontology Class
---

# representative office of a foreign bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/RepresentativeOfficeOfAForeignBank>

## Definition

office of a foreign bank which is located in any state and is not a federal branch, federal agency, state branch, state agency, or commercial lending company subsidiary

## Relationships

- **Subclass of**: [OfficeOfAForeignBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/OfficeOfAForeignBank.md)

## Constraints

- **Disjoint with**: [DomesticBranchOfAForeignBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticBranchOfAForeignBank.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-REP`
- **[playsRole](<https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole>)**: some values from of type [AgencyOfAForeignBankingOrganization](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/AgencyOfAForeignBankingOrganization.md)
- **[playsRole](<https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole>)**: some values from of type [CommercialLendingCompany](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/CommercialLendingCompany.md)

## Annotations

- **label**: representative office of a foreign bank
- **definition**: office of a foreign bank which is located in any state and is not a federal branch, federal agency, state branch, state agency, or commercial lending company subsidiary
- **adaptedFrom**: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-211/subpart-B/section-211.21
- **synonym**: representative office

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
