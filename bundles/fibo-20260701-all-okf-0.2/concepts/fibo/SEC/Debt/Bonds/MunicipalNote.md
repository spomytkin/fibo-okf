---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: municipal note
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: short-term obligation to repay a specified principal amount on a certain date, together with interest at a stated
      rate, usually payable from a defined source of anticipated revenues
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Notes usually mature in one year or less, although notes of longer maturities are also issued.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalNote
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: municipal note
type: Ontology Class
---

# municipal note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalNote>

## Definition

short-term obligation to repay a specified principal amount on a certain date, together with interest at a stated rate, usually payable from a defined source of anticipated revenues

## Relationships

- **Subclass of**: [MunicipalSecurity](/concepts/fibo/SEC/Debt/Bonds/MunicipalSecurity.md)

## Annotations

- **label**: municipal note
- **definition**: short-term obligation to repay a specified principal amount on a certain date, together with interest at a stated rate, usually payable from a defined source of anticipated revenues
- **explanatoryNote**: Notes usually mature in one year or less, although notes of longer maturities are also issued.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
