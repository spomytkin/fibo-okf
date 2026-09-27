---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: product lifecycle stage occurrence
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: realization of a specific stage in the lifecycle of a given product
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleOccurrence
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isStageOf
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleEventOccurrence
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStageOccurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStageOccurrence
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: product lifecycle stage occurrence
type: Ontology Class
---

# product lifecycle stage occurrence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStageOccurrence>

## Definition

realization of a specific stage in the lifecycle of a given product

## Relationships

- **Subclass of**: [LifecycleStageOccurrence](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md)

## Constraints

- **[isStageOf](/concepts/fibo/FND/Arrangements/Lifecycles/isStageOf.md)**: some values from of type [ProductLifecycleOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleOccurrence.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [ProductLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [ProductLifecycleEventOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleEventOccurrence.md)

## Annotations

- **label**: product lifecycle stage occurrence
- **definition**: realization of a specific stage in the lifecycle of a given product

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
