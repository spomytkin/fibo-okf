---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has non-binding term
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: refers to a term that is included in an agreement that is not considered legally binding
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In other words, a breach of such terms in the future would not be considered to be a breach of the contract.
  domain:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Agreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
  range:
  - concept: /concepts/fibo/FND/Agreements/Contracts/NonBindingTerm.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NonBindingTerm
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasNonBindingTerm
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has non-binding term
type: Ontology Property
---

# has non-binding term

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasNonBindingTerm>

## Definition

refers to a term that is included in an agreement that is not considered legally binding

## Relationships

- **Domain**: [Agreement](/concepts/fibo/FND/Agreements/Agreements/Agreement.md)
- **Range**: [NonBindingTerm](/concepts/fibo/FND/Agreements/Contracts/NonBindingTerm.md)
- **Subproperty of**: [hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)

## Annotations

- **label**: has non-binding term
- **definition**: refers to a term that is included in an agreement that is not considered legally binding
- **explanatoryNote**: In other words, a breach of such terms in the future would not be considered to be a breach of the contract.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
