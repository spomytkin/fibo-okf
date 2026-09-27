---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: settlement terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms that define the commitment to and mechanism for settling one or more sides of a transaction
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In general, settlement involves arrangement of disposition of property, typically for legal reasons. With respect
      to financial transactions, it involves completion of a trade, either between brokers or agents, or between a broker
      and client. This may include settlement in cash, either for the entire transaction or for the cash leg of a transaction,
      either now or at some specified time in the future.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/DeliveryMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/hasDeliveryMethod
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasSettlementDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/Settlement
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/SettlementConvention
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
sources:
- id: fibo-source-89377f435c
  resource: references/fibo/FBC/FinancialInstruments/Settlement.rdf
  sha256: 89377f435ce3f9d5ae76a4c2bf85b0591df9c10d237d0a2ca9700d9da0c4da5c
  title: FIBO source FBC/FinancialInstruments/Settlement.rdf
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: settlement terms
type: Ontology Class
---

# settlement terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms>

## Definition

contract terms that define the commitment to and mechanism for settling one or more sides of a transaction

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Constraints

- **[hasDeliveryMethod](/concepts/fibo/FBC/FinancialInstruments/Settlement/hasDeliveryMethod.md)**: some values from of type [DeliveryMethod](/concepts/fibo/FBC/FinancialInstruments/Settlement/DeliveryMethod.md)
- **[hasSettlementDate](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/hasSettlementDate.md)**: all values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Settlement](/concepts/fibo/FBC/FinancialInstruments/Settlement/Settlement.md)
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: some values from of type [SettlementConvention](/concepts/fibo/FBC/FinancialInstruments/Settlement/SettlementConvention.md)

## Annotations

- **label**: settlement terms
- **definition**: contract terms that define the commitment to and mechanism for settling one or more sides of a transaction
- **explanatoryNote**: In general, settlement involves arrangement of disposition of property, typically for legal reasons. With respect to financial transactions, it involves completion of a trade, either between brokers or agents, or between a broker and client. This may include settlement in cash, either for the entire transaction or for the cash leg of a transaction, either now or at some specified time in the future.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
