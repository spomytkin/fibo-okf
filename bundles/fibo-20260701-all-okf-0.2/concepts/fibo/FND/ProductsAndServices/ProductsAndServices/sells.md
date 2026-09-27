---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sells
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a party in the role of broker, dealer, vendor, or merchandiser to something that they make available for
      sale
  domain:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Seller.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Seller
  range:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/sells
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: sells
type: Ontology Property
---

# sells

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/sells>

## Definition

links a party in the role of broker, dealer, vendor, or merchandiser to something that they make available for sale

## Relationships

- **Domain**: [Seller](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Seller.md)
- **Range**: [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)

## Annotations

- **label**: sells
- **definition**: links a party in the role of broker, dealer, vendor, or merchandiser to something that they make available for sale

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
