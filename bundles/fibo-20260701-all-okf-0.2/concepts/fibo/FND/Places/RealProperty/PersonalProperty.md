---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: personal property
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: asset that is a movable item or possession not fixed to land
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Personal property may include tangible assets, such as machinery, furniture, vehicles, artwork, and jewelry, regardless
      of whether such assets are owned by a person or organization, and intangible assets, including but not limited to intellectual
      property and financial instruments.
  disjoint_with:
  - concept: /concepts/fibo/FND/Places/RealProperty/RealProperty.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraisal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isEvaluatedBy
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/PersonalProperty
sources:
- id: fibo-source-f0e5ecd06c
  resource: references/fibo/FND/Places/RealProperty.rdf
  sha256: f0e5ecd06c164d1e5fff0c1236869b2014bcba3d7008365dcc2c7363064202bd
  title: FIBO source FND/Places/RealProperty.rdf
title: personal property
type: Ontology Class
---

# personal property

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/PersonalProperty>

## Definition

asset that is a movable item or possession not fixed to land

## Relationships

- **Subclass of**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)

## Constraints

- **Disjoint with**: [RealProperty](/concepts/fibo/FND/Places/RealProperty/RealProperty.md)
- **[isEvaluatedBy](/concepts/fibo/FND/Relations/Relations/isEvaluatedBy.md)**: min qualified cardinality 0 of type [Appraisal](/concepts/fibo/FND/Arrangements/Assessments/Appraisal.md)

## Annotations

- **label** (en): personal property
- **definition** (en): asset that is a movable item or possession not fixed to land
- **explanatoryNote** (en): Personal property may include tangible assets, such as machinery, furniture, vehicles, artwork, and jewelry, regardless of whether such assets are owned by a person or organization, and intangible assets, including but not limited to intellectual property and financial instruments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
