---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: weighted average time to receipt of cashflows
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The weighted average time to the receipt of cashflows for an instrument.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: A formal definition is needed for this. The name is almost self defining, but only to those who already know what
      this means. In particular we should define how the weighted average is weighted, and what this means, along with a formula
      for calculating this at the most generic level (cashflow, time, without assumptions about particular types of instrument).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Formula.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Formula
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/WeightedAverageTimeToReceiptOfCashflows
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: weighted average time to receipt of cashflows
type: Ontology Class
---

# weighted average time to receipt of cashflows

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/WeightedAverageTimeToReceiptOfCashflows>

## Definition

The weighted average time to the receipt of cashflows for an instrument.

## Relationships

- **Subclass of**: [Formula](/concepts/fibo/FND/Utilities/Analytics/Formula.md)

## Annotations

- **label** (en): weighted average time to receipt of cashflows
- **definition** (en): The weighted average time to the receipt of cashflows for an instrument.
- **editorialNote** (en): A formal definition is needed for this. The name is almost self defining, but only to those who already know what this means. In particular we should define how the weighted average is weighted, and what this means, along with a formula for calculating this at the most generic level (cashflow, time, without assumptions about particular types of instrument).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
