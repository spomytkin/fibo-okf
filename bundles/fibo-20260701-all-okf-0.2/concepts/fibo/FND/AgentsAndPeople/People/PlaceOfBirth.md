---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: place of birth
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: physical location, including country, region, and municipality where an individual was born
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: birth place
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Locations/PhysicalLocation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PlaceOfBirth
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: place of birth
type: Ontology Class
---

# place of birth

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PlaceOfBirth>

## Definition

physical location, including country, region, and municipality where an individual was born

## Relationships

- **Subclass of**: [PhysicalLocation](<https://www.omg.org/spec/Commons/Locations/PhysicalLocation>)

## Annotations

- **label**: place of birth
- **definition**: physical location, including country, region, and municipality where an individual was born
- **synonym**: birth place

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
