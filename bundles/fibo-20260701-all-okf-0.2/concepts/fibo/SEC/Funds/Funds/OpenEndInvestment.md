---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: open-end investment
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment fund that offered through a fund company that sells shares directly to investors
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: open-end fund
  disjoint_with:
  - concept: /concepts/fibo/SEC/Funds/Funds/ClosedEndInvestment.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/ClosedEndInvestment
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isOpenEnded
    value: 'true'
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/ManagedInvestment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/OpenEndInvestment
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: open-end investment
type: Ontology Class
---

# open-end investment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/OpenEndInvestment>

## Definition

investment fund that offered through a fund company that sells shares directly to investors

## Relationships

- **Subclass of**: [ManagedInvestment](/concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md)

## Constraints

- **Disjoint with**: [ClosedEndInvestment](/concepts/fibo/SEC/Funds/Funds/ClosedEndInvestment.md)
- **[isOpenEnded](/concepts/fibo/SEC/Funds/Funds/isOpenEnded.md)**: has value value `true`

## Annotations

- **label** (en): open-end investment
- **definition** (en): investment fund that offered through a fund company that sells shares directly to investors
- **synonym** (en): open-end fund

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
