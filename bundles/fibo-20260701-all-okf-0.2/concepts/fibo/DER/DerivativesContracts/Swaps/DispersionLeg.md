---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dispersion leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: floating leg of a dispersion swap that pays an amount based on the realized dispersion of the price changes of
      the underlying product
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Underlying assets may include, for example, exchange rates, interest rates, or the price of an index.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: variance leg
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionSwap
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/isLegOf
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionLeg
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: dispersion leg
type: Ontology Class
---

# dispersion leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionLeg>

## Definition

floating leg of a dispersion swap that pays an amount based on the realized dispersion of the price changes of the underlying product

## Relationships

- **Subclass of**: [PerformanceBasedVariableLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md)

## Constraints

- **[isLegOf](/concepts/fibo/DER/DerivativesContracts/Swaps/isLegOf.md)**: some values from of type [DispersionSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/DispersionSwap.md)

## Annotations

- **label** (en): dispersion leg
- **definition**: floating leg of a dispersion swap that pays an amount based on the realized dispersion of the price changes of the underlying product
- **explanatoryNote** (en): Underlying assets may include, for example, exchange rates, interest rates, or the price of an index.
- **synonym** (en): variance leg

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
