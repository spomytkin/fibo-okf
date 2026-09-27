---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: plain vanilla interest rate swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: fixed-float single currency interest rate swap in which interest payments are netted, the notional principal does
      not change, and there are no embedded options
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
    value: N8dc41755dbdd474896cc87111f4b3b38
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
    value: Ncc261f221a8a421d886ace214105bb71
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNotionalAmount
  subclass_of:
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/FixedFloatSingleCurrencyInterestRateSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedFloatSingleCurrencyInterestRateSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/PlainVanillaInterestRateSwap
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: plain vanilla interest rate swap
type: Ontology Class
---

# plain vanilla interest rate swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/PlainVanillaInterestRateSwap>

## Definition

fixed-float single currency interest rate swap in which interest payments are netted, the notional principal does not change, and there are no embedded options

## Relationships

- **Subclass of**: [FixedFloatSingleCurrencyInterestRateSwap](/concepts/fibo/DER/RateDerivatives/IRSwaps/FixedFloatSingleCurrencyInterestRateSwap.md)

## Constraints

- **[hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)**: some values from value `N8dc41755dbdd474896cc87111f4b3b38`
- **[hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)**: some values from value `Ncc261f221a8a421d886ace214105bb71`
- **[hasNotionalAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasNotionalAmount.md)**: exact qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: plain vanilla interest rate swap
- **definition**: fixed-float single currency interest rate swap in which interest payments are netted, the notional principal does not change, and there are no embedded options

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
