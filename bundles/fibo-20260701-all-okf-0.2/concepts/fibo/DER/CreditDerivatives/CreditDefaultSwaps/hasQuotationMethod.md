---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has quotation method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the nature of the pricing quotations to be requested from banks and/or dealers when determining the market
      value of the reference obligation for purposes of cash settlement
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/Settlement/CashSettlementTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/CashSettlementTerms
  range:
  - concept: /concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CashSettlementMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CashSettlementMethod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/hasQuotationMethod
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: has quotation method
type: Ontology Property
---

# has quotation method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/hasQuotationMethod>

## Definition

indicates the nature of the pricing quotations to be requested from banks and/or dealers when determining the market value of the reference obligation for purposes of cash settlement

## Relationships

- **Domain**: [CashSettlementTerms](/concepts/fibo/FBC/FinancialInstruments/Settlement/CashSettlementTerms.md)
- **Range**: [CashSettlementMethod](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CashSettlementMethod.md)
- **Subproperty of**: [hasPriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod.md)

## Annotations

- **label** (en): has quotation method
- **definition** (en): indicates the nature of the pricing quotations to be requested from banks and/or dealers when determining the market value of the reference obligation for purposes of cash settlement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
