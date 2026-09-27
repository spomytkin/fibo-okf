---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is supplied by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the party (supplier, vendor, distributor, etc.) that makes a product available
  domain:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
  inverse_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/supplies.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/supplies
  range:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Supplier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Supplier
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/isSuppliedBy
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: is supplied by
type: Ontology Property
---

# is supplied by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/isSuppliedBy>

## Definition

identifies the party (supplier, vendor, distributor, etc.) that makes a product available

## Relationships

- **Domain**: [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)
- **Inverse of**: [supplies](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/supplies.md)
- **Range**: [Supplier](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Supplier.md)
- **Subproperty of**: [isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)

## Annotations

- **label**: is supplied by
- **definition**: identifies the party (supplier, vendor, distributor, etc.) that makes a product available

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
