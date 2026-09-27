---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: paying party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party responsible for making payments in a transaction specified in a contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payer
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Buyer
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/PayingParty
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: paying party
type: Ontology Class
---

# paying party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/PayingParty>

## Definition

party responsible for making payments in a transaction specified in a contract

## Relationships

- **Subclass of**: [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)
- **Subclass of**: [Payer](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md)
- **Subclass of**: [Buyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md)

## Annotations

- **label**: paying party
- **definition**: party responsible for making payments in a transaction specified in a contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
