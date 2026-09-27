---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit rating scale
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rating scale for assigning a credit rating to individual, entity, or instrument, including defining a set of codes
      or numeric scores and indicating how an assessment that is assigned a score based on that scale means
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingScale.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScale
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingScale
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: credit rating scale
type: Ontology Class
---

# credit rating scale

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingScale>

## Definition

rating scale for assigning a credit rating to individual, entity, or instrument, including defining a set of codes or numeric scores and indicating how an assessment that is assigned a score based on that scale means

## Relationships

- **Subclass of**: [RatingScale](/concepts/fibo/FND/Arrangements/Ratings/RatingScale.md)

## Constraints

- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: some values from of type [CreditRatingAgency](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md)

## Annotations

- **label** (en): credit rating scale
- **definition** (en): rating scale for assigning a credit rating to individual, entity, or instrument, including defining a set of codes or numeric scores and indicating how an assessment that is assigned a score based on that scale means

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
