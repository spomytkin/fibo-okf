---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: payment event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an event that involves delivery of money in fulfillment of an obligation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payment
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/involves
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentEvent
sources:
- id: fibo-source-53130861ea
  resource: references/fibo/FND/ProductsAndServices/PaymentsAndSchedules.rdf
  sha256: 53130861eac6d2084e3ddb6496db6123d851e37aa0259feed44cd96fd48920cf
  title: FIBO source FND/ProductsAndServices/PaymentsAndSchedules.rdf
title: payment event
type: Ontology Class
---

# payment event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentEvent>

## Definition

an event that involves delivery of money in fulfillment of an obligation

## Relationships

- **Subclass of**: [TransactionEvent](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md)

## Constraints

- **[involves](/concepts/fibo/FND/Relations/Relations/involves.md)**: exact qualified cardinality 1 of type [Payment](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payment.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: exact qualified cardinality 1 of type [PaymentObligation](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation.md)

## Annotations

- **label**: payment event
- **definition**: an event that involves delivery of money in fulfillment of an obligation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
