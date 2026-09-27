---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pool factor
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: How much of the original pool is still outstanding. This is a number below one. Expressed as percentage.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Would multiply the factor by the starting value of the pool. This determines how much it is paying down. Would
      take the form of a 10 digit decimal factor showing how much of the pool is outstanding. You get Factor information every
      month or so which includes the WAM figure (and the WALA and WAC). The rate can be derived from this. that would be the
      rate at which the pool is paying down. These all come from the issuer.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PoolFactor
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: pool factor
type: Ontology Class
---

# pool factor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PoolFactor>

## Definition

How much of the original pool is still outstanding. This is a number below one. Expressed as percentage.

## Relationships

- **Subclass of**: [Percentage](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage>)

## Annotations

- **label** (en): pool factor
- **definition** (en): How much of the original pool is still outstanding. This is a number below one. Expressed as percentage.
- **explanatoryNote** (en): Would multiply the factor by the starting value of the pool. This determines how much it is paying down. Would take the form of a 10 digit decimal factor showing how much of the pool is outstanding. You get Factor information every month or so which includes the WAM figure (and the WALA and WAC). The rate can be derived from this. that would be the rate at which the pool is paying down. These all come from the issuer.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
