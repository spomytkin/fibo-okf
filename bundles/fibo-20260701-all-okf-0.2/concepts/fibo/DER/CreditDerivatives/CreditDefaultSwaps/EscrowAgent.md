---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: escrow agent
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: third party that holds an asset or funds before they are formally transferred from one party to another party,
      per the terms of a contract, within some specified time period and/or when a triggering event occurs
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Use of an escrow agent is one possible mechanism that may be used in some cases, as specified in a credit default
      swap contract, for delivery purposes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/EscrowAgent
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: escrow agent
type: Ontology Class
---

# escrow agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/EscrowAgent>

## Definition

third party that holds an asset or funds before they are formally transferred from one party to another party, per the terms of a contract, within some specified time period and/or when a triggering event occurs

## Relationships

- **Subclass of**: [RegisteredAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md)
- **Subclass of**: [ContractThirdParty](/concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md)

## Constraints

- **[holds](/concepts/fibo/FND/Relations/Relations/holds.md)**: some values from of type [DeliverableObligation](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation.md)

## Annotations

- **label** (en): escrow agent
- **definition** (en): third party that holds an asset or funds before they are formally transferred from one party to another party, per the terms of a contract, within some specified time period and/or when a triggering event occurs
- **explanatoryNote** (en): Use of an escrow agent is one possible mechanism that may be used in some cases, as specified in a credit default swap contract, for delivery purposes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
