---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: index return swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: return swap in which payments are based on a fee paid to the seller of the swap and on a floating reference price
      based on changes in the level of an index from an initial level to a level observed on some valuation date(s)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISDA Disclosure Annex for Commodity Derivative Transactions. See https://globalmarkets.bnpparibas.com/gm/features/docs/dfdisclosures/ISDA_Commodity_Derivatives_Disclosure_Annex_04_2013.pdf
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Payments to the parties may be made either on a periodic basis or on termination of the transaction. One party
      will receive a payment based upon the change in the level of the index between two valuation dates (multiplied by the
      notional amount of the swap), as modified by the fee paid to the seller of the swap. If the level of the index increases,
      the buyer of the swap will be entitled to a payment based on this performance, as such payment may be reduced (or negated)
      by the fee paid to the seller of the swap. If the level of the index decreases, the seller of the swap will be entitled
      to a payment based on this performance, as such payment may be increased by the fee paid to the seller of the swap.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/ReturnSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/IndexReturnSwap
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: index return swap
type: Ontology Class
---

# index return swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/IndexReturnSwap>

## Definition

return swap in which payments are based on a fee paid to the seller of the swap and on a floating reference price based on changes in the level of an index from an initial level to a level observed on some valuation date(s)

## Relationships

- **Subclass of**: [ReturnSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/ReturnSwap.md)

## Annotations

- **label** (en): index return swap
- **definition** (en): return swap in which payments are based on a fee paid to the seller of the swap and on a floating reference price based on changes in the level of an index from an initial level to a level observed on some valuation date(s)
- **adaptedFrom** (en): ISDA Disclosure Annex for Commodity Derivative Transactions. See https://globalmarkets.bnpparibas.com/gm/features/docs/dfdisclosures/ISDA_Commodity_Derivatives_Disclosure_Annex_04_2013.pdf
- **explanatoryNote** (en): Payments to the parties may be made either on a periodic basis or on termination of the transaction. One party will receive a payment based upon the change in the level of the index between two valuation dates (multiplied by the notional amount of the swap), as modified by the fee paid to the seller of the swap. If the level of the index increases, the buyer of the swap will be entitled to a payment based on this performance, as such payment may be reduced (or negated) by the fee paid to the seller of the swap. If the level of the index decreases, the seller of the swap will be entitled to a payment based on this performance, as such payment may be increased by the fee paid to the seller of the swap.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
