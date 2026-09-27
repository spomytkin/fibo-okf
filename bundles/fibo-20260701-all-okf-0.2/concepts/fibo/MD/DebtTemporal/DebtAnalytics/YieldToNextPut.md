---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: yield to next put
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NextPut
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasOutlookPeriod
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldToNextPut
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: yield to next put
type: Ontology Class
---

# yield to next put

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldToNextPut>

## Relationships

- **Subclass of**: [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)

## Constraints

- **[hasOutlookPeriod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/hasOutlookPeriod.md)**: some values from of type [NextPut](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/NextPut.md)

## Annotations

- **label** (en): yield to next put

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
