---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: deliverable obligation buyer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract party that is obliged to purchase a deliverable obligation (asset) if a triggering event occurs, depending
      on the event and the contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Buyer
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligationBuyer
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: deliverable obligation buyer
type: Ontology Class
---

# deliverable obligation buyer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligationBuyer>

## Definition

contract party that is obliged to purchase a deliverable obligation (asset) if a triggering event occurs, depending on the event and the contract

## Relationships

- **Subclass of**: [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)
- **Subclass of**: [Buyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md)

## Annotations

- **label** (en): deliverable obligation buyer
- **definition** (en): contract party that is obliged to purchase a deliverable obligation (asset) if a triggering event occurs, depending on the event and the contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
