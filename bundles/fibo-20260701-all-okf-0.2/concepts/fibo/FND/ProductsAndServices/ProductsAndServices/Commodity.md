---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: material resource used in commerce that is interchangeable with other commodities of the same type
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Commodities are most often used as inputs in the production of other goods or services. The quality of a given
      commodity may differ slightly, but it is essentially uniform across producers.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Good.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Good
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Commodity
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: commodity
type: Ontology Class
---

# commodity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Commodity>

## Definition

material resource used in commerce that is interchangeable with other commodities of the same type

## Relationships

- **Subclass of**: [Good](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Good.md)

## Annotations

- **label**: commodity
- **definition**: material resource used in commerce that is interchangeable with other commodities of the same type
- **explanatoryNote**: Commodities are most often used as inputs in the production of other goods or services. The quality of a given commodity may differ slightly, but it is essentially uniform across producers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
