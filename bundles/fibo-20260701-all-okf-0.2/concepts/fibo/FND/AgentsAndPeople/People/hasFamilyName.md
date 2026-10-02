---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has family name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the name shared in common to identify the members of a family, as distinguished from each member's given
      name
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: '''Family name'' is more commonly used in the United Kingdom than in the United States to refer to someone''s surname.'
  equivalent_to:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/hasLastName.md
    predicate: http://www.w3.org/2002/07/owl#equivalentProperty
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasLastName
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/hasSurname.md
    predicate: http://www.w3.org/2002/07/owl#equivalentProperty
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasSurname
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/hasPersonName.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPersonName
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasFamilyName
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has family name
type: Ontology Property
---

# has family name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasFamilyName>

## Definition

indicates the name shared in common to identify the members of a family, as distinguished from each member's given name

## Relationships

- **Equivalent to**: [hasLastName](/concepts/fibo/FND/AgentsAndPeople/People/hasLastName.md)
- **Equivalent to**: [hasSurname](/concepts/fibo/FND/AgentsAndPeople/People/hasSurname.md)
- **Subproperty of**: [hasPersonName](/concepts/fibo/FND/AgentsAndPeople/People/hasPersonName.md)

## Annotations

- **label**: has family name
- **definition**: indicates the name shared in common to identify the members of a family, as distinguished from each member's given name
- **explanatoryNote**: 'Family name' is more commonly used in the United Kingdom than in the United States to refer to someone's surname.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
