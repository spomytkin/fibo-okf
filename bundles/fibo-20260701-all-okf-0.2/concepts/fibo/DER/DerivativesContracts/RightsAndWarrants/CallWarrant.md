---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: call warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant giving the buyer (holder) the right, but not the obligation, to acquire specific underlying assets during
      a specified period at a specified price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Exercising a call warrant whose underlying instrument is an equity involves buying new shares directly from the
      company, causing dilution.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CallWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: call warrant
type: Ontology Class
---

# call warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CallWarrant>

## Definition

warrant giving the buyer (holder) the right, but not the obligation, to acquire specific underlying assets during a specified period at a specified price

## Relationships

- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)

## Annotations

- **label** (en): call warrant
- **definition** (en): warrant giving the buyer (holder) the right, but not the obligation, to acquire specific underlying assets during a specified period at a specified price
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.
- **explanatoryNote** (en): Exercising a call warrant whose underlying instrument is an equity involves buying new shares directly from the company, causing dilution.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
