---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: government
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system by which a state or community is controlled
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the Commonwealth of Nations, the word government is also used more narrowly to refer to the collective group
      of people that exercises executive authority in a state. This usage is analogous to what is called an 'administration'
      in American English. Furthermore, especially in American English, the concepts of the state and the government may be
      used synonymously to refer to the person or group of people exercising authority over a politically organized territory.
  disjoint_with:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Instrumentality.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Instrumentality
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Government
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: government
type: Ontology Class
---

# government

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Government>

## Definition

system by which a state or community is controlled

## Relationships

- **Subclass of**: [FunctionalEntity](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity.md)

## Constraints

- **Disjoint with**: [Instrumentality](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Instrumentality.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: min qualified cardinality 0
- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [GeopoliticalEntity](<https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity>)

## Annotations

- **label**: government
- **definition**: system by which a state or community is controlled
- **explanatoryNote**: In the Commonwealth of Nations, the word government is also used more narrowly to refer to the collective group of people that exercises executive authority in a state. This usage is analogous to what is called an 'administration' in American English. Furthermore, especially in American English, the concepts of the state and the government may be used synonymously to refer to the person or group of people exercising authority over a politically organized territory.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
