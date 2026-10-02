---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: publication
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: document offered for general distribution and usually produced in multiple copies
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 5127:2017, Information and documentation - Foundation and vocabulary
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A publication can be anything made public by print (such as a newspaper, magazine, pamphlet, letter, telegram,
      via computer modem or program, or in a poster, brochure or pamphlet), orally, or by broadcast (radio, television).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Document
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publication
sources:
- id: fibo-source-c08bba6665
  resource: references/fibo/BE/FunctionalEntities/Publishers.rdf
  sha256: c08bba6665f5e8fa0f777c7625413d35aa10a63353e739c085127bbbe73c5d28
  title: FIBO source BE/FunctionalEntities/Publishers.rdf
title: publication
type: Ontology Class
---

# publication

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publication>

## Definition

document offered for general distribution and usually produced in multiple copies

## Relationships

- **Subclass of**: [Document](<https://www.omg.org/spec/Commons/Documents/Document>)

## Annotations

- **label**: publication
- **definition**: document offered for general distribution and usually produced in multiple copies
- **adaptedFrom**: ISO 5127:2017, Information and documentation - Foundation and vocabulary
- **explanatoryNote**: A publication can be anything made public by print (such as a newspaper, magazine, pamphlet, letter, telegram, via computer modem or program, or in a poster, brochure or pamphlet), orally, or by broadcast (radio, television).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
