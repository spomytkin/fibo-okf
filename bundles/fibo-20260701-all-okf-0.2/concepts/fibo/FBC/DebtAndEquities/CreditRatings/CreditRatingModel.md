---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit rating model
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: algorithm for computing a credit rating
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Use dct:hasVersion to specify a version for the credit score model.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScore
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/produces
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingModelType
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasTextualName
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingModel
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: credit rating model
type: Ontology Class
---

# credit rating model

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingModel>

## Definition

algorithm for computing a credit rating

## Relationships

- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[produces](/concepts/fibo/FND/Relations/Relations/produces.md)**: some values from of type [RatingScore](/concepts/fibo/FND/Arrangements/Ratings/RatingScore.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [CreditRatingModelType](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRatingModelType.md)
- **[hasTextualName](<https://www.omg.org/spec/Commons/Designators/hasTextualName>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: credit rating model
- **definition**: algorithm for computing a credit rating
- **usageNote**: Use dct:hasVersion to specify a version for the credit score model.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
