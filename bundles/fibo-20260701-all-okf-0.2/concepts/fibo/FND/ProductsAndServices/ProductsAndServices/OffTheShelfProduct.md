---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: off-the-shelf product
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: product that is readily available from merchandise in stock, or can be quickly and easily configured to order,
      not specially designed or custom-made
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: COTS product
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: commercial off-the-shelf product
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: commercially available off-the-shelf product
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/OffTheShelfProduct
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: off-the-shelf product
type: Ontology Class
---

# off-the-shelf product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/OffTheShelfProduct>

## Definition

product that is readily available from merchandise in stock, or can be quickly and easily configured to order, not specially designed or custom-made

## Relationships

- **Subclass of**: [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)

## Annotations

- **label**: off-the-shelf product
- **definition**: product that is readily available from merchandise in stock, or can be quickly and easily configured to order, not specially designed or custom-made
- **abbreviation**: COTS product
- **synonym**: commercial off-the-shelf product
- **synonym**: commercially available off-the-shelf product

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
