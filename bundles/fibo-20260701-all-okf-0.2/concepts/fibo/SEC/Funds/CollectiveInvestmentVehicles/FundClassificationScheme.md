---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund classification scheme
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A published scheme for the category of a fund according to the asset class.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundClassification
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundClassificationScheme
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund classification scheme
type: Ontology Class
---

# fund classification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundClassificationScheme>

## Definition

A published scheme for the category of a fund according to the asset class.

## Relationships

- **Subclass of**: [ClassificationScheme](<https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [FundClassification](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundClassification.md)

## Annotations

- **label** (en): fund classification scheme
- **definition** (en): A published scheme for the category of a fund according to the asset class.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
