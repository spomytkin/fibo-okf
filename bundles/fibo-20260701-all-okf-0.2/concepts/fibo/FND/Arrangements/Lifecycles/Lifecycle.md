---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lifecycle
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: arrangement that compares the cyclical nature of families, organizations, processes, products, marketing, and order
      management, portfolio management or other systems with the cradle to grave life stages (birth, growth, maturity, decay,
      and death) of living organisms
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'The product life cycle describes the period of time over which an item is developed, brought to market and eventually
      removed from the market. The cycle is broken into four stages: introduction, growth, maturity and decline. The idea
      of the product life cycle is used in marketing to decide when it is appropriate to advertise, reduce prices, explore
      new markets or create new packaging.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  - filler: http://www.w3.org/2002/07/owl#Thing
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isLifecycleOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Arrangement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/Lifecycle
sources:
- id: fibo-source-92efc72f29
  resource: references/fibo/FND/Arrangements/Lifecycles.rdf
  sha256: 92efc72f29aba7c64208722174530078a5a46ad575d7ceabbf0cd9a444ad5e0e
  title: FIBO source FND/Arrangements/Lifecycles.rdf
title: lifecycle
type: Ontology Class
---

# lifecycle

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/Lifecycle>

## Definition

arrangement that compares the cyclical nature of families, organizations, processes, products, marketing, and order management, portfolio management or other systems with the cradle to grave life stages (birth, growth, maturity, decay, and death) of living organisms

## Relationships

- **Subclass of**: [Arrangement](<https://www.omg.org/spec/Commons/Collections/Arrangement>)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [LifecycleStage](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md)
- **[isLifecycleOf](/concepts/fibo/FND/Arrangements/Lifecycles/isLifecycleOf.md)**: some values from of type [Thing](<http://www.w3.org/2002/07/owl#Thing>)
- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [LifecycleStage](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md)

## Annotations

- **label**: lifecycle
- **definition**: arrangement that compares the cyclical nature of families, organizations, processes, products, marketing, and order management, portfolio management or other systems with the cradle to grave life stages (birth, growth, maturity, decay, and death) of living organisms
- **example**: The product life cycle describes the period of time over which an item is developed, brought to market and eventually removed from the market. The cycle is broken into four stages: introduction, growth, maturity and decline. The idea of the product life cycle is used in marketing to decide when it is appropriate to advertise, reduce prices, explore new markets or create new packaging.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
