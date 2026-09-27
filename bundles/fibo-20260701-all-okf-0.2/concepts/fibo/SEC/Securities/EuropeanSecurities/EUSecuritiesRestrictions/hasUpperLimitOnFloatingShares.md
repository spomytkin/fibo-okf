---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has upper limit on floating shares
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the upper limit on the number of free float shares to be reported, if applicable
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasAmount
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/hasUpperLimitOnFloatingShares
sources:
- id: fibo-source-d2c4e0b02d
  resource: references/fibo/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions.rdf
  sha256: d2c4e0b02d30114692ca293e6f51e26b36eef9f530171ac73c4831c6e7869087
  title: FIBO source SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions.rdf
title: has upper limit on floating shares
type: Ontology Property
---

# has upper limit on floating shares

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/hasUpperLimitOnFloatingShares>

## Definition

indicates the upper limit on the number of free float shares to be reported, if applicable

## Relationships

- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **Subproperty of**: [hasAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md)

## Annotations

- **label** (en): has upper limit on floating shares
- **definition** (en): indicates the upper limit on the number of free float shares to be reported, if applicable

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
