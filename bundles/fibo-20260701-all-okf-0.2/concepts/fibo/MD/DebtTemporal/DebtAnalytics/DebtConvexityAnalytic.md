---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt convexity analytic
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'The second derivative of a security''s price with respect to its yield, divided by the security''s price. A security
      exhibits positive convexity when its price rises more for a downward move in its yield than its price declines for an
      equal upward move in its yield. Further notes: A measure of the change in price for a given change in Modified Duration.
      This always (necessarily) refers to Modified Duration. This is used as another risk measurement. Numerator is always
      (a) duration - either MacCaulays or Modified. Always rate of change of (one of the) Duration against some other parameter.
      The other paramater can be characterised as a Yield (it may be the Price, but that has a relationship to the Yield in
      any case). REVIEW: Inconsistency in the above - is it always necessarily Modified Duration that is referred to, or "any"
      Duration measure (Macaulays and.or Modified)? notes 9 Dec A measure of the sensitivity of the price with reference to
      interest rates. This is normally determined with reference to maturity, but since there are different maturity dates,
      this figure gives an estimate of the equitvalent if you had a homogenous portfolio, i.e. this is an estimate based on
      a pure equivalent, homogenous portfolio. Convexity of instrument versus portfolio. Sees instrument in terms of the set
      of cashflows. The term Convexity can be applied either to a bond or to a portfolio. More notes: When you get Convexit
      in MD, it will tell you what Duration it is refrfering to, along with Redemption Date (logically). Also if there is
      Option Adjusted Yield, there is a third set of analytics. What are they? i.e. OA Convexity, Duration Yield and the rest.
      Conclusions: Agreed to revisit this in OTC.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DurationAnalytic
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/isRateOfChangeOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketSpread
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtConvexityAnalytic
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: debt convexity analytic
type: Ontology Class
---

# debt convexity analytic

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtConvexityAnalytic>

## Definition

The second derivative of a security's price with respect to its yield, divided by the security's price. A security exhibits positive convexity when its price rises more for a downward move in its yield than its price declines for an equal upward move in its yield. Further notes: A measure of the change in price for a given change in Modified Duration. This always (necessarily) refers to Modified Duration. This is used as another risk measurement. Numerator is always (a) duration - either MacCaulays or Modified. Always rate of change of (one of the) Duration against some other parameter. The other paramater can be characterised as a Yield (it may be the Price, but that has a relationship to the Yield in any case). REVIEW: Inconsistency in the above - is it always necessarily Modified Duration that is referred to, or "any" Duration measure (Macaulays and.or Modified)? notes 9 Dec A measure of the sensitivity of the price with reference to interest rates. This is normally determined with reference to maturity, but since there are different maturity dates, this figure gives an estimate of the equitvalent if you had a homogenous portfolio, i.e. this is an estimate based on a pure equivalent, homogenous portfolio. Convexity of instrument versus portfolio. Sees instrument in terms of the set of cashflows. The term Convexity can be applied either to a bond or to a portfolio. More notes: When you get Convexit in MD, it will tell you what Duration it is refrfering to, along with Redemption Date (logically). Also if there is Option Adjusted Yield, there is a third set of analytics. What are they? i.e. OA Convexity, Duration Yield and the rest. Conclusions: Agreed to revisit this in OTC.

## Relationships

- **Subclass of**: [DatedCollectionConstituent](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)

## Constraints

- **[isRateOfChangeOf](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/isRateOfChangeOf.md)**: some values from of type [DurationAnalytic](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DurationAnalytic.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [MarketSpread](/concepts/fibo/IND/Indicators/Indicators/MarketSpread.md)

## Annotations

- **label** (en): debt convexity analytic
- **definition** (en): The second derivative of a security's price with respect to its yield, divided by the security's price. A security exhibits positive convexity when its price rises more for a downward move in its yield than its price declines for an equal upward move in its yield. Further notes: A measure of the change in price for a given change in Modified Duration. This always (necessarily) refers to Modified Duration. This is used as another risk measurement. Numerator is always (a) duration - either MacCaulays or Modified. Always rate of change of (one of the) Duration against some other parameter. The other paramater can be characterised as a Yield (it may be the Price, but that has a relationship to the Yield in any case). REVIEW: Inconsistency in the above - is it always necessarily Modified Duration that is referred to, or "any" Duration measure (Macaulays and.or Modified)? notes 9 Dec A measure of the sensitivity of the price with reference to interest rates. This is normally determined with reference to maturity, but since there are different maturity dates, this figure gives an estimate of the equitvalent if you had a homogenous portfolio, i.e. this is an estimate based on a pure equivalent, homogenous portfolio. Convexity of instrument versus portfolio. Sees instrument in terms of the set of cashflows. The term Convexity can be applied either to a bond or to a portfolio. More notes: When you get Convexit in MD, it will tell you what Duration it is refrfering to, along with Redemption Date (logically). Also if there is Option Adjusted Yield, there is a third set of analytics. What are they? i.e. OA Convexity, Duration Yield and the rest. Conclusions: Agreed to revisit this in OTC.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
