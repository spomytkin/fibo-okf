---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract lifecycle
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: lifecycle of an agreement, including, but not limited to a credit agreement, financial instrument, or other formal
      contract, from initial stages through retirement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Certain business agreements, such as partnership agreements,may involve planning, drafting/review/revision, execution
      and management, renewal, and possibly sunsetting phases. Financial contracts, such as loans and other instruments have
      specific stages and events during the execution and management phase, i.e. from the effective date of the contract through
      maturity and redemption.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isLifecycleOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/Lifecycle
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycle
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: contract lifecycle
type: Ontology Class
---

# contract lifecycle

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycle>

## Definition

lifecycle of an agreement, including, but not limited to a credit agreement, financial instrument, or other formal contract, from initial stages through retirement

## Relationships

- **Subclass of**: [Lifecycle](/concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [ContractLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage.md)
- **[isLifecycleOf](/concepts/fibo/FND/Arrangements/Lifecycles/isLifecycleOf.md)**: some values from of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [ContractLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage.md)

## Annotations

- **label**: contract lifecycle
- **definition**: lifecycle of an agreement, including, but not limited to a credit agreement, financial instrument, or other formal contract, from initial stages through retirement
- **explanatoryNote**: Certain business agreements, such as partnership agreements,may involve planning, drafting/review/revision, execution and management, renewal, and possibly sunsetting phases. Financial contracts, such as loans and other instruments have specific stages and events during the execution and management phase, i.e. from the effective date of the contract through maturity and redemption.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
