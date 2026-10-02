---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sovereign state
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: non-physical juridical entity that is represented by one centralized government that has sovereignty over a geographic
      area
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A legal entity that is represented by one centralized government, has a permanent population, defined territory,
      and the capacity to enter into relations with other sovereign states.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Locations/Country
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/hasFullSovereigntyOver
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/NationalGovernment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Polity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/SovereignState
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: sovereign state
type: Ontology Class
---

# sovereign state

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/SovereignState>

## Definition

non-physical juridical entity that is represented by one centralized government that has sovereignty over a geographic area

## Relationships

- **Subclass of**: [Polity](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md)

## Constraints

- **[hasFullSovereigntyOver](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/hasFullSovereigntyOver.md)**: some values from of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[isRepresentedBy](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy.md)**: some values from of type [NationalGovernment](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/NationalGovernment.md)

## Annotations

- **label**: sovereign state
- **definition**: non-physical juridical entity that is represented by one centralized government that has sovereignty over a geographic area
- **explanatoryNote**: A legal entity that is represented by one centralized government, has a permanent population, defined territory, and the capacity to enter into relations with other sovereign states.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
