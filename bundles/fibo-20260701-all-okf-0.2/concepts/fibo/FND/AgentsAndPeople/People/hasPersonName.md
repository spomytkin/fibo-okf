---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has person name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a name to an individual
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the concept of a person name may include symbology as long as the symbols are properly encoded. Because
      person name is a class, other iconography or symbology that cannot be encoded in UTF-8 can, alternatively, be linked
      or attached as a separate image or in another form.
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Designators/hasTextualName
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPersonName
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has person name
type: Ontology Property
---

# has person name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPersonName>

## Definition

links a name to an individual

## Relationships

- **Subproperty of**: [hasTextualName](<https://www.omg.org/spec/Commons/Designators/hasTextualName>)

## Annotations

- **label**: has person name
- **definition**: links a name to an individual
- **explanatoryNote**: Note that the concept of a person name may include symbology as long as the symbols are properly encoded. Because person name is a class, other iconography or symbology that cannot be encoded in UTF-8 can, alternatively, be linked or attached as a separate image or in another form.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
