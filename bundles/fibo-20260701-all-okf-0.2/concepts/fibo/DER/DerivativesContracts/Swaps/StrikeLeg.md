---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: strike leg
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap leg that specifies a fixed amount, 'the strike', quoted at the time of execution
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The fixed amount may be with respect to some variable or a monetary amount. The realization of a strike leg is
      not a cashflow per se, but a netting out against the terms defined in the other leg of a statistical swap.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/FixedLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/StrikeLeg
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: strike leg
type: Ontology Class
---

# strike leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/StrikeLeg>

## Definition

swap leg that specifies a fixed amount, 'the strike', quoted at the time of execution

## Relationships

- **Subclass of**: [FixedLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/FixedLeg.md)

## Annotations

- **label** (en): strike leg
- **definition** (en): swap leg that specifies a fixed amount, 'the strike', quoted at the time of execution
- **explanatoryNote** (en): The fixed amount may be with respect to some variable or a monetary amount. The realization of a strike leg is not a cashflow per se, but a netting out against the terms defined in the other leg of a statistical swap.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
