---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cash flow
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the movement of money from some source to some sink
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: From the perspective of an individual investor, the transaction date is the day when the investor's order is executed
      in the market. However, the process doesn't end there. The value date, on the other hand, is when the transaction actually
      settles, meaning when the buyer receives the securities and the seller gets the money. This lag between the transaction
      and value dates is known as the settlement period, which can vary depending on the type of security involved.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: One of the primary concepts in value dating is the 'value date', which is the date on which the funds from a transaction
      are considered available for use. This date can be influenced by various factors, including the type of transaction,
      the currencies involved, and the policies of the financial institutions handling the transaction. For instance, in international
      transactions, the value date might be delayed due to the time required for currency conversion and cross-border fund
      transfers.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    kind: exact_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/hasSourceOfMoney
  - cardinality: 1
    kind: exact_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/hasTargetOfMoney
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://fastercapital.com/content/Transaction-Date--Transaction-Date-vs--Value-Date--Understanding-the-Timeline-of-Your-Money.html#Introduction-to-Transaction-Dates-and-Value-Dates
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/CashFlow
sources:
- id: fibo-source-11f30e320a
  resource: references/fibo/FND/Accounting/CashFlows.rdf
  sha256: 11f30e320a47607eb0377d4c97d55d7f8607ad5ba323af00057df476c78573e2
  title: FIBO source FND/Accounting/CashFlows.rdf
title: cash flow
type: Ontology Class
---

# cash flow

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/CashFlow>

## Definition

the movement of money from some source to some sink

## Relationships

- **See also**: [Introduction-to-Transaction-Dates-and-Value-Dates](<https://fastercapital.com/content/Transaction-Date--Transaction-Date-vs--Value-Date--Understanding-the-Timeline-of-Your-Money.html#Introduction-to-Transaction-Dates-and-Value-Dates>)
- **Subclass of**: [DatedCollectionConstituent](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)

## Constraints

- **[hasSourceOfMoney](/concepts/fibo/FND/Accounting/CashFlows/hasSourceOfMoney.md)**: exact cardinality 1
- **[hasTargetOfMoney](/concepts/fibo/FND/Accounting/CashFlows/hasTargetOfMoney.md)**: exact cardinality 1
- **[hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)**: exact qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: cash flow
- **definition**: the movement of money from some source to some sink
- **explanatoryNote**: From the perspective of an individual investor, the transaction date is the day when the investor's order is executed in the market. However, the process doesn't end there. The value date, on the other hand, is when the transaction actually settles, meaning when the buyer receives the securities and the seller gets the money. This lag between the transaction and value dates is known as the settlement period, which can vary depending on the type of security involved.
- **explanatoryNote**: One of the primary concepts in value dating is the 'value date', which is the date on which the funds from a transaction are considered available for use. This date can be influenced by various factors, including the type of transaction, the currencies involved, and the policies of the financial institutions handling the transaction. For instance, in international transactions, the value date might be delayed due to the time required for currency conversion and cross-border fund transfers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
