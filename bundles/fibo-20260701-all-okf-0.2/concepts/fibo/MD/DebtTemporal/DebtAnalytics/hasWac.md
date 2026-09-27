---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has wac
  domain:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity
  range:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/WeightedAverageCoupon.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageCoupon
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasWac
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: has wac
type: Ontology Property
---

# has wac

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasWac>

## Relationships

- **Domain**: [MortgageBackedSecurity](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md)
- **Range**: [WeightedAverageCoupon](/concepts/fibo/SEC/Debt/PoolBackedSecurities/WeightedAverageCoupon.md)

## Annotations

- **label** (en): has wac

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
