---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: excess return swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: return swap in which the change in the level of the index will be equal to the returns generated primarily by the
      changes in price of each of the contracts that comprise the index
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISDA Disclosure Annex for Commodity Derivative Transactions. See https://globalmarkets.bnpparibas.com/gm/features/docs/dfdisclosures/ISDA_Commodity_Derivatives_Disclosure_Annex_04_2013.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/IndexReturnSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/IndexReturnSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ExcessReturnSwap
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: excess return swap
type: Ontology Class
---

# excess return swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ExcessReturnSwap>

## Definition

return swap in which the change in the level of the index will be equal to the returns generated primarily by the changes in price of each of the contracts that comprise the index

## Relationships

- **Subclass of**: [IndexReturnSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/IndexReturnSwap.md)

## Annotations

- **label** (en): excess return swap
- **definition** (en): return swap in which the change in the level of the index will be equal to the returns generated primarily by the changes in price of each of the contracts that comprise the index
- **adaptedFrom** (en): ISDA Disclosure Annex for Commodity Derivative Transactions. See https://globalmarkets.bnpparibas.com/gm/features/docs/dfdisclosures/ISDA_Commodity_Derivatives_Disclosure_Annex_04_2013.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
