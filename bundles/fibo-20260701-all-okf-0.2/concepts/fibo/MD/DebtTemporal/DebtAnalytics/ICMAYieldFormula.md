---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: i c m a yield formula
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The calculation method specified by ICMA (formerly ISMA) for determination of yield for fixed-rate bonds.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This basic formula is used across many markets, including the US and most of Europe. While individual markets may
      have different flavors (French round their bonds to 5 decimals, UK Gilts have ex-div), the formula is still the same.
      This would be the formula used by "Wall Street Yield", "US Treasury Yield", "Corporate Bond Yield" etc. Notes Origin:Fidessa
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationFormula.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationFormula
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/ICMAYieldFormula
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: i c m a yield formula
type: Ontology Class
---

# i c m a yield formula

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/ICMAYieldFormula>

## Definition

The calculation method specified by ICMA (formerly ISMA) for determination of yield for fixed-rate bonds.

## Relationships

- **Subclass of**: [YieldCalculationFormula](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationFormula.md)

## Annotations

- **label** (en): i c m a yield formula
- **definition** (en): The calculation method specified by ICMA (formerly ISMA) for determination of yield for fixed-rate bonds.
- **explanatoryNote** (en): This basic formula is used across many markets, including the US and most of Europe. While individual markets may have different flavors (French round their bonds to 5 decimals, UK Gilts have ex-div), the formula is still the same. This would be the formula used by "Wall Street Yield", "US Treasury Yield", "Corporate Bond Yield" etc. Notes Origin:Fidessa

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
