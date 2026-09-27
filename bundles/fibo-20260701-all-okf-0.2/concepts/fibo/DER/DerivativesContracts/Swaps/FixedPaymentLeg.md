---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fixed payment leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap leg that specifies contractual terms associated with a schedule of payments for any swap calculated by reference
      to a fixed annual rate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: fixed payment stream terms
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: funding leg
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: 'Payments may be fixed or variable, which is independent from the function of the leg (payments, return etc.).
      The schedule may be expressed in one of two ways: as an explicit schedule of dates or as a formula for determining payment
      dates in advance (taking into account for example roll rules for non working days).'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentSchedule
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedPaymentLeg
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: fixed payment leg
type: Ontology Class
---

# fixed payment leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedPaymentLeg>

## Definition

swap leg that specifies contractual terms associated with a schedule of payments for any swap calculated by reference to a fixed annual rate

## Relationships

- **Subclass of**: [SwapLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md)

## Constraints

- **[hasPaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentSchedule.md)**: some values from of type [PaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)

## Annotations

- **label**: fixed payment leg
- **definition**: swap leg that specifies contractual terms associated with a schedule of payments for any swap calculated by reference to a fixed annual rate
- **synonym**: fixed payment stream terms
- **synonym**: funding leg
- **usageNote**: Payments may be fixed or variable, which is independent from the function of the leg (payments, return etc.). The schedule may be expressed in one of two ways: as an explicit schedule of dates or as a formula for determining payment dates in advance (taking into account for example roll rules for non working days).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
