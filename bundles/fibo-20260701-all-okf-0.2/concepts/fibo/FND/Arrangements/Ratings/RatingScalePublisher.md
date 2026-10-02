---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rating scale publisher
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party responsible for managing one or more rating schemes and potentially publishing ratings based on those schemes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Rating scale publishers are frequently also rating agencies.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScale
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/manages
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScalePublisher
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: rating scale publisher
type: Ontology Class
---

# rating scale publisher

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScalePublisher>

## Definition

party responsible for managing one or more rating schemes and potentially publishing ratings based on those schemes

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[manages](<https://www.omg.org/spec/Commons/Organizations/manages>)**: some values from of type [RatingScale](/concepts/fibo/FND/Arrangements/Ratings/RatingScale.md)

## Annotations

- **label**: rating scale publisher
- **definition**: party responsible for managing one or more rating schemes and potentially publishing ratings based on those schemes
- **explanatoryNote**: Rating scale publishers are frequently also rating agencies.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
