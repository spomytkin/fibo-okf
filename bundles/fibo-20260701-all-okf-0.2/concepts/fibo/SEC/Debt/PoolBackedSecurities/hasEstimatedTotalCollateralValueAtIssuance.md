---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is estimated value of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the estimated value of the combined underlying collateral for a given tranche at the time the instrument
      was issued
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/isEstimatedValueOf.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/isEstimatedValueOf
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/hasEstimatedTotalCollateralValueAtIssuance
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: is estimated value of
type: Ontology Property
---

# is estimated value of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/hasEstimatedTotalCollateralValueAtIssuance>

## Definition

indicates the estimated value of the combined underlying collateral for a given tranche at the time the instrument was issued

## Relationships

- **Range**: [CollateralValueAsOfDate](/concepts/fibo/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md)
- **Subproperty of**: [isEstimatedValueOf](/concepts/fibo/FND/Arrangements/Assessments/isEstimatedValueOf.md)

## Annotations

- **label**: is estimated value of
- **definition**: indicates the estimated value of the combined underlying collateral for a given tranche at the time the instrument was issued

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
