---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: closed-end investment
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment fund that has a fixed number of shares offered by an investment company through an initial public offering
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: closed-end fund
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isOpenEnded
    value: 'false'
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/ManagedInvestment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/ClosedEndInvestment
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: closed-end investment
type: Ontology Class
---

# closed-end investment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/ClosedEndInvestment>

## Definition

investment fund that has a fixed number of shares offered by an investment company through an initial public offering

## Relationships

- **Subclass of**: [ManagedInvestment](/concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md)

## Constraints

- **[isOpenEnded](/concepts/fibo/SEC/Funds/Funds/isOpenEnded.md)**: has value value `false`

## Annotations

- **label** (en): closed-end investment
- **definition** (en): investment fund that has a fixed number of shares offered by an investment company through an initial public offering
- **synonym** (en): closed-end fund

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
