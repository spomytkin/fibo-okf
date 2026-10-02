---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cash settlement terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contractual commitment to settle in cash
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the security price represents a price per share or per lot, whereas the settlement amount represents
      a total.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the valuation determined via the appraisal of the underlying asset may include a quotation that is either
      an upper limit to the outstanding principal balance of the reference obligation for which the quote should be obtained,
      or a floating rate payer calculation amount.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/hasMinimumQuotationAmount
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CashSettlementMethod
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/hasQuotationMethod
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPricingSource
    value: N5ee6c8980d484752976964e201fb31b0
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/hasDeliveryMethod
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/DeliveryInCash
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/hasSettlementAmount
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ValuationTerms
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/CashSettlementTerms
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
- id: fibo-source-89377f435c
  resource: references/fibo/FBC/FinancialInstruments/Settlement.rdf
  sha256: 89377f435ce3f9d5ae76a4c2bf85b0591df9c10d237d0a2ca9700d9da0c4da5c
  title: FIBO source FBC/FinancialInstruments/Settlement.rdf
title: cash settlement terms
type: Ontology Class
---

# cash settlement terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/CashSettlementTerms>

## Definition

contractual commitment to settle in cash

## Relationships

- **Subclass of**: [SettlementTerms](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)

## Constraints

- **[hasMinimumQuotationAmount](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/hasMinimumQuotationAmount.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasQuotationMethod](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/hasQuotationMethod.md)**: min qualified cardinality 0 of type [CashSettlementMethod](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CashSettlementMethod.md)
- **[hasPricingSource](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasPricingSource.md)**: some values from value `N5ee6c8980d484752976964e201fb31b0`
- **[hasDeliveryMethod](/concepts/fibo/FBC/FinancialInstruments/Settlement/hasDeliveryMethod.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/DeliveryInCash`
- **[hasSettlementAmount](/concepts/fibo/FBC/FinancialInstruments/Settlement/hasSettlementAmount.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)**: min qualified cardinality 0 of type [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [ValuationTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/ValuationTerms.md)

## Annotations

- **label** (en): cash settlement terms
- **definition**: contractual commitment to settle in cash
- **explanatoryNote**: Note that the security price represents a price per share or per lot, whereas the settlement amount represents a total.
- **explanatoryNote** (en): Note that the valuation determined via the appraisal of the underlying asset may include a quotation that is either an upper limit to the outstanding principal balance of the reference obligation for which the quote should be obtained, or a floating rate payer calculation amount.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
