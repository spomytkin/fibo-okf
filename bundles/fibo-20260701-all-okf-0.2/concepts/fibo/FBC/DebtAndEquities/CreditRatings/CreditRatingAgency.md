---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit rating agency
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rating agency that publishes reports assessing the creditworthiness of a borrower or legal entity, either generally
      or with respect to a specific obligation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRating
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/issues
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingScale
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/manages
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingAgency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingAgency
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: credit rating agency
type: Ontology Class
---

# credit rating agency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency>

## Definition

rating agency that publishes reports assessing the creditworthiness of a borrower or legal entity, either generally or with respect to a specific obligation

## Relationships

- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- **Subclass of**: [RatingAgency](/concepts/fibo/FND/Arrangements/Ratings/RatingAgency.md)

## Constraints

- **[issues](/concepts/fibo/FND/Relations/Relations/issues.md)**: some values from of type [CreditRating](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRating.md)
- **[manages](<https://www.omg.org/spec/Commons/Organizations/manages>)**: some values from of type [CreditRatingScale](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRatingScale.md)

## Annotations

- **label** (en): credit rating agency
- **definition** (en): rating agency that publishes reports assessing the creditworthiness of a borrower or legal entity, either generally or with respect to a specific obligation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
