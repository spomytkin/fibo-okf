---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit spread
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: yield spread that reflects the additional net yield an investor can earn from a security with more credit risk
      relative to one with less credit risk
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The credit spread of a particular security is often quoted in relation to the yield on a credit risk-free benchmark
      security or reference rate. Further Notes There are several measures of credit spread, including Z-spread and option-adjusted
      spread. Old definition (Algo) The spread between the credit rating of something and its maturity. THis is now defined
      as a different term pending further review with Algorithmics. Update from SMER. difference between risk free price (price
      of govt bond) and the price of this security. (matches Wikipedia definition above) i.e. price of this credit versus
      the price of a (near) risk free credit. The latter is a reference security with low risk such as a Treasury Bond. Is
      this between prices or between yields? can be expressed as either wrt price or yield, and this is detemined by context
      for different markets. Try and get a list. This is more generic - the meaning is not that it is speciufically wrt yield
      as such. Debt Price Spread is in context of price, whereas this is more generic.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/YieldSpread.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/YieldSpread
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/CreditSpread
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: credit spread
type: Ontology Class
---

# credit spread

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/CreditSpread>

## Definition

yield spread that reflects the additional net yield an investor can earn from a security with more credit risk relative to one with less credit risk

## Relationships

- **Subclass of**: [YieldSpread](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/YieldSpread.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [ReferenceInterestRate](/concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md)

## Annotations

- **label** (en): credit spread
- **definition** (en): yield spread that reflects the additional net yield an investor can earn from a security with more credit risk relative to one with less credit risk
- **explanatoryNote** (en): The credit spread of a particular security is often quoted in relation to the yield on a credit risk-free benchmark security or reference rate. Further Notes There are several measures of credit spread, including Z-spread and option-adjusted spread. Old definition (Algo) The spread between the credit rating of something and its maturity. THis is now defined as a different term pending further review with Algorithmics. Update from SMER. difference between risk free price (price of govt bond) and the price of this security. (matches Wikipedia definition above) i.e. price of this credit versus the price of a (near) risk free credit. The latter is a reference security with low risk such as a Treasury Bond. Is this between prices or between yields? can be expressed as either wrt price or yield, and this is detemined by context for different markets. Try and get a list. This is more generic - the meaning is not that it is speciufically wrt yield as such. Debt Price Spread is in context of price, whereas this is more generic.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
