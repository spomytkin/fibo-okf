---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit rating
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: assessment of creditworthiness of a borrower generally or with respect to a particular debt or financial obligation
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Typically, a credit rating is provided as a detailed report based on the financial history of borrowing or lending
      and creditworthiness of the entity or person derived from income statements, historical records related to borrowing,
      etc. with an aim to determine their ability to meet debt obligations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingModel
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/isDerivedFrom
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/Rating.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/Rating
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRating
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: credit rating
type: Ontology Class
---

# credit rating

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRating>

## Definition

assessment of creditworthiness of a borrower generally or with respect to a particular debt or financial obligation

## Relationships

- **Subclass of**: [Rating](/concepts/fibo/FND/Arrangements/Ratings/Rating.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from of type [CreditRatingAgency](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md)
- **[isDerivedFrom](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/isDerivedFrom>)**: min qualified cardinality 0 of type [CreditRatingModel](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRatingModel.md)

## Annotations

- **label** (en): credit rating
- **definition** (en): assessment of creditworthiness of a borrower generally or with respect to a particular debt or financial obligation
- **explanatoryNote** (en): Typically, a credit rating is provided as a detailed report based on the financial history of borrowing or lending and creditworthiness of the entity or person derived from income statements, historical records related to borrowing, etc. with an aim to determine their ability to meet debt obligations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
