---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: catalog
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: publication including a list of products available for sale with their descriptions and possibly prices
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/describes
  - filler: https://www.omg.org/spec/Commons/Identifiers/Identifier
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/Publication.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publication
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Catalog
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: catalog
type: Ontology Class
---

# catalog

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Catalog>

## Definition

publication including a list of products available for sale with their descriptions and possibly prices

## Relationships

- **Subclass of**: [Publication](/concepts/fibo/BE/FunctionalEntities/Publishers/Publication.md)

## Constraints

- **[describes](<https://www.omg.org/spec/Commons/Designators/describes>)**: some values from of type [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: all values from of type [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Annotations

- **label**: catalog
- **definition**: publication including a list of products available for sale with their descriptions and possibly prices

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
