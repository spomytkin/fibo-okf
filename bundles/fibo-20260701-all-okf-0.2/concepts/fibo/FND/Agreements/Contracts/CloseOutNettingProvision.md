---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: close-out netting provision
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: netting provision that may be triggered when a counterparty defaults, leading to the termination of all outstanding
      transactions between the parties
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the case of close-out netting, the financial positions of the defaulting party are assessed to determine their
      worth, and total amounts owed are offset, resulting in a single net payment obligation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: close out netting provision
  disjoint_with:
  - concept: /concepts/fibo/FND/Agreements/Contracts/SettlementNettingProvision.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/SettlementNettingProvision
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/NettingProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NettingProvision
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/CloseOutNettingProvision
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: close-out netting provision
type: Ontology Class
---

# close-out netting provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/CloseOutNettingProvision>

## Definition

netting provision that may be triggered when a counterparty defaults, leading to the termination of all outstanding transactions between the parties

## Relationships

- **Subclass of**: [NettingProvision](/concepts/fibo/FND/Agreements/Contracts/NettingProvision.md)

## Constraints

- **Disjoint with**: [SettlementNettingProvision](/concepts/fibo/FND/Agreements/Contracts/SettlementNettingProvision.md)

## Annotations

- **label** (en): close-out netting provision
- **definition** (en): netting provision that may be triggered when a counterparty defaults, leading to the termination of all outstanding transactions between the parties
- **explanatoryNote**: In the case of close-out netting, the financial positions of the defaulting party are assessed to determine their worth, and total amounts owed are offset, resulting in a single net payment obligation.
- **synonym**: close out netting provision

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
