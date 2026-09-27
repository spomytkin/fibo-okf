---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: produces ratings for
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: issuer for which ratings are produced or posted through
  domain:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingParty
  inverse_of:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/usesRatingParty.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/usesRatingParty
  range:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingIssuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingIssuer
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/produces.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/produces
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/producesRatingsFor
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: produces ratings for
type: Ontology Property
---

# produces ratings for

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/producesRatingsFor>

## Definition

issuer for which ratings are produced or posted through

## Relationships

- **Domain**: [RatingParty](/concepts/fibo/FND/Arrangements/Ratings/RatingParty.md)
- **Inverse of**: [usesRatingParty](/concepts/fibo/FND/Arrangements/Ratings/usesRatingParty.md)
- **Range**: [RatingIssuer](/concepts/fibo/FND/Arrangements/Ratings/RatingIssuer.md)
- **Subproperty of**: [produces](/concepts/fibo/FND/Relations/Relations/produces.md)

## Annotations

- **label**: produces ratings for
- **definition**: issuer for which ratings are produced or posted through

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
