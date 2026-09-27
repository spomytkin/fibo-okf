---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tribal entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal entity that represents fundamental unit of sovereign tribal (indigenous) government
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Any indigenous group or community which is recognized as having rights and obligations independent of the central
      government.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/TribalArea
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/hasSharedSovereigntyOver
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/TribalGovernment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Polity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/TribalEntity
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: tribal entity
type: Ontology Class
---

# tribal entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/TribalEntity>

## Definition

legal entity that represents fundamental unit of sovereign tribal (indigenous) government

## Relationships

- **Subclass of**: [Polity](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md)

## Constraints

- **[hasSharedSovereigntyOver](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/hasSharedSovereigntyOver.md)**: some values from of type [TribalArea](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/TribalArea.md)
- **[isRepresentedBy](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy.md)**: some values from of type [TribalGovernment](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/TribalGovernment.md)

## Annotations

- **label**: tribal entity
- **definition**: legal entity that represents fundamental unit of sovereign tribal (indigenous) government
- **explanatoryNote**: Any indigenous group or community which is recognized as having rights and obligations independent of the central government.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
