---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basis swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap in which payment streams are referenced to different bases
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A basis swap can have two legs of the same tenor but different indices, e.g., 3 month LIBOR vs. 3 month TIBOR.
      The difference in this case is not driven by different interest rate periods but from different markets, i.e., the difference
      in efficiency between the two markets. The objective is to hedge against basis risk which is the difference in price
      between two markets. See also forward swap, as a means for controlling interest rate.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/RatesSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RatesSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/BasisSwap
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: basis swap
type: Ontology Class
---

# basis swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/BasisSwap>

## Definition

swap in which payment streams are referenced to different bases

## Relationships

- **Subclass of**: [RatesSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/RatesSwap.md)

## Annotations

- **label**: basis swap
- **definition**: swap in which payment streams are referenced to different bases
- **explanatoryNote**: A basis swap can have two legs of the same tenor but different indices, e.g., 3 month LIBOR vs. 3 month TIBOR. The difference in this case is not driven by different interest rate periods but from different markets, i.e., the difference in efficiency between the two markets. The objective is to hedge against basis risk which is the difference in price between two markets. See also forward swap, as a means for controlling interest rate.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
