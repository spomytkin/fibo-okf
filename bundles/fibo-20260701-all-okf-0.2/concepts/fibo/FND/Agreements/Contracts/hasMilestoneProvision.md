---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has milestone provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: refers to a requirement included in an agreement related to fulfillment as of some point in time in the lifetime
      of the contract
  domain:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Agreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
  range:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractMilestone.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractMilestone
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasMilestoneProvision
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has milestone provision
type: Ontology Property
---

# has milestone provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasMilestoneProvision>

## Definition

refers to a requirement included in an agreement related to fulfillment as of some point in time in the lifetime of the contract

## Relationships

- **Domain**: [Agreement](/concepts/fibo/FND/Agreements/Agreements/Agreement.md)
- **Range**: [ContractMilestone](/concepts/fibo/FND/Agreements/Contracts/ContractMilestone.md)
- **Subproperty of**: [hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)

## Annotations

- **label**: has milestone provision
- **definition**: refers to a requirement included in an agreement related to fulfillment as of some point in time in the lifetime of the contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
