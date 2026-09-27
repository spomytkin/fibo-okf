---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: treasury bill
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: short-term zero coupon treasury obligation with a maturity ranging from one to twelve months
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: T-bill
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The pricing of T-bills is unique among U.S. government debt issues. Treasury bills are offered in multiples of
      $100 and in terms ranging from a few days to 52 weeks. Rather than providing interest payments as Treasury Bonds or
      Notes do, T-bills are sold at a discount, and the entire return is realized upon maturity. The price of a bill is determined
      at auction. The annualized interest rate earned on T-bills is equal to the difference between the purchase price and
      maturity value, divided by the maturity value.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtIssue
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/AtADiscount
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtMaturity
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/ParValue
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.treasurydirect.gov/indiv/research/indepth/tbills/res_tbill.htm
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.treasurydirect.gov/indiv/research/indepth/tbills/res_tbill_rates.htm
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/USTreasurySecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/USTreasurySecurity
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryBill
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: treasury bill
type: Ontology Class
---

# treasury bill

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryBill>

## Definition

short-term zero coupon treasury obligation with a maturity ranging from one to twelve months

## Relationships

- **See also**: [res_tbill.htm](<https://www.treasurydirect.gov/indiv/research/indepth/tbills/res_tbill.htm>)
- **See also**: [res_tbill_rates.htm](<https://www.treasurydirect.gov/indiv/research/indepth/tbills/res_tbill_rates.htm>)
- **Subclass of**: [USTreasurySecurity](/concepts/fibo/SEC/Debt/Bonds/USTreasurySecurity.md)
- **Subclass of**: [MoneyMarketInstrument](/concepts/fibo/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md)

## Constraints

- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: some values from of type [ReferenceInterestRate](/concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md)
- **[hasRelativePriceAtIssue](/concepts/fibo/SEC/Debt/DebtInstruments/hasRelativePriceAtIssue.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/AtADiscount`
- **[hasRelativePriceAtMaturity](/concepts/fibo/SEC/Debt/DebtInstruments/hasRelativePriceAtMaturity.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/ParValue`

## Annotations

- **label**: treasury bill
- **definition**: short-term zero coupon treasury obligation with a maturity ranging from one to twelve months
- **abbreviation**: T-bill
- **explanatoryNote**: The pricing of T-bills is unique among U.S. government debt issues. Treasury bills are offered in multiples of $100 and in terms ranging from a few days to 52 weeks. Rather than providing interest payments as Treasury Bonds or Notes do, T-bills are sold at a discount, and the entire return is realized upon maturity. The price of a bill is determined at auction. The annualized interest rate earned on T-bills is equal to the difference between the purchase price and maturity value, divided by the maturity value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
