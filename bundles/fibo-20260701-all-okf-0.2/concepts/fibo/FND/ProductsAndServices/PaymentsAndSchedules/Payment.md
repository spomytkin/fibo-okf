---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: payment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: delivery of money in fulfillment of an obligation, such as to satisfy a claim or debt
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentAmount
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payment
sources:
- id: fibo-source-53130861ea
  resource: references/fibo/FND/ProductsAndServices/PaymentsAndSchedules.rdf
  sha256: 53130861eac6d2084e3ddb6496db6123d851e37aa0259feed44cd96fd48920cf
  title: FIBO source FND/ProductsAndServices/PaymentsAndSchedules.rdf
title: payment
type: Ontology Class
---

# payment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payment>

## Definition

delivery of money in fulfillment of an obligation, such as to satisfy a claim or debt

## Relationships

- **Subclass of**: [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Constraints

- **[hasPaymentAmount](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentAmount.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: payment
- **definition**: delivery of money in fulfillment of an obligation, such as to satisfy a claim or debt

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
