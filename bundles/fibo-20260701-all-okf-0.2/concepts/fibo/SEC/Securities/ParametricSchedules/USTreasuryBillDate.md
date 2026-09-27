---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: US Treasury bill date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: auction date for US 13 week and 26 week Treasury bills
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Per FpML notes/definition, this is every Monday except on New York holidays when it will be on a Tuesday.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/USTreasuryBillAuctionDateRule
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculatedDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/USTreasuryBillDate
sources:
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: US Treasury bill date
type: Ontology Class
---

# US Treasury bill date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/USTreasuryBillDate>

## Definition

auction date for US 13 week and 26 week Treasury bills

## Relationships

- **Subclass of**: [CalculatedDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md)

## Constraints

- **[hasBusinessDayConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention.md)**: exact qualified cardinality 1 of type [USTreasuryBillAuctionDateRule](/concepts/fibo/SEC/Securities/ParametricSchedules/USTreasuryBillAuctionDateRule.md)

## Annotations

- **label**: US Treasury bill date
- **definition**: auction date for US 13 week and 26 week Treasury bills
- **explanatoryNote**: Per FpML notes/definition, this is every Monday except on New York holidays when it will be on a Tuesday.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
