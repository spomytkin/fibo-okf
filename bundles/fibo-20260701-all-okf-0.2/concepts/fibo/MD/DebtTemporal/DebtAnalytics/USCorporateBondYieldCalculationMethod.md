---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: u s corporate bond yield calculation method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: This has 30/360 and semi-annual compounding.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/ICMAYieldFormula
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasFormula
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/USCorporateBondYieldCalculationMethod
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: u s corporate bond yield calculation method
type: Ontology Class
---

# u s corporate bond yield calculation method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/USCorporateBondYieldCalculationMethod>

## Definition

This has 30/360 and semi-annual compounding.

## Relationships

- **Subclass of**: [YieldCalculationMethod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md)

## Constraints

- **[hasFormula](/concepts/fibo/FND/Utilities/Analytics/hasFormula.md)**: some values from of type [ICMAYieldFormula](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/ICMAYieldFormula.md)

## Annotations

- **label** (en): u s corporate bond yield calculation method
- **definition** (en): This has 30/360 and semi-annual compounding.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
