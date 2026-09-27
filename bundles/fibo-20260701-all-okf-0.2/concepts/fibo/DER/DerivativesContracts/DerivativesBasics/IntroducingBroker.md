---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: introducing broker
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: broker that solicits or accepts orders for derivatives that are traded on or subject to the rules of an exchange
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: IB
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.cftc.gov/IndustryOversight/Intermediaries/index.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Introducing brokers do not accept money, securities, or property (or extend credit in lieu thereof) to margin,
      guarantee, or secure any trades or contracts that result or may result.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Broker.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Broker
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/IntroducingBroker
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: introducing broker
type: Ontology Class
---

# introducing broker

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/IntroducingBroker>

## Definition

broker that solicits or accepts orders for derivatives that are traded on or subject to the rules of an exchange

## Relationships

- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)
- **Subclass of**: [Broker](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Broker.md)

## Annotations

- **label**: introducing broker
- **definition**: broker that solicits or accepts orders for derivatives that are traded on or subject to the rules of an exchange
- **abbreviation**: IB
- **adaptedFrom**: http://www.cftc.gov/IndustryOversight/Intermediaries/index.htm
- **explanatoryNote**: Introducing brokers do not accept money, securities, or property (or extend credit in lieu thereof) to margin, guarantee, or secure any trades or contracts that result or may result.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
