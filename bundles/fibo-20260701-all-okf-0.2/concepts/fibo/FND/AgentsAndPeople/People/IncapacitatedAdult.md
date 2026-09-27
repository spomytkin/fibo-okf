---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: incapacitated adult
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an adult who is legally identified as not having legal capacity, typically as a result of some inherent physical
      or mental incapacity or as a result of having contracted some illness which temporarily deprives them of such capacity
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://en.wikipedia.org/wiki/Capacity_(law)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Individuals may have an inherent physical condition which prevents them from achieving the normal levels of performance
      expected from persons of comparable age, or their inability to match current levels of performance may be caused by
      contracting an illness. Whatever the cause, if the resulting condition is such that individuals cannot care for themselves,
      or may act in ways that are against their interests, those persons are vulnerable through dependency and require the
      protection of the state against the risks of abuse or exploitation. Hence, any agreements that were made are voidable,
      and a court may declare that person a ward of the state and grant power of attorney to an appointed legal guardian.
  disjoint_with:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/LegallyCapableAdult.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/LegallyCapableAdult
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Adult.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Adult
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IncapacitatedAdult
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: incapacitated adult
type: Ontology Class
---

# incapacitated adult

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IncapacitatedAdult>

## Definition

an adult who is legally identified as not having legal capacity, typically as a result of some inherent physical or mental incapacity or as a result of having contracted some illness which temporarily deprives them of such capacity

## Relationships

- **Subclass of**: [Adult](/concepts/fibo/FND/AgentsAndPeople/People/Adult.md)

## Constraints

- **Disjoint with**: [LegallyCapableAdult](/concepts/fibo/FND/AgentsAndPeople/People/LegallyCapableAdult.md)

## Annotations

- **label**: incapacitated adult
- **definition**: an adult who is legally identified as not having legal capacity, typically as a result of some inherent physical or mental incapacity or as a result of having contracted some illness which temporarily deprives them of such capacity
- **adaptedFrom**: https://en.wikipedia.org/wiki/Capacity_(law)
- **explanatoryNote**: Individuals may have an inherent physical condition which prevents them from achieving the normal levels of performance expected from persons of comparable age, or their inability to match current levels of performance may be caused by contracting an illness. Whatever the cause, if the resulting condition is such that individuals cannot care for themselves, or may act in ways that are against their interests, those persons are vulnerable through dependency and require the protection of the state against the risks of abuse or exploitation. Hence, any agreements that were made are voidable, and a court may declare that person a ward of the state and grant power of attorney to an appointed legal guardian.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
