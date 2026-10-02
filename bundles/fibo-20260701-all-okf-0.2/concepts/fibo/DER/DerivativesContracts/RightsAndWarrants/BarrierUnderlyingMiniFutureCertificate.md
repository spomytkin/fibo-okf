---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: barrier underlying mini-future certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: mini-future certificate that immediately expires if the barrier underlying level is breached during product lifetime
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/MiniFutureCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/MiniFutureCertificate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/BarrierUnderlyingMiniFutureCertificate
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: barrier underlying mini-future certificate
type: Ontology Class
---

# barrier underlying mini-future certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/BarrierUnderlyingMiniFutureCertificate>

## Definition

mini-future certificate that immediately expires if the barrier underlying level is breached during product lifetime

## Relationships

- **Subclass of**: [MiniFutureCertificate](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/MiniFutureCertificate.md)

## Annotations

- **label** (en): barrier underlying mini-future certificate
- **definition** (en): mini-future certificate that immediately expires if the barrier underlying level is breached during product lifetime
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
