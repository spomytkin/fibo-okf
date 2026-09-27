---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: involves merchant
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the merchant (seller) involved in the transaction
  range:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/Merchant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Merchant
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/involves.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/involves
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/involvesMerchant
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: involves merchant
type: Ontology Property
---

# involves merchant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/involvesMerchant>

## Definition

indicates the merchant (seller) involved in the transaction

## Relationships

- **Range**: [Merchant](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/Merchant.md)
- **Subproperty of**: [involves](/concepts/fibo/FND/Relations/Relations/involves.md)

## Annotations

- **label**: involves merchant
- **definition**: indicates the merchant (seller) involved in the transaction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
