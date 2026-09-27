---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract lifecycle occurrence
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: realization of the lifecycle of a specific contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStageOccurrence
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycle
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleOccurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleOccurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleOccurrence
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: contract lifecycle occurrence
type: Ontology Class
---

# contract lifecycle occurrence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleOccurrence>

## Definition

realization of the lifecycle of a specific contract

## Relationships

- **Subclass of**: [LifecycleOccurrence](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleOccurrence.md)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [ContractLifecycleStageOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStageOccurrence.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [ContractLifecycle](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycle.md)

## Annotations

- **label**: contract lifecycle occurrence
- **definition**: realization of the lifecycle of a specific contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
