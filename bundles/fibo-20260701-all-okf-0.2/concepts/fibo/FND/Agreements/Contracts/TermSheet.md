---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: term sheet
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: nonbinding agreement setting forth the basic terms and conditions under which a proposed business deal may be made
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Term sheets state the intentions of the parties and are used to guide legal counsel in the preparation of proposed
      agreements or contracts.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NonBindingTerm
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasNonBindingTerm
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Agreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/TermSheet
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: term sheet
type: Ontology Class
---

# term sheet

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/TermSheet>

## Definition

nonbinding agreement setting forth the basic terms and conditions under which a proposed business deal may be made

## Relationships

- **Subclass of**: [Agreement](/concepts/fibo/FND/Agreements/Agreements/Agreement.md)

## Constraints

- **[hasNonBindingTerm](/concepts/fibo/FND/Agreements/Contracts/hasNonBindingTerm.md)**: some values from of type [NonBindingTerm](/concepts/fibo/FND/Agreements/Contracts/NonBindingTerm.md)

## Annotations

- **label**: term sheet
- **definition**: nonbinding agreement setting forth the basic terms and conditions under which a proposed business deal may be made
- **explanatoryNote**: Term sheets state the intentions of the parties and are used to guide legal counsel in the preparation of proposed agreements or contracts.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
