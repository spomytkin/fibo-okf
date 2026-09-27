---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rating issuer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that is responsible for issuing ratings
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A rating issuer is frequently, but not always the rating scale publisher. A rating issuer may delegate responsibility
      for producing a rating to a rating party.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/Rating
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/issues
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingIssuer
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: rating issuer
type: Ontology Class
---

# rating issuer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingIssuer>

## Definition

party that is responsible for issuing ratings

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[issues](/concepts/fibo/FND/Relations/Relations/issues.md)**: some values from of type [Rating](/concepts/fibo/FND/Arrangements/Ratings/Rating.md)

## Annotations

- **label**: rating issuer
- **definition**: party that is responsible for issuing ratings
- **explanatoryNote**: A rating issuer is frequently, but not always the rating scale publisher. A rating issuer may delegate responsibility for producing a rating to a rating party.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
