---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: price value of basis point
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Sensitivity of the price for one basis point change in yield, defined as the difference in price given 1 bp change
      in yield.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: PVBP
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Price value of Basis Point Definition: The difference in price given 1 bp change in yield. This is like Duration
      but normalized to 1 basis point. Synonym DV01'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PriceValueOfBasisPoint
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: price value of basis point
type: Ontology Class
---

# price value of basis point

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PriceValueOfBasisPoint>

## Definition

Sensitivity of the price for one basis point change in yield, defined as the difference in price given 1 bp change in yield.

## Relationships

- **Subclass of**: [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)

## Constraints

- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)

## Annotations

- **label** (en): price value of basis point
- **definition** (en): Sensitivity of the price for one basis point change in yield, defined as the difference in price given 1 bp change in yield.
- **abbreviation** (en): PVBP
- **explanatoryNote** (en): Price value of Basis Point Definition: The difference in price given 1 bp change in yield. This is like Duration but normalized to 1 basis point. Synonym DV01

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
