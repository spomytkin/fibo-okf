---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: payee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a party to whom a debt should be paid, or to whose order a bill of exchange, note, or check is made payable, or
      who receives or will receive a payment from a payer in partial or complete fulfillment of an obligation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nb6f3fbcd37f34b8e9679c395376f4604
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Obligee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligee
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payee
sources:
- id: fibo-source-53130861ea
  resource: references/fibo/FND/ProductsAndServices/PaymentsAndSchedules.rdf
  sha256: 53130861eac6d2084e3ddb6496db6123d851e37aa0259feed44cd96fd48920cf
  title: FIBO source FND/ProductsAndServices/PaymentsAndSchedules.rdf
title: payee
type: Ontology Class
---

# payee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payee>

## Definition

a party to whom a debt should be paid, or to whose order a bill of exchange, note, or check is made payable, or who receives or will receive a payment from a payer in partial or complete fulfillment of an obligation

## Relationships

- **Subclass of**: [Obligee](/concepts/fibo/FND/Agreements/Agreements/Obligee.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nb6f3fbcd37f34b8e9679c395376f4604`

## Annotations

- **label**: payee
- **definition**: a party to whom a debt should be paid, or to whose order a bill of exchange, note, or check is made payable, or who receives or will receive a payment from a payer in partial or complete fulfillment of an obligation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
