---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option that giving the buyer (holder) the right, but not the obligation, to receive a cash payment if market interest
      rate of a reference rate is higher or lower, depending on the option, than the strike rate of the option
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The amount of the payment will be based on the difference between the market rate on the exercise date and the
      strike rate, multiplied by the notional principal specified in the option contract, to calculate the total payment.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasStrikeRate
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nfb574809ae674bc8b6c268b38a10e2ca
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/VanillaOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/InterestRateOption
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: interest rate option
type: Ontology Class
---

# interest rate option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/InterestRateOption>

## Definition

option that giving the buyer (holder) the right, but not the obligation, to receive a cash payment if market interest rate of a reference rate is higher or lower, depending on the option, than the strike rate of the option

## Relationships

- **Subclass of**: [InterestRateDerivative](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md)
- **Subclass of**: [VanillaOption](/concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md)

## Constraints

- **[hasStrikeRate](/concepts/fibo/DER/DerivativesContracts/Options/hasStrikeRate.md)**: some values from of type [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)
- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nfb574809ae674bc8b6c268b38a10e2ca`

## Annotations

- **label** (en): interest rate option
- **definition** (en): option that giving the buyer (holder) the right, but not the obligation, to receive a cash payment if market interest rate of a reference rate is higher or lower, depending on the option, than the strike rate of the option
- **explanatoryNote** (en): The amount of the payment will be based on the difference between the market rate on the exercise date and the strike rate, multiplied by the notional principal specified in the option contract, to calculate the total payment.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
