---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: minimum rating restriction
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The minimum rating of securities to be invested in.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction
  range:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingScore.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingScore
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/minimumRatingRestriction
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: minimum rating restriction
type: Ontology Property
---

# minimum rating restriction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/minimumRatingRestriction>

## Definition

The minimum rating of securities to be invested in.

## Relationships

- **Domain**: [InvestmentRestriction](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction.md)
- **Range**: [RatingScore](/concepts/fibo/FND/Arrangements/Ratings/RatingScore.md)

## Annotations

- **label** (en): minimum rating restriction
- **definition** (en): The minimum rating of securities to be invested in.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
