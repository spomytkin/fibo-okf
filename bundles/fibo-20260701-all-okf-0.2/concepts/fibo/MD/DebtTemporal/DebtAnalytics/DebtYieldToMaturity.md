---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt yield to maturity
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The internal rate of return an investor would achieve if he or she purchased that bond at its current dirty price,
      and held it to maturity, assuming all coupon and principal payments are received as scheduled.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasOutlookPeriod
    value: N1f46f87feb8d4a25b6c5a0496c655782
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtYieldToMaturity
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: debt yield to maturity
type: Ontology Class
---

# debt yield to maturity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtYieldToMaturity>

## Definition

The internal rate of return an investor would achieve if he or she purchased that bond at its current dirty price, and held it to maturity, assuming all coupon and principal payments are received as scheduled.

## Relationships

- **Subclass of**: [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)

## Constraints

- **[hasOutlookPeriod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/hasOutlookPeriod.md)**: some values from value `N1f46f87feb8d4a25b6c5a0496c655782`

## Annotations

- **label** (en): debt yield to maturity
- **definition** (en): The internal rate of return an investor would achieve if he or she purchased that bond at its current dirty price, and held it to maturity, assuming all coupon and principal payments are received as scheduled.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
