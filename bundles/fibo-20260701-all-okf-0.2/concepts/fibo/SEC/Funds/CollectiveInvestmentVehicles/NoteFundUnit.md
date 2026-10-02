---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: note fund unit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment interest in a fund that issues notes rather than traditional equity, in cases where the fund is structured
      as a trust, partnership, or unitized fund
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A note fund unit refers to a non-equity interest in a fund that issues rated notes and is organized as a unit trust
      or limited partnership.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/NoteFund
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isPartOf
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/Funds/FundUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/NoteFundUnit
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: note fund unit
type: Ontology Class
---

# note fund unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/NoteFundUnit>

## Definition

investment interest in a fund that issues notes rather than traditional equity, in cases where the fund is structured as a trust, partnership, or unitized fund

## Relationships

- **Subclass of**: [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)

## Constraints

- **[isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)**: some values from of type [NoteFund](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/NoteFund.md)

## Annotations

- **label**: note fund unit
- **definition**: investment interest in a fund that issues notes rather than traditional equity, in cases where the fund is structured as a trust, partnership, or unitized fund
- **explanatoryNote**: A note fund unit refers to a non-equity interest in a fund that issues rated notes and is organized as a unit trust or limited partnership.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
