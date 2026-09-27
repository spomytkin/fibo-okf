---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: risk pooling institution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution that provides some financial service while spreading the financial risk inherent in that
      service to lower the probability of a catastrophic financial event by aggregating customers across diverse dimensions
      as a risk management practice
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Insurance companies are the most common form of risk pooling institution.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.worldbank.org/en/publication/gfdr/gfdr-2016/background/nonbank-financial-institution
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/RiskPoolingInstitution
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: risk pooling institution
type: Ontology Class
---

# risk pooling institution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/RiskPoolingInstitution>

## Definition

financial institution that provides some financial service while spreading the financial risk inherent in that service to lower the probability of a catastrophic financial event by aggregating customers across diverse dimensions as a risk management practice

## Relationships

- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)

## Annotations

- **label**: risk pooling institution
- **definition**: financial institution that provides some financial service while spreading the financial risk inherent in that service to lower the probability of a catastrophic financial event by aggregating customers across diverse dimensions as a risk management practice
- **example**: Insurance companies are the most common form of risk pooling institution.
- **adaptedFrom**: https://www.worldbank.org/en/publication/gfdr/gfdr-2016/background/nonbank-financial-institution

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
