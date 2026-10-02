---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: traditional warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that gives the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant)
      an underlying asset at a specified price (the strike or exercise price) by a predetermined date, issued by the issuer
      of the underlying instrument
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: vanilla warrant
  disjoint_with:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/CoveredWarrant.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CoveredWarrant
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/NakedWarrant.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/NakedWarrant
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/TraditionalWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: traditional warrant
type: Ontology Class
---

# traditional warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/TraditionalWarrant>

## Definition

warrant that gives the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant) an underlying asset at a specified price (the strike or exercise price) by a predetermined date, issued by the issuer of the underlying instrument

## Relationships

- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)

## Constraints

- **Disjoint with**: [CoveredWarrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/CoveredWarrant.md)
- **Disjoint with**: [NakedWarrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/NakedWarrant.md)

## Annotations

- **label** (en): traditional warrant
- **definition** (en): warrant that gives the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant) an underlying asset at a specified price (the strike or exercise price) by a predetermined date, issued by the issuer of the underlying instrument
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **synonym** (en): vanilla warrant

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
