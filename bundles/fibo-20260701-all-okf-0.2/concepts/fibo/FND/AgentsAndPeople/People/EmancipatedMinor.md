---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: emancipated minor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a minor who is allowed to conduct a business or any other occupation on his or her own behalf or for their own
      account outside the control of a parent or guardian
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://en.wikipedia.org/wiki/Emancipated_minor
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The minor will then have full contractual capacity to conclude contracts with regard to the business. Whether parental
      consent is needed to achieve emancipated status varies from case to case. In some cases, court permission is necessary.
      Protocols vary by jurisdiction.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Minor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Minor
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/EmancipatedMinor
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: emancipated minor
type: Ontology Class
---

# emancipated minor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/EmancipatedMinor>

## Definition

a minor who is allowed to conduct a business or any other occupation on his or her own behalf or for their own account outside the control of a parent or guardian

## Relationships

- **Subclass of**: [Minor](/concepts/fibo/FND/AgentsAndPeople/People/Minor.md)

## Annotations

- **label**: emancipated minor
- **definition**: a minor who is allowed to conduct a business or any other occupation on his or her own behalf or for their own account outside the control of a parent or guardian
- **adaptedFrom**: https://en.wikipedia.org/wiki/Emancipated_minor
- **explanatoryNote**: The minor will then have full contractual capacity to conclude contracts with regard to the business. Whether parental consent is needed to achieve emancipated status varies from case to case. In some cases, court permission is necessary. Protocols vary by jurisdiction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
