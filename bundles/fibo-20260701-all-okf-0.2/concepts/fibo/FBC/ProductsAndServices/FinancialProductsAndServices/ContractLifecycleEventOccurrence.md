---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract lifecycle event occurrence
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: actual occurrence of an event during a specific stage of a specific contract lifecycle
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStageOccurrence
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleEventOccurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleEventOccurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: contract lifecycle event occurrence
type: Ontology Class
---

# contract lifecycle event occurrence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence>

## Definition

actual occurrence of an event during a specific stage of a specific contract lifecycle

## Relationships

- **Subclass of**: [LifecycleEventOccurrence](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleEventOccurrence.md)

## Constraints

- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [ContractLifecycleEvent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [ContractLifecycleEvent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [ContractLifecycleStageOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStageOccurrence.md)

## Annotations

- **label**: contract lifecycle event occurrence
- **definition**: actual occurrence of an event during a specific stage of a specific contract lifecycle

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
