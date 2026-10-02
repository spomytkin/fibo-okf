---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: federal government
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: union of states under a central government distinct from the individual governments of the separate states
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A federation is a political entity characterized by a union of partially self-governing states or regions under
      a central (federal) government. In a federation, the self-governing status of the component states, as well as the division
      of power between them and the central government, are typically constitutionally entrenched and may not be altered by
      a unilateral decision of either party, the states or the federal political body.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/NationalGovernment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/NationalGovernment
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/FederalGovernment
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: federal government
type: Ontology Class
---

# federal government

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/FederalGovernment>

## Definition

union of states under a central government distinct from the individual governments of the separate states

## Relationships

- **Subclass of**: [NationalGovernment](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/NationalGovernment.md)

## Annotations

- **label**: federal government
- **definition**: union of states under a central government distinct from the individual governments of the separate states
- **explanatoryNote**: A federation is a political entity characterized by a union of partially self-governing states or regions under a central (federal) government. In a federation, the self-governing status of the component states, as well as the division of power between them and the central government, are typically constitutionally entrenched and may not be altered by a unilateral decision of either party, the states or the federal political body.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
