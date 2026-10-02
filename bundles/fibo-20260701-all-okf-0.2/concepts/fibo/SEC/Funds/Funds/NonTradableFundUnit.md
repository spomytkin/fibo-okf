---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non-tradable fund unit
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security representing an interest in a fund that cannot be traded ontside of the fund itself
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Non-tradable fund units are commonly found in pension funds, insurance pools, or internal benefit plans, where
      units serve as accounting or entitlement mechanisms without market transferability.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Funds/Funds/TradableFundUnit.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/TradableFundUnit
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/NonNegotiableSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/NonNegotiableSecurity
  - concept: /concepts/fibo/SEC/Funds/Funds/FundUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/NonTradableFundUnit
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: non-tradable fund unit
type: Ontology Class
---

# non-tradable fund unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/NonTradableFundUnit>

## Definition

security representing an interest in a fund that cannot be traded ontside of the fund itself

## Relationships

- **Subclass of**: [NonNegotiableSecurity](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/NonNegotiableSecurity.md)
- **Subclass of**: [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)

## Constraints

- **Disjoint with**: [TradableFundUnit](/concepts/fibo/SEC/Funds/Funds/TradableFundUnit.md)

## Annotations

- **label** (en): non-tradable fund unit
- **definition** (en): security representing an interest in a fund that cannot be traded ontside of the fund itself
- **explanatoryNote**: Non-tradable fund units are commonly found in pension funds, insurance pools, or internal benefit plans, where units serve as accounting or entitlement mechanisms without market transferability.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
