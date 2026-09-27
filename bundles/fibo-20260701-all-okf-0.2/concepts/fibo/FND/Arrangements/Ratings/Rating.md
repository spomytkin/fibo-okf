---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rating
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: standing of something at a particular time, indicated by at least one scores with respect to some scale, based
      on an assessment by some party
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasEffectiveDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScore
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/hasRatingScore
  - cardinality: 1
    kind: exact_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/rates
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingParty
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isGeneratedBy
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingIssuer
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDateOfIssuance
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/Opinion.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Opinion
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/Rating
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: rating
type: Ontology Class
---

# rating

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/Rating>

## Definition

standing of something at a particular time, indicated by at least one scores with respect to some scale, based on an assessment by some party

## Relationships

- **Subclass of**: [Opinion](/concepts/fibo/FND/Arrangements/Assessments/Opinion.md)

## Constraints

- **[hasEffectiveDate](/concepts/fibo/FND/Agreements/Contracts/hasEffectiveDate.md)**: max qualified cardinality 1 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasRatingScore](/concepts/fibo/FND/Arrangements/Ratings/hasRatingScore.md)**: some values from of type [RatingScore](/concepts/fibo/FND/Arrangements/Ratings/RatingScore.md)
- **[rates](/concepts/fibo/FND/Arrangements/Ratings/rates.md)**: exact cardinality 1
- **[isGeneratedBy](/concepts/fibo/FND/Relations/Relations/isGeneratedBy.md)**: exact qualified cardinality 1 of type [RatingParty](/concepts/fibo/FND/Arrangements/Ratings/RatingParty.md)
- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: exact qualified cardinality 1 of type [RatingIssuer](/concepts/fibo/FND/Arrangements/Ratings/RatingIssuer.md)
- **[hasDateOfIssuance](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDateOfIssuance>)**: exact qualified cardinality 1 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label**: rating
- **definition**: standing of something at a particular time, indicated by at least one scores with respect to some scale, based on an assessment by some party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
