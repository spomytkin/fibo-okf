---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: private equity fund
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment fund used for making investments in various equity (and to a lesser extent debt) securities according
      to an investment strategy associated with private equity
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: PE fund
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Private equity funds are typically structured as limited partnerships or limited liability companies, wherein investors
      are limited partners, and the fund is managed by one or more general partners. It is composed of investors and funds
      that invest directly in private companies, or that engage in buyouts of public companies, resulting in the delisting
      of the public equity.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/PrivateFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PrivateFund
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/PrivateEquityFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: private equity fund
type: Ontology Class
---

# private equity fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/PrivateEquityFund>

## Definition

investment fund used for making investments in various equity (and to a lesser extent debt) securities according to an investment strategy associated with private equity

## Relationships

- **Subclass of**: [PrivateFund](/concepts/fibo/SEC/Securities/Pools/PrivateFund.md)

## Annotations

- **label** (en): private equity fund
- **definition** (en): investment fund used for making investments in various equity (and to a lesser extent debt) securities according to an investment strategy associated with private equity
- **abbreviation** (en): PE fund
- **adaptedFrom** (en): ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth edition, October 2019
- **explanatoryNote** (en): Private equity funds are typically structured as limited partnerships or limited liability companies, wherein investors are limited partners, and the fund is managed by one or more general partners. It is composed of investors and funds that invest directly in private companies, or that engage in buyouts of public companies, resulting in the delisting of the public equity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
