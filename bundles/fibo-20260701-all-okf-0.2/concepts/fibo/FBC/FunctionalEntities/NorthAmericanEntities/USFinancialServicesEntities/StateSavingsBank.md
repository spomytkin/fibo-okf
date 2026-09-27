---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: state savings bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: savings bank that has a state affiliation
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FederalSavingsBank.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FederalSavingsBank
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-SSB
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/SavingsBank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/SavingsBank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/StateSavingsBank
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
title: state savings bank
type: Ontology Class
---

# state savings bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/StateSavingsBank>

## Definition

savings bank that has a state affiliation

## Relationships

- **Subclass of**: [SavingsBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/SavingsBank.md)

## Constraints

- **Disjoint with**: [FederalSavingsBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FederalSavingsBank.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-SSB`

## Annotations

- **label**: state savings bank
- **definition**: savings bank that has a state affiliation
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
