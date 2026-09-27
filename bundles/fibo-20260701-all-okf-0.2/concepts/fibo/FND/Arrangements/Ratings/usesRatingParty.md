---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: uses rating performer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rating performer an issuer uses to assess ratings
  domain:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingIssuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingIssuer
  range:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/isProducedBy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isProducedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/usesRatingParty
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: uses rating performer
type: Ontology Property
---

# uses rating performer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/usesRatingParty>

## Definition

rating performer an issuer uses to assess ratings

## Relationships

- **Domain**: [RatingIssuer](/concepts/fibo/FND/Arrangements/Ratings/RatingIssuer.md)
- **Range**: [RatingParty](/concepts/fibo/FND/Arrangements/Ratings/RatingParty.md)
- **Subproperty of**: [isProducedBy](/concepts/fibo/FND/Relations/Relations/isProducedBy.md)

## Annotations

- **label**: uses rating performer
- **definition**: rating performer an issuer uses to assess ratings

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
