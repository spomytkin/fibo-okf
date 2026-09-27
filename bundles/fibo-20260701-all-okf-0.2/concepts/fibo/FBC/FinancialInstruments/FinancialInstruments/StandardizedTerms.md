---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: standardized terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms that, grouped together, that are generally and consistently reused across many contracts, published
      by some organization, and capable of being incorporated into a contract by reference
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Each exchange has a set of terms they apply to membership agreements and with respect to the instruments that may
      be traded on that exchange. For example, there is a set expiration date that exchanges will publish for exchange-traded
      options - in the US it is the Saturday following the third Friday of every month. Similarly, there are set incremental
      dates for strike for exchange traded options. Contract sizes are also stipulated, for example in the US these are standardized
      by the OPRA Convention (Options Pricing Reporting Authority).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: standardized terms
type: Ontology Class
---

# standardized terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms>

## Definition

contract terms that, grouped together, that are generally and consistently reused across many contracts, published by some organization, and capable of being incorporated into a contract by reference

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Annotations

- **label**: standardized terms
- **definition**: contract terms that, grouped together, that are generally and consistently reused across many contracts, published by some organization, and capable of being incorporated into a contract by reference
- **example**: Each exchange has a set of terms they apply to membership agreements and with respect to the instruments that may be traded on that exchange. For example, there is a set expiration date that exchanges will publish for exchange-traded options - in the US it is the Saturday following the third Friday of every month. Similarly, there are set incremental dates for strike for exchange traded options. Contract sizes are also stipulated, for example in the US these are standardized by the OPRA Convention (Options Pricing Reporting Authority).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
