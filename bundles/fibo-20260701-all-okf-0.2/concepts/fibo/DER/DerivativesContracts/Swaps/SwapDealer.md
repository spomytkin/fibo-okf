---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: swap dealer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: non-depository institution such as one that deals in swaps, makes a market in swaps, regularly enters into swaps
      with counterparties as an ordinary course of business for its own account, and engages in any activity causing the person
      to be commonly known in the trade as a dealer/market maker in swaps
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SD
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.cftc.gov/IndustryOversight/Intermediaries/index.htm
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Dealer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Dealer
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapDealer
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: swap dealer
type: Ontology Class
---

# swap dealer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapDealer>

## Definition

non-depository institution such as one that deals in swaps, makes a market in swaps, regularly enters into swaps with counterparties as an ordinary course of business for its own account, and engages in any activity causing the person to be commonly known in the trade as a dealer/market maker in swaps

## Relationships

- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)
- **Subclass of**: [Dealer](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Dealer.md)

## Annotations

- **label**: swap dealer
- **definition**: non-depository institution such as one that deals in swaps, makes a market in swaps, regularly enters into swaps with counterparties as an ordinary course of business for its own account, and engages in any activity causing the person to be commonly known in the trade as a dealer/market maker in swaps
- **abbreviation**: SD
- **adaptedFrom**: http://www.cftc.gov/IndustryOversight/Intermediaries/index.htm

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
