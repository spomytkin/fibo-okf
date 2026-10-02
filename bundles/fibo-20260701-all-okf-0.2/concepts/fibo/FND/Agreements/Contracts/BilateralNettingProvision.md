---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bilateral netting provision
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: netting provision that occurs between two parties, in which mutual obligations are offset to determine a single
      net payment
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/BilateralContract
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/NettingProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NettingProvision
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/BilateralNettingProvision
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: bilateral netting provision
type: Ontology Class
---

# bilateral netting provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/BilateralNettingProvision>

## Definition

netting provision that occurs between two parties, in which mutual obligations are offset to determine a single net payment

## Relationships

- **Subclass of**: [NettingProvision](/concepts/fibo/FND/Agreements/Contracts/NettingProvision.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [BilateralContract](/concepts/fibo/FND/Agreements/Contracts/BilateralContract.md)

## Annotations

- **label** (en): bilateral netting provision
- **definition** (en): netting provision that occurs between two parties, in which mutual obligations are offset to determine a single net payment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
