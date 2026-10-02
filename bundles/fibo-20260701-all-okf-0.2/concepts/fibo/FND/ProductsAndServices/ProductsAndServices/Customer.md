---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: customer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that receives or consumes products (goods or services) and has the ability to choose between different products
      and suppliers
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Supplier
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/buysFrom
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Buyer
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Customer
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: customer
type: Ontology Class
---

# customer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Customer>

## Definition

party that receives or consumes products (goods or services) and has the ability to choose between different products and suppliers

## Relationships

- **Subclass of**: [Buyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md)

## Constraints

- **[buysFrom](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/buysFrom.md)**: some values from of type [Supplier](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Supplier.md)

## Annotations

- **label**: customer
- **definition**: party that receives or consumes products (goods or services) and has the ability to choose between different products and suppliers

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
