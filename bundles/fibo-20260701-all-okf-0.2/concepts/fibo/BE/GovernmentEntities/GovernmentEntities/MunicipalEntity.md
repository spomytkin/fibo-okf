---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: municipal entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: polity that typically represents a city, township, or other administrative subdivision having corporate status
      and powers of self-government or jurisdiction
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Municipal entity in the sense of a legal entity, that is, what it is that incurs debt for a municipality, as distinct
      from the Municipal government. A municipal entity has a Government which sets laws applicable within the geographical
      area corresponding to its jurisdiction.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: municipality
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Locations/Municipality
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/hasSovereigntyOver
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/MunicipalGovernment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Polity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/MunicipalEntity
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: municipal entity
type: Ontology Class
---

# municipal entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/MunicipalEntity>

## Definition

polity that typically represents a city, township, or other administrative subdivision having corporate status and powers of self-government or jurisdiction

## Relationships

- **Subclass of**: [Polity](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md)

## Constraints

- **[hasSovereigntyOver](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/hasSovereigntyOver.md)**: some values from of type [Municipality](<https://www.omg.org/spec/Commons/Locations/Municipality>)
- **[isRepresentedBy](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy.md)**: some values from of type [MunicipalGovernment](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/MunicipalGovernment.md)

## Annotations

- **label**: municipal entity
- **definition**: polity that typically represents a city, township, or other administrative subdivision having corporate status and powers of self-government or jurisdiction
- **explanatoryNote**: Municipal entity in the sense of a legal entity, that is, what it is that incurs debt for a municipality, as distinct from the Municipal government. A municipal entity has a Government which sets laws applicable within the geographical area corresponding to its jurisdiction.
- **synonym**: municipality

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
