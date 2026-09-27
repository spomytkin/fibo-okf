---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: net asset value calculation method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Parameters for the calculation of the net asset value for an investment fund/fund class.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: These terms were in the ISO FIBIM model but correspond to some details in the EFAMA DD.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/isCalculatedIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/NetAssetValueCalculationMethod
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: net asset value calculation method
type: Ontology Class
---

# net asset value calculation method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/NetAssetValueCalculationMethod>

## Definition

Parameters for the calculation of the net asset value for an investment fund/fund class.

## Relationships

- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[isCalculatedIn](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/isCalculatedIn.md)**: some values from of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label** (en): net asset value calculation method
- **definition** (en): Parameters for the calculation of the net asset value for an investment fund/fund class.
- **editorialNote** (en): These terms were in the ISO FIBIM model but correspond to some details in the EFAMA DD.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
