---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: realized variable leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: performance-based leg wherein the payment is netted at maturity rather than periodically
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In this case there is a single payment at maturity/settlement and so there is no stream of cashflows either way.
      The other leg of these swaps is implied, and is simply the strike price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RealizedVariableLeg
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: realized variable leg
type: Ontology Class
---

# realized variable leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RealizedVariableLeg>

## Definition

performance-based leg wherein the payment is netted at maturity rather than periodically

## Relationships

- **Subclass of**: [PerformanceBasedVariableLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md)

## Annotations

- **label**: realized variable leg
- **definition**: performance-based leg wherein the payment is netted at maturity rather than periodically
- **explanatoryNote**: In this case there is a single payment at maturity/settlement and so there is no stream of cashflows either way. The other leg of these swaps is implied, and is simply the strike price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
