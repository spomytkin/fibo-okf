---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: brokerage firm
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: firm in the business of buying and selling securities, operating as both a broker and a dealer, depending on the
      transaction
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: Office of Financial Research (OFR) Annual Report, 2012, Glossary
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.worldbank.org/en/publication/gfdr/gfdr-2016/background/nonbank-financial-institution
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The term broker-dealer is used in U.S. securities regulation parlance to describe stock brokerages, because most
      of them act as both agents and principals. A brokerage acts as a broker (or agent) when it executes orders on behalf
      of clients, whereas it acts as a dealer (or principal) when it trades for its own account.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: market maker
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/BrokerDealer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/BrokerDealer
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BrokerageFirm
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: brokerage firm
type: Ontology Class
---

# brokerage firm

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BrokerageFirm>

## Definition

firm in the business of buying and selling securities, operating as both a broker and a dealer, depending on the transaction

## Relationships

- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)
- **Subclass of**: [BrokerDealer](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/BrokerDealer.md)

## Annotations

- **label**: brokerage firm
- **definition**: firm in the business of buying and selling securities, operating as both a broker and a dealer, depending on the transaction
- **definitionOrigin**: Office of Financial Research (OFR) Annual Report, 2012, Glossary
- **adaptedFrom**: https://www.worldbank.org/en/publication/gfdr/gfdr-2016/background/nonbank-financial-institution
- **explanatoryNote**: The term broker-dealer is used in U.S. securities regulation parlance to describe stock brokerages, because most of them act as both agents and principals. A brokerage acts as a broker (or agent) when it executes orders on behalf of clients, whereas it acts as a dealer (or principal) when it trades for its own account.
- **synonym**: market maker

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
