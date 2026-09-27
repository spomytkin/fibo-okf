---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rating agency
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rating issuer that is also a rating scale publisher, frequently but not always an independent rating service
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/FormalOrganization
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingIssuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingIssuer
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingScalePublisher.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScalePublisher
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingAgency
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: rating agency
type: Ontology Class
---

# rating agency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingAgency>

## Definition

rating issuer that is also a rating scale publisher, frequently but not always an independent rating service

## Relationships

- **Subclass of**: [RatingIssuer](/concepts/fibo/FND/Arrangements/Ratings/RatingIssuer.md)
- **Subclass of**: [RatingScalePublisher](/concepts/fibo/FND/Arrangements/Ratings/RatingScalePublisher.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [FormalOrganization](<https://www.omg.org/spec/Commons/Organizations/FormalOrganization>)

## Annotations

- **label**: rating agency
- **definition**: rating issuer that is also a rating scale publisher, frequently but not always an independent rating service

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
