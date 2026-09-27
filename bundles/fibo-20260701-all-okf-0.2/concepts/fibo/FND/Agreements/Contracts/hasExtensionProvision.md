---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has extension provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the details of a contract provision allowing extension of some aspect of the contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Typically a contract extension refers to the termination date, coverage period, or, in the case of a security,
      may refer to extension of repayment or maturity dates.
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Contract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
  range:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ExtensionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ExtensionProvision
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasExtensionProvision
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has extension provision
type: Ontology Property
---

# has extension provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasExtensionProvision>

## Definition

specifies the details of a contract provision allowing extension of some aspect of the contract

## Relationships

- **Domain**: [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **Range**: [ExtensionProvision](/concepts/fibo/FND/Agreements/Contracts/ExtensionProvision.md)
- **Subproperty of**: [hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)

## Annotations

- **label**: has extension provision
- **definition**: specifies the details of a contract provision allowing extension of some aspect of the contract
- **explanatoryNote**: Typically a contract extension refers to the termination date, coverage period, or, in the case of a security, may refer to extension of repayment or maturity dates.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
