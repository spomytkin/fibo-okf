---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unique transaction identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters identifying a financial transaction uniquely whenever useful and agreed by the parties or
      community involved in the transaction
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: UTI
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Harmonization of the Unique Transaction Identifier - Technical Guidance, 20 Feb 2017, described in https://www.bis.org/cpmi/publ/d158.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 23897:2020, Financial services - Unique transaction identifier (UTI)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In particular, a UTI will help to ensure the consistent aggregation of OTC derivatives and other securities transactions
      by minimising the likelihood that the same transaction will be counted more than once (for instance, because it is reported
      by more than one counterparty to a transaction, or to more than one trade repository (TR)).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalEntity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasGeneratingEntity
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/SecuritiesTransaction
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/UniqueTransactionIdentifier
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: unique transaction identifier
type: Ontology Class
---

# unique transaction identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/UniqueTransactionIdentifier>

## Definition

sequence of characters identifying a financial transaction uniquely whenever useful and agreed by the parties or community involved in the transaction

## Relationships

- **Subclass of**: [TradeIdentifier](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier.md)

## Constraints

- **[hasGeneratingEntity](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/hasGeneratingEntity.md)**: some values from of type [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [SecuritiesTransaction](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/SecuritiesTransaction.md)

## Annotations

- **label**: unique transaction identifier
- **definition**: sequence of characters identifying a financial transaction uniquely whenever useful and agreed by the parties or community involved in the transaction
- **abbreviation**: UTI
- **adaptedFrom**: Harmonization of the Unique Transaction Identifier - Technical Guidance, 20 Feb 2017, described in https://www.bis.org/cpmi/publ/d158.pdf
- **adaptedFrom**: ISO 23897:2020, Financial services - Unique transaction identifier (UTI)
- **explanatoryNote**: In particular, a UTI will help to ensure the consistent aggregation of OTC derivatives and other securities transactions by minimising the likelihood that the same transaction will be counted more than once (for instance, because it is reported by more than one counterparty to a transaction, or to more than one trade repository (TR)).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
