---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fulfills obligation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: satisfies a requirement for payment of some claim, debt, or other obligation
  domain:
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payment
  range:
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/fulfillsObligation
sources:
- id: fibo-source-53130861ea
  resource: references/fibo/FND/ProductsAndServices/PaymentsAndSchedules.rdf
  sha256: 53130861eac6d2084e3ddb6496db6123d851e37aa0259feed44cd96fd48920cf
  title: FIBO source FND/ProductsAndServices/PaymentsAndSchedules.rdf
title: fulfills obligation
type: Ontology Property
---

# fulfills obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/fulfillsObligation>

## Definition

satisfies a requirement for payment of some claim, debt, or other obligation

## Relationships

- **Domain**: [Payment](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payment.md)
- **Range**: [PaymentObligation](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation.md)

## Annotations

- **label**: fulfills obligation
- **definition**: satisfies a requirement for payment of some claim, debt, or other obligation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
