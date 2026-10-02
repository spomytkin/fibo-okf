---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is private
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates that the fund does not offer its securities to the general public
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the U.S., private funds are exempt from certain regulations under the Investment Company Act of 1940. Common
      types include venture capital funds, private equity funds, and some hedge funds. They often target illiquid assets or
      use aggressive strategies, offering flexibility compared to public funds.
  domain:
  - concept: /concepts/fibo/SEC/Securities/Pools/PooledFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PooledFund
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isPrivate
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: is private
type: Ontology Property
---

# is private

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isPrivate>

## Definition

indicates that the fund does not offer its securities to the general public

## Relationships

- **Domain**: [PooledFund](/concepts/fibo/SEC/Securities/Pools/PooledFund.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is private
- **definition** (en): indicates that the fund does not offer its securities to the general public
- **explanatoryNote** (en): In the U.S., private funds are exempt from certain regulations under the Investment Company Act of 1940. Common types include venture capital funds, private equity funds, and some hedge funds. They often target illiquid assets or use aggressive strategies, offering flexibility compared to public funds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
