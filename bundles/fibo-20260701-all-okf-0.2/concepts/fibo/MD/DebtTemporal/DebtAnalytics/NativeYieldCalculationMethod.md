---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: native yield calculation method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The convention used in the marketplace for that security.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/isDefaultMethodFor
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/RelativeYieldCalculationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/RelativeYieldCalculationMethod
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NativeYieldCalculationMethod
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: native yield calculation method
type: Ontology Class
---

# native yield calculation method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NativeYieldCalculationMethod>

## Definition

The convention used in the marketplace for that security.

## Relationships

- **Subclass of**: [RelativeYieldCalculationMethod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/RelativeYieldCalculationMethod.md)

## Constraints

- **[isDefaultMethodFor](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/isDefaultMethodFor.md)**: some values from of type [TradableDebtInstrument](/concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)

## Annotations

- **label** (en): native yield calculation method
- **definition** (en): The convention used in the marketplace for that security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
