---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: payer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a party who pays a bill or fees, or who makes payments to a payee in partial or complete fulfillment of an obligation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/hasObligation
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Obligor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligor
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payer
sources:
- id: fibo-source-53130861ea
  resource: references/fibo/FND/ProductsAndServices/PaymentsAndSchedules.rdf
  sha256: 53130861eac6d2084e3ddb6496db6123d851e37aa0259feed44cd96fd48920cf
  title: FIBO source FND/ProductsAndServices/PaymentsAndSchedules.rdf
title: payer
type: Ontology Class
---

# payer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payer>

## Definition

a party who pays a bill or fees, or who makes payments to a payee in partial or complete fulfillment of an obligation

## Relationships

- **Subclass of**: [Obligor](/concepts/fibo/FND/Agreements/Agreements/Obligor.md)

## Constraints

- **[hasObligation](/concepts/fibo/FND/Agreements/Agreements/hasObligation.md)**: all values from of type [PaymentObligation](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation.md)

## Annotations

- **label**: payer
- **definition**: a party who pays a bill or fees, or who makes payments to a payee in partial or complete fulfillment of an obligation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
