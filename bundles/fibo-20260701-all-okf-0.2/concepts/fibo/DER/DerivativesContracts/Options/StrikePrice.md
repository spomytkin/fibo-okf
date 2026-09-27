---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: strike price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: price at which a lot of the underlying asset may be bought or sold when the contract is exercised
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For call options, the strike price is the price at which the security may be purchased by the option holder; for
      put options, the strike price is the price at which the security may be sold.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StrikePrice
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: strike price
type: Ontology Class
---

# strike price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StrikePrice>

## Definition

price at which a lot of the underlying asset may be bought or sold when the contract is exercised

## Relationships

- **Subclass of**: [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)

## Annotations

- **label** (en): strike price
- **definition** (en): price at which a lot of the underlying asset may be bought or sold when the contract is exercised
- **explanatoryNote** (en): For call options, the strike price is the price at which the security may be purchased by the option holder; for put options, the strike price is the price at which the security may be sold.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
