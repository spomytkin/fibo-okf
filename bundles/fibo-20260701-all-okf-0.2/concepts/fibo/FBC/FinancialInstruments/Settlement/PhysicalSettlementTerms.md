---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: physical settlement terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: commitment to deliver the actual underlying asset on the specified delivery date, rather than cash
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'If you sell a gold futures contract of say 100 troy ounces then you have to deliver real gold to the buyer on
      the mutually agreed date. Most derivatives are not actually exercised, but are traded out before their delivery date.
      However, physical delivery still occurs with some trades: it is most common with commodities, but can also occur with
      other financial instruments.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/hasDeliveryMethod
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/PhysicalDeliveryMethod
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/EscrowAgent
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/PhysicalSettlementTerms
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
- id: fibo-source-89377f435c
  resource: references/fibo/FBC/FinancialInstruments/Settlement.rdf
  sha256: 89377f435ce3f9d5ae76a4c2bf85b0591df9c10d237d0a2ca9700d9da0c4da5c
  title: FIBO source FBC/FinancialInstruments/Settlement.rdf
title: physical settlement terms
type: Ontology Class
---

# physical settlement terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/PhysicalSettlementTerms>

## Definition

commitment to deliver the actual underlying asset on the specified delivery date, rather than cash

## Relationships

- **Subclass of**: [SettlementTerms](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)

## Constraints

- **[hasDeliveryMethod](/concepts/fibo/FBC/FinancialInstruments/Settlement/hasDeliveryMethod.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/PhysicalDeliveryMethod`
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: min qualified cardinality 0 of type [EscrowAgent](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/EscrowAgent.md)

## Annotations

- **label** (en): physical settlement terms
- **definition** (en): commitment to deliver the actual underlying asset on the specified delivery date, rather than cash
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): If you sell a gold futures contract of say 100 troy ounces then you have to deliver real gold to the buyer on the mutually agreed date. Most derivatives are not actually exercised, but are traded out before their delivery date. However, physical delivery still occurs with some trades: it is most common with commodities, but can also occur with other financial instruments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
