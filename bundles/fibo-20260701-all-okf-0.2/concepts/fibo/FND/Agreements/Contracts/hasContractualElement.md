---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has contractual element
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates something that is a component of an agreement
  domain:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Agreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
  range:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualElement
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has contractual element
type: Ontology Property
---

# has contractual element

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement>

## Definition

indicates something that is a component of an agreement

## Relationships

- **Domain**: [Agreement](/concepts/fibo/FND/Agreements/Agreements/Agreement.md)
- **Range**: [ContractualElement](/concepts/fibo/FND/Agreements/Contracts/ContractualElement.md)
- **Subproperty of**: [comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)

## Annotations

- **label**: has contractual element
- **definition**: indicates something that is a component of an agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
