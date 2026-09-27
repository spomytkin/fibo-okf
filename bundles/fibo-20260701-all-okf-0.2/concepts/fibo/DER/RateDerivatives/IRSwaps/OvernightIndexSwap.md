---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: overnight index swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap in which the periodic payments for one leg are based on an overnight interest rate index multiplied by the
      same notional amount upon which payments for the other leg of the swap are based
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: OIS swap
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The interest of the overnight rate portion of the swap is compounded and paid at reset dates. The present value
      for the leg is determined by either compounding of the overnight rate or by taking the geometric average of the rate
      over a given period.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/OvernightRateIndexLeg
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
  subclass_of:
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/OvernightIndexSwap
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: overnight index swap
type: Ontology Class
---

# overnight index swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/OvernightIndexSwap>

## Definition

swap in which the periodic payments for one leg are based on an overnight interest rate index multiplied by the same notional amount upon which payments for the other leg of the swap are based

## Relationships

- **Subclass of**: [InterestRateSwap](/concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)

## Constraints

- **[hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)**: some values from of type [OvernightRateIndexLeg](/concepts/fibo/DER/RateDerivatives/IRSwaps/OvernightRateIndexLeg.md)

## Annotations

- **label** (en): overnight index swap
- **definition** (en): swap in which the periodic payments for one leg are based on an overnight interest rate index multiplied by the same notional amount upon which payments for the other leg of the swap are based
- **abbreviation** (en): OIS swap
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15
- **explanatoryNote** (en): The interest of the overnight rate portion of the swap is compounded and paid at reset dates. The present value for the leg is determined by either compounding of the overnight rate or by taking the geometric average of the rate over a given period.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
