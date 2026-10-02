---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: multilateral contract
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract where multiple parties (i.e., more than two) commit to perform specific actions or obligations towards
      each other
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/MultilateralAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/MultilateralAgreement
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MultilateralContract
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: multilateral contract
type: Ontology Class
---

# multilateral contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MultilateralContract>

## Definition

contract where multiple parties (i.e., more than two) commit to perform specific actions or obligations towards each other

## Relationships

- **Subclass of**: [MultilateralAgreement](/concepts/fibo/FND/Agreements/Agreements/MultilateralAgreement.md)
- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Annotations

- **label**: multilateral contract
- **definition**: contract where multiple parties (i.e., more than two) commit to perform specific actions or obligations towards each other

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
