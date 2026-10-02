---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: organization credit rating
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit rating that provides an opinion of creditworthiness of an organization
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/FormalOrganization
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/rates
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRating.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRating
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/OrganizationCreditRating
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: organization credit rating
type: Ontology Class
---

# organization credit rating

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/OrganizationCreditRating>

## Definition

credit rating that provides an opinion of creditworthiness of an organization

## Relationships

- **Subclass of**: [CreditRating](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRating.md)

## Constraints

- **[rates](/concepts/fibo/FND/Arrangements/Ratings/rates.md)**: some values from of type [FormalOrganization](<https://www.omg.org/spec/Commons/Organizations/FormalOrganization>)

## Annotations

- **label** (en): organization credit rating
- **definition** (en): credit rating that provides an opinion of creditworthiness of an organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
