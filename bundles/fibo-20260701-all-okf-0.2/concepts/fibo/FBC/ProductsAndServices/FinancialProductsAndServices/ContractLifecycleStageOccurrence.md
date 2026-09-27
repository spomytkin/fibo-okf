---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract lifecycle stage occurrence
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: realization, from start to finish of a phase in an occurrence of a specific contract lifecycle
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleOccurrence
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isStageOf
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStageOccurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStageOccurrence
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: contract lifecycle stage occurrence
type: Ontology Class
---

# contract lifecycle stage occurrence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStageOccurrence>

## Definition

realization, from start to finish of a phase in an occurrence of a specific contract lifecycle

## Relationships

- **Subclass of**: [LifecycleStageOccurrence](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md)

## Constraints

- **[isStageOf](/concepts/fibo/FND/Arrangements/Lifecycles/isStageOf.md)**: some values from of type [ContractLifecycleOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleOccurrence.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [ContractLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [ContractLifecycleEventOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md)

## Annotations

- **label**: contract lifecycle stage occurrence
- **definition**: realization, from start to finish of a phase in an occurrence of a specific contract lifecycle

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
