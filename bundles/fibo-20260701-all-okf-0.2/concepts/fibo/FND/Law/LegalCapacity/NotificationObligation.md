---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: notification obligation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: requirement for one party to formally inform another party (or parties) about specific events, actions, or changes
      as outlined in the agreement
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Common triggering events include breaches, changes in circumstances, delays, or other kinds of events that may
      have a material impact on the agreement.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/ContingentObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentObligation
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/NotificationObligation
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: notification obligation
type: Ontology Class
---

# notification obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/NotificationObligation>

## Definition

requirement for one party to formally inform another party (or parties) about specific events, actions, or changes as outlined in the agreement

## Relationships

- **Subclass of**: [ContingentObligation](/concepts/fibo/FND/Law/LegalCapacity/ContingentObligation.md)
- **Subclass of**: [LegalObligation](/concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md)

## Annotations

- **label** (en): notification obligation
- **definition** (en): requirement for one party to formally inform another party (or parties) about specific events, actions, or changes as outlined in the agreement
- **explanatoryNote** (en): Common triggering events include breaches, changes in circumstances, delays, or other kinds of events that may have a material impact on the agreement.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
