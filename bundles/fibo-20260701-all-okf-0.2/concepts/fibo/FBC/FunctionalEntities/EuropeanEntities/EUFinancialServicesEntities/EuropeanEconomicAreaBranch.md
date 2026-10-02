---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: European Economic Area branch
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a branch of a credit institution authorised in another European Economic Area (EEA) country that has the right
      to passport its activities
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: http://www.eba.europa.eu/risk-analysis-and-data/credit-institutions-register
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: EEA branch
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/NonEuropeanEconomicAreaBranch.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/NonEuropeanEconomicAreaBranch
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/EuropeanEconomicAreaBranch
sources:
- id: fibo-source-760f05a832
  resource: references/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
  sha256: 760f05a8322c75aaef31b7b35eefe1470b4bd58ea40a9be94100e8fe641fce43
  title: FIBO source FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
title: European Economic Area branch
type: Ontology Class
---

# European Economic Area branch

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/EuropeanEconomicAreaBranch>

## Definition

a branch of a credit institution authorised in another European Economic Area (EEA) country that has the right to passport its activities

## Relationships

- **Subclass of**: [CreditInstitution](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution.md)

## Constraints

- **Disjoint with**: [NonEuropeanEconomicAreaBranch](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/NonEuropeanEconomicAreaBranch.md)

## Annotations

- **label**: European Economic Area branch
- **definition**: a branch of a credit institution authorised in another European Economic Area (EEA) country that has the right to passport its activities
- **definitionOrigin**: http://www.eba.europa.eu/risk-analysis-and-data/credit-institutions-register
- **synonym**: EEA branch

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
