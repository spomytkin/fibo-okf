---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: hedge fund
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment fund that pursues a total return and is usually open to qualified investors only
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth edition, October 2019
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/Funds/OpenEndInvestment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/OpenEndInvestment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/HedgeFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: hedge fund
type: Ontology Class
---

# hedge fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/HedgeFund>

## Definition

investment fund that pursues a total return and is usually open to qualified investors only

## Relationships

- **Subclass of**: [OpenEndInvestment](/concepts/fibo/SEC/Funds/Funds/OpenEndInvestment.md)

## Annotations

- **label** (en): hedge fund
- **definition** (en): investment fund that pursues a total return and is usually open to qualified investors only
- **adaptedFrom** (en): ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth edition, October 2019

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
