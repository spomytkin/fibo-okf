---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt yield to equivalent life
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The yield achieved by substituting a bond's equivalent life for the issue's final maturity date.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Some sources have Average Life and Equivalent Life as the same term, whereas we have separated them.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/EquivalentLifeAnalytic
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasOutlookPeriod
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtYieldToEquivalentLife
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: debt yield to equivalent life
type: Ontology Class
---

# debt yield to equivalent life

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtYieldToEquivalentLife>

## Definition

The yield achieved by substituting a bond's equivalent life for the issue's final maturity date.

## Relationships

- **Subclass of**: [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)

## Constraints

- **[hasOutlookPeriod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/hasOutlookPeriod.md)**: some values from of type [EquivalentLifeAnalytic](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/EquivalentLifeAnalytic.md)

## Annotations

- **label** (en): debt yield to equivalent life
- **definition** (en): The yield achieved by substituting a bond's equivalent life for the issue's final maturity date.
- **editorialNote** (en): Some sources have Average Life and Equivalent Life as the same term, whereas we have separated them.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
