---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: CRD credit institution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an undertaking whose business is to receive deposits or other repayable funds from the public and to grant credits
      for its own account as defined by the European Banking Authority (EBA)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: http://www.eba.europa.eu/risk-analysis-and-data/credit-institutions-register
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/EuropeanEconomicAreaBranch.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/EuropeanEconomicAreaBranch
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/NonEuropeanEconomicAreaBranch.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/NonEuropeanEconomicAreaBranch
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CRDCreditInstitution
sources:
- id: fibo-source-760f05a832
  resource: references/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
  sha256: 760f05a8322c75aaef31b7b35eefe1470b4bd58ea40a9be94100e8fe641fce43
  title: FIBO source FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
title: CRD credit institution
type: Ontology Class
---

# CRD credit institution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CRDCreditInstitution>

## Definition

an undertaking whose business is to receive deposits or other repayable funds from the public and to grant credits for its own account as defined by the European Banking Authority (EBA)

## Relationships

- **Subclass of**: [CreditInstitution](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution.md)

## Constraints

- **Disjoint with**: [EuropeanEconomicAreaBranch](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/EuropeanEconomicAreaBranch.md)
- **Disjoint with**: [NonEuropeanEconomicAreaBranch](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/NonEuropeanEconomicAreaBranch.md)

## Annotations

- **label**: CRD credit institution
- **definition**: an undertaking whose business is to receive deposits or other repayable funds from the public and to grant credits for its own account as defined by the European Banking Authority (EBA)
- **definitionOrigin**: http://www.eba.europa.eu/risk-analysis-and-data/credit-institutions-register

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
