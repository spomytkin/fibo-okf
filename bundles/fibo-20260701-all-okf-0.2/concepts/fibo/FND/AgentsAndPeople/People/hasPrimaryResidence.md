---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has primary residence
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a dwelling where an individual resides the majority of the year
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For tax purposes, in cases when an individual owns more than one home, their primary residence is the home in which
      they reside most of the time, and for which they can provide evidence to that effect. Having said this, there are cases,
      such as for individuals that have dual citizenship, where they may have multiple primary residences, one in each country
      in which they maintain a home. There may also be subtle issues related to 'rent control' that may impact the statements
      an individual makes about their primary residence. In other words, one cannot necessarily infer a person's identity
      from their primary place of residence.
  domain:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/hasResidence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasResidence
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPrimaryResidence
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has primary residence
type: Ontology Property
---

# has primary residence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPrimaryResidence>

## Definition

identifies a dwelling where an individual resides the majority of the year

## Relationships

- **Domain**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)
- **Range**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)
- **Subproperty of**: [hasResidence](/concepts/fibo/FND/AgentsAndPeople/People/hasResidence.md)

## Annotations

- **label**: has primary residence
- **definition**: identifies a dwelling where an individual resides the majority of the year
- **explanatoryNote**: For tax purposes, in cases when an individual owns more than one home, their primary residence is the home in which they reside most of the time, and for which they can provide evidence to that effect. Having said this, there are cases, such as for individuals that have dual citizenship, where they may have multiple primary residences, one in each country in which they maintain a home. There may also be subtle issues related to 'rent control' that may impact the statements an individual makes about their primary residence. In other words, one cannot necessarily infer a person's identity from their primary place of residence.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
