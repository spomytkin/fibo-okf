---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: broker
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any party that acts as an intermediary between a buyer and a seller, usually charging a commission
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 17 CFR 45.1, Definitions - see the definition of agent
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A broker that specializes in stocks, bonds, commodities, or certain derivatives must be registered with the exchange
      in which the securities are traded.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Broker
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: broker
type: Ontology Class
---

# broker

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Broker>

## Definition

any party that acts as an intermediary between a buyer and a seller, usually charging a commission

## Relationships

- **Subclass of**: [ContractThirdParty](/concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md)

## Annotations

- **label**: broker
- **definition**: any party that acts as an intermediary between a buyer and a seller, usually charging a commission
- **adaptedFrom**: 17 CFR 45.1, Definitions - see the definition of agent
- **explanatoryNote**: A broker that specializes in stocks, bonds, commodities, or certain derivatives must be registered with the exchange in which the securities are traded.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
