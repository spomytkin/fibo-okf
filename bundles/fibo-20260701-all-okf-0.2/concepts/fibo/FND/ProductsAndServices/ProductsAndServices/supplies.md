---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: supplies
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a party in the role of outfitter, provisioner, distributor, etc. to something that they provide
  domain:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Supplier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Supplier
  range:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Organizations/provides
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/supplies
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: supplies
type: Ontology Property
---

# supplies

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/supplies>

## Definition

links a party in the role of outfitter, provisioner, distributor, etc. to something that they provide

## Relationships

- **Domain**: [Supplier](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Supplier.md)
- **Range**: [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)
- **Subproperty of**: [provides](<https://www.omg.org/spec/Commons/Organizations/provides>)

## Annotations

- **label**: supplies
- **definition**: links a party in the role of outfitter, provisioner, distributor, etc. to something that they provide

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
