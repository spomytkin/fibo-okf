---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has funding leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the leg of a return swap that specifies a set payment rate, typically benchmark based but possibly a
      fixed rate
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/ReturnSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnSwap
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasFundingLeg
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: has funding leg
type: Ontology Property
---

# has funding leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasFundingLeg>

## Definition

indicates the leg of a return swap that specifies a set payment rate, typically benchmark based but possibly a fixed rate

## Relationships

- **Domain**: [ReturnSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/ReturnSwap.md)
- **Subproperty of**: [hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)

## Annotations

- **label** (en): has funding leg
- **definition**: indicates the leg of a return swap that specifies a set payment rate, typically benchmark based but possibly a fixed rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
