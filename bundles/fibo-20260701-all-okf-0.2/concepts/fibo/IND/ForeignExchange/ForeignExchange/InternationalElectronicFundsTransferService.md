---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: international electronic funds transfer service
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: electronic funds transfer (EFT) service involving the transfer of funds across national borders, that may also
      involve currency conversion
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: international wire transfer
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ElectronicFundsTransferService.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ElectronicFundsTransferService
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/ForeignExchangeService.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/ForeignExchangeService
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/InternationalElectronicFundsTransferService
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: international electronic funds transfer service
type: Ontology Class
---

# international electronic funds transfer service

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/InternationalElectronicFundsTransferService>

## Definition

electronic funds transfer (EFT) service involving the transfer of funds across national borders, that may also involve currency conversion

## Relationships

- **Subclass of**: [ElectronicFundsTransferService](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ElectronicFundsTransferService.md)
- **Subclass of**: [ForeignExchangeService](/concepts/fibo/IND/ForeignExchange/ForeignExchange/ForeignExchangeService.md)

## Annotations

- **label**: international electronic funds transfer service
- **definition**: electronic funds transfer (EFT) service involving the transfer of funds across national borders, that may also involve currency conversion
- **synonym**: international wire transfer

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
