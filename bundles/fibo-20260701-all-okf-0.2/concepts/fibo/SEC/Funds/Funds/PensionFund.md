---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pension fund
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment fund run by a financial intermediary on behalf of an organization and its employees/members
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A pension fund is a common asset pool meant to generate stable growth over a long-term investment horizon.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/ManagedInvestment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/PensionFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: pension fund
type: Ontology Class
---

# pension fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/PensionFund>

## Definition

investment fund run by a financial intermediary on behalf of an organization and its employees/members

## Relationships

- **Subclass of**: [ManagedInvestment](/concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md)

## Annotations

- **label** (en): pension fund
- **definition** (en): investment fund run by a financial intermediary on behalf of an organization and its employees/members
- **adaptedFrom** (en): ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth edition, October 2019
- **explanatoryNote** (en): A pension fund is a common asset pool meant to generate stable growth over a long-term investment horizon.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
