---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: regional government
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: administrative body for a geographic area, such as a county, smaller town, or other similar community
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A local government will typically only have control over their specific geographical region, and cannot pass or
      enforce laws that will affect a wider area. Local governments can elect officials, enact taxes, and do many other things
      that a national government would do, just on a smaller scale.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: local government
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Government.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Government
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/RegionalGovernment
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: regional government
type: Ontology Class
---

# regional government

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/RegionalGovernment>

## Definition

administrative body for a geographic area, such as a county, smaller town, or other similar community

## Relationships

- **Subclass of**: [Government](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Government.md)

## Constraints

- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [GeopoliticalEntity](<https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity>)

## Annotations

- **label**: regional government
- **definition**: administrative body for a geographic area, such as a county, smaller town, or other similar community
- **explanatoryNote**: A local government will typically only have control over their specific geographical region, and cannot pass or enforce laws that will affect a wider area. Local governments can elect officials, enact taxes, and do many other things that a national government would do, just on a smaller scale.
- **synonym**: local government

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
