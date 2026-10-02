---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund share class unit
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The legal structure in which you can purchase part of an investment pool, defined by a variety of characteristics
      like investor type, minimum size of investment, distribution type, fee and currency. A fund unit which gives the holder
      an equity stake in the fund.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'From review sessions: Theoretically you can buy a fraction of a share in a fund. This would depend on the legal
      structure of the fund, e.g. a minimum investment. There is always a distribution plan.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionPolicy
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/Funds/FundUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund share class unit
type: Ontology Class
---

# fund share class unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit>

## Definition

The legal structure in which you can purchase part of an investment pool, defined by a variety of characteristics like investor type, minimum size of investment, distribution type, fee and currency. A fund unit which gives the holder an equity stake in the fund.

## Relationships

- **Subclass of**: [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)

## Constraints

- **[hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)**: some values from of type [FundUnitDistributionPolicy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionPolicy.md)

## Annotations

- **label** (en): fund share class unit
- **definition** (en): The legal structure in which you can purchase part of an investment pool, defined by a variety of characteristics like investor type, minimum size of investment, distribution type, fee and currency. A fund unit which gives the holder an equity stake in the fund.
- **explanatoryNote** (en): From review sessions: Theoretically you can buy a fraction of a share in a fund. This would depend on the legal structure of the fund, e.g. a minimum investment. There is always a distribution plan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
