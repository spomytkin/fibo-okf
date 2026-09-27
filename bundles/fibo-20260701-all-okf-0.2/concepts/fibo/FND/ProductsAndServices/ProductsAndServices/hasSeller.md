---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has seller
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the vendor in the context of a sales transaction
  range:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Seller.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Seller
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasSeller
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: has seller
type: Ontology Property
---

# has seller

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasSeller>

## Definition

indicates the vendor in the context of a sales transaction

## Relationships

- **Range**: [Seller](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Seller.md)
- **Subproperty of**: [hasActor](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor>)

## Annotations

- **label** (en): has seller
- **definition**: indicates the vendor in the context of a sales transaction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
