---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mutual fund
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: open-end professionally managed investment fund established for the purpose of investing in securities such as
      stocks, bonds, money market instruments and similar assets
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: standard (vanilla) investment fund
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/Funds/OpenEndInvestment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/OpenEndInvestment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/MutualFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: mutual fund
type: Ontology Class
---

# mutual fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/MutualFund>

## Definition

open-end professionally managed investment fund established for the purpose of investing in securities such as stocks, bonds, money market instruments and similar assets

## Relationships

- **Subclass of**: [OpenEndInvestment](/concepts/fibo/SEC/Funds/Funds/OpenEndInvestment.md)

## Annotations

- **label** (en): mutual fund
- **definition** (en): open-end professionally managed investment fund established for the purpose of investing in securities such as stocks, bonds, money market instruments and similar assets
- **adaptedFrom** (en): ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth edition, October 2019
- **synonym** (en): standard (vanilla) investment fund

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
