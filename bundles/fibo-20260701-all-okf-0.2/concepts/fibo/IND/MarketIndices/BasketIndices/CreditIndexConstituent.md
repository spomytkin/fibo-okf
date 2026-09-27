---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit index constituent
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: constituent of a basket of credit risks
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/BasketOfCreditRisks
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isConstituentOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/CreditEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CreditIndexConstituent
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: credit index constituent
type: Ontology Class
---

# credit index constituent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CreditIndexConstituent>

## Definition

constituent of a basket of credit risks

## Relationships

- **Subclass of**: [WeightedBasketConstituent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md)
- **Subclass of**: [DatedCollectionConstituent](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)

## Constraints

- **[hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)**: some values from of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[isConstituentOf](<https://www.omg.org/spec/Commons/Collections/isConstituentOf>)**: some values from of type [BasketOfCreditRisks](/concepts/fibo/IND/MarketIndices/BasketIndices/BasketOfCreditRisks.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [CreditEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/CreditEvent.md)

## Annotations

- **label** (en): credit index constituent
- **definition** (en): constituent of a basket of credit risks

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
