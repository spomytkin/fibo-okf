---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: option adjusted yield
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'NB specified as a spread. synonym: OAS Based on different Int Rate paths. There are different OAS models just
      like there are different Yield methods. Also would make reference to the Yield Curve - but these are parameters that
      go into that model. Limit this model at the point where it distinguishes the difference between things - we are not
      in a position to mathematically model the things themselves, just capture the basic facts.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/OptionAdjustedYield
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: option adjusted yield
type: Ontology Class
---

# option adjusted yield

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/OptionAdjustedYield>

## Definition

NB specified as a spread. synonym: OAS Based on different Int Rate paths. There are different OAS models just like there are different Yield methods. Also would make reference to the Yield Curve - but these are parameters that go into that model. Limit this model at the point where it distinguishes the difference between things - we are not in a position to mathematically model the things themselves, just capture the basic facts.

## Relationships

- **Subclass of**: [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)

## Annotations

- **label** (en): option adjusted yield
- **definition** (en): NB specified as a spread. synonym: OAS Based on different Int Rate paths. There are different OAS models just like there are different Yield methods. Also would make reference to the Yield Curve - but these are parameters that go into that model. Limit this model at the point where it distinguishes the difference between things - we are not in a position to mathematically model the things themselves, just capture the basic facts.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
