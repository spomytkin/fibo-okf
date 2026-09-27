---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: multilateral netting provision
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: netting provision that, when triggered, is facilitated by a central clearinghouse or financial institution
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Rather than settling individual obligations between each party, as in bilateral netting, all transactions are aggregated,
      and a single net amount is determined for each participant.
  disjoint_with:
  - concept: /concepts/fibo/FND/Agreements/Contracts/BilateralNettingProvision.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/BilateralNettingProvision
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MultilateralContract
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/NettingProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NettingProvision
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MultilateralNettingProvision
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: multilateral netting provision
type: Ontology Class
---

# multilateral netting provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MultilateralNettingProvision>

## Definition

netting provision that, when triggered, is facilitated by a central clearinghouse or financial institution

## Relationships

- **Subclass of**: [NettingProvision](/concepts/fibo/FND/Agreements/Contracts/NettingProvision.md)

## Constraints

- **Disjoint with**: [BilateralNettingProvision](/concepts/fibo/FND/Agreements/Contracts/BilateralNettingProvision.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [MultilateralContract](/concepts/fibo/FND/Agreements/Contracts/MultilateralContract.md)

## Annotations

- **label** (en): multilateral netting provision
- **definition** (en): netting provision that, when triggered, is facilitated by a central clearinghouse or financial institution
- **explanatoryNote**: Rather than settling individual obligations between each party, as in bilateral netting, all transactions are aggregated, and a single net amount is determined for each participant.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
