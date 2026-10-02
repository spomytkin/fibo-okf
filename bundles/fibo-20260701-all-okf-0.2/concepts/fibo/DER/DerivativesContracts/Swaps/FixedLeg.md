---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fixed leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap leg whose paying party is obligated to make payments from time to time over the term of a swap calculated
      by reference to a fixed annual rate or consisting of at least one payment of a fixed amount
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 2006 ISDA Definitions
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISDA Disclosure Annex for Commodity Derivative Transactions. See https://globalmarkets.bnpparibas.com/gm/features/docs/dfdisclosures/ISDA_Commodity_Derivatives_Disclosure_Annex_04_2013.pdf
  disjoint_with:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/FloatingLeg.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FloatingLeg
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentSchedule
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedLeg
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: fixed leg
type: Ontology Class
---

# fixed leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedLeg>

## Definition

swap leg whose paying party is obligated to make payments from time to time over the term of a swap calculated by reference to a fixed annual rate or consisting of at least one payment of a fixed amount

## Relationships

- **Subclass of**: [SwapLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md)

## Constraints

- **Disjoint with**: [FloatingLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/FloatingLeg.md)
- **[hasPaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentSchedule.md)**: min qualified cardinality 0 of type [PaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)

## Annotations

- **label**: fixed leg
- **definition**: swap leg whose paying party is obligated to make payments from time to time over the term of a swap calculated by reference to a fixed annual rate or consisting of at least one payment of a fixed amount
- **adaptedFrom** (en): 2006 ISDA Definitions
- **adaptedFrom** (en): ISDA Disclosure Annex for Commodity Derivative Transactions. See https://globalmarkets.bnpparibas.com/gm/features/docs/dfdisclosures/ISDA_Commodity_Derivatives_Disclosure_Annex_04_2013.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
