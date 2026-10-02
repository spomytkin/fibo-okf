---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: total return swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: return swap where the seller agrees to pay the other party the difference in value of some underlying asset multiplied
      by an agreed-upon notional value should the asset value increase between specified periods of time
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example the parties may enter into a two year agreement where every three months they compare the value of
      the Barclays Capital Aggregate Bond Index to its value three months previously. If the agreed upon notional was US $10,000,000
      and the value increased 0.04%, or 4 basis points (bps), the seller would pay the buyer US $4,000. If, after another
      three months, the value decreased by 3bps, the buyer would pay the seller US $3,000. As part of the agreement, the buyer
      may also make an additional payment each period to the seller based on a floating rate index multiplied by the notional
      value.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: CFTC Data Dictionary. See https://www.cftc.gov/MarketReports/SwapsReports/DataDictionary/index.htm
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISDA Disclosure Annex for Commodity Derivative Transactions. See https://globalmarkets.bnpparibas.com/gm/features/docs/dfdisclosures/ISDA_Commodity_Derivatives_Disclosure_Annex_04_2013.pdf
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In a total return swap that is index-based, the change in the level of the index will be equal to the returns generated
      by the change in price of each of the contracts that comprise the index plus a return based upon interest earned on
      any cash collateral posted upon the purchase of the contracts comprising the index.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In exchange, the other party, the buyer of the credit risk, agrees to pay the difference in value of the specified
      asset multiplied by the notional value should that value decrease between the same specified periods of time. Total
      return swaps often appear in asset classes other than the credit asset class; however, for the purpose of the CFTC Swaps
      Report, all total return swaps are counted only in the credit asset class.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/TotalReturnLeg
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasReturnLeg
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CreditDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CreditDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/ReturnSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/TotalReturnSwap
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: total return swap
type: Ontology Class
---

# total return swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/TotalReturnSwap>

## Definition

return swap where the seller agrees to pay the other party the difference in value of some underlying asset multiplied by an agreed-upon notional value should the asset value increase between specified periods of time

## Relationships

- **Subclass of**: [CreditDerivative](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CreditDerivative.md)
- **Subclass of**: [ReturnSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/ReturnSwap.md)

## Constraints

- **[hasReturnLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasReturnLeg.md)**: some values from of type [TotalReturnLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/TotalReturnLeg.md)

## Annotations

- **label** (en): total return swap
- **definition** (en): return swap where the seller agrees to pay the other party the difference in value of some underlying asset multiplied by an agreed-upon notional value should the asset value increase between specified periods of time
- **example** (en): For example the parties may enter into a two year agreement where every three months they compare the value of the Barclays Capital Aggregate Bond Index to its value three months previously. If the agreed upon notional was US $10,000,000 and the value increased 0.04%, or 4 basis points (bps), the seller would pay the buyer US $4,000. If, after another three months, the value decreased by 3bps, the buyer would pay the seller US $3,000. As part of the agreement, the buyer may also make an additional payment each period to the seller based on a floating rate index multiplied by the notional value.
- **adaptedFrom** (en): CFTC Data Dictionary. See https://www.cftc.gov/MarketReports/SwapsReports/DataDictionary/index.htm
- **adaptedFrom** (en): ISDA Disclosure Annex for Commodity Derivative Transactions. See https://globalmarkets.bnpparibas.com/gm/features/docs/dfdisclosures/ISDA_Commodity_Derivatives_Disclosure_Annex_04_2013.pdf
- **explanatoryNote** (en): In a total return swap that is index-based, the change in the level of the index will be equal to the returns generated by the change in price of each of the contracts that comprise the index plus a return based upon interest earned on any cash collateral posted upon the purchase of the contracts comprising the index.
- **explanatoryNote** (en): In exchange, the other party, the buyer of the credit risk, agrees to pay the difference in value of the specified asset multiplied by the notional value should that value decrease between the same specified periods of time. Total return swaps often appear in asset classes other than the credit asset class; however, for the purpose of the CFTC Swaps Report, all total return swaps are counted only in the credit asset class.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
