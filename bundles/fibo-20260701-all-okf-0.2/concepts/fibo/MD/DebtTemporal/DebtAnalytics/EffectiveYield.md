---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: effective yield
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'The difference between this and Native yield is as per note: Native yield relates to price quotation context;
      Effective Yild is in relation to portfolio analytics. Recall: every analytic formula relates to the set of cash flows,
      so there are assumptions underlying each of these, For example the assumption that Y is constant, which it isn''t (because
      there is a curve, which may be convex not linear (is that right?). So you can compare rate or return between what I
      see and what the market has out there. In the US market: a Y which is calculated using Monto Carlo method simulation.
      relationship facts to add: Relation to method / formula (e.g. Monte Carlo), and the method used to determine the actual
      figure for the MC method. eff Y for single instrument: E Y for bonds without calls and stuff. Variation in this: whether
      we look at a whole set of bonds YTM quoted by Bmb would be the YTM quoted according to whatever the market is - = the
      NAtive Yield. SO: Publicly quoted more: choose another adjective.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/EffectiveYield
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: effective yield
type: Ontology Class
---

# effective yield

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/EffectiveYield>

## Relationships

- **Subclass of**: [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)

## Annotations

- **label** (en): effective yield
- **editorialNote** (en): The difference between this and Native yield is as per note: Native yield relates to price quotation context; Effective Yild is in relation to portfolio analytics. Recall: every analytic formula relates to the set of cash flows, so there are assumptions underlying each of these, For example the assumption that Y is constant, which it isn't (because there is a curve, which may be convex not linear (is that right?). So you can compare rate or return between what I see and what the market has out there. In the US market: a Y which is calculated using Monto Carlo method simulation. relationship facts to add: Relation to method / formula (e.g. Monte Carlo), and the method used to determine the actual figure for the MC method. eff Y for single instrument: E Y for bonds without calls and stuff. Variation in this: whether we look at a whole set of bonds YTM quoted by Bmb would be the YTM quoted according to whatever the market is - = the NAtive Yield. SO: Publicly quoted more: choose another adjective.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
