---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is subordinate to
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the primary contract referenced by a subordinate agreement, such as a collateral agreement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This property may also be used as the basis for linking agreements based on priority, such as linking a second
      or junior lien to the primary lien on some collateral
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
  range:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/refersTo
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isSubordinateTo
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: is subordinate to
type: Ontology Property
---

# is subordinate to

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isSubordinateTo>

## Definition

indicates the primary contract referenced by a subordinate agreement, such as a collateral agreement

## Relationships

- **Domain**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)
- **Range**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)
- **Subproperty of**: [refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)

## Annotations

- **label**: is subordinate to
- **definition**: indicates the primary contract referenced by a subordinate agreement, such as a collateral agreement
- **explanatoryNote**: This property may also be used as the basis for linking agreements based on priority, such as linking a second or junior lien to the primary lien on some collateral

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
