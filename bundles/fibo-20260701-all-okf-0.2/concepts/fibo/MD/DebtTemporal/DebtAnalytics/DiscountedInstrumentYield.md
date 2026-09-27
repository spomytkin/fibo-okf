---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: discounted instrument yield
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Yield quoted for a discount instrument. This is the ratio of the discount to the face value, divided by the period
      to maturity as a fraction of a year.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Applies to Debt only.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DiscountedInstrumentYield
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: discounted instrument yield
type: Ontology Class
---

# discounted instrument yield

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DiscountedInstrumentYield>

## Definition

Yield quoted for a discount instrument. This is the ratio of the discount to the face value, divided by the period to maturity as a fraction of a year.

## Relationships

- **Subclass of**: [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)

## Annotations

- **label** (en): discounted instrument yield
- **definition** (en): Yield quoted for a discount instrument. This is the ratio of the discount to the face value, divided by the period to maturity as a fraction of a year.
- **usageNote** (en): Applies to Debt only.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
