---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has rating
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the rating assigned to a thing based on a grade or score according to a particular rating scale
  inverse_of:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/rates.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/rates
  range:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/Rating.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/Rating
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasRating
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: has rating
type: Ontology Property
---

# has rating

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasRating>

## Definition

indicates the rating assigned to a thing based on a grade or score according to a particular rating scale

## Relationships

- **Inverse of**: [rates](/concepts/fibo/FND/Arrangements/Ratings/rates.md)
- **Range**: [Rating](/concepts/fibo/FND/Arrangements/Ratings/Rating.md)
- **Subproperty of**: [isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)

## Annotations

- **label**: has rating
- **definition**: indicates the rating assigned to a thing based on a grade or score according to a particular rating scale

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
