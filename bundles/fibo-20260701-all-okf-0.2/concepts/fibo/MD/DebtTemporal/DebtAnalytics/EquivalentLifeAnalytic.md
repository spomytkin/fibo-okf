---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equivalent life analytic
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/WeightedAverageLife.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageLife
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PartialCallsEstimationModel
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondWithPartialCall
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/LifeAnalytic.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/LifeAnalytic
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/EquivalentLifeAnalytic
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: equivalent life analytic
type: Ontology Class
---

# equivalent life analytic

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/EquivalentLifeAnalytic>

## Relationships

- **Subclass of**: [LifeAnalytic](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/LifeAnalytic.md)

## Constraints

- **Disjoint with**: [WeightedAverageLife](/concepts/fibo/SEC/Debt/PoolBackedSecurities/WeightedAverageLife.md)
- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [PartialCallsEstimationModel](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/PartialCallsEstimationModel.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [BondWithPartialCall](/concepts/fibo/SEC/Debt/Bonds/BondWithPartialCall.md)

## Annotations

- **label** (en): equivalent life analytic

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
