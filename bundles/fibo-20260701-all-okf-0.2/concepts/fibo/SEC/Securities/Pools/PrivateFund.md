---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: private fund
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: managed investment that cannot offer securities to the public
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Private funds are not required to be registered or regulated as investment companies under the U.S. federal securities
      laws. They raise capital from investors through exempt offerings, which means the offering must fall within an exemption
      from registration under the Securities Act of 1933.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isPrivate
    value: 'true'
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/private-funds
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/ManagedInvestment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PrivateFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
- id: fibo-source-73259da08c
  resource: references/fibo/SEC/Securities/Pools.rdf
  sha256: 73259da08ce2d3336ab19acd98a9182e1bef062fb636a27936e96545e083ec39
  title: FIBO source SEC/Securities/Pools.rdf
title: private fund
type: Ontology Class
---

# private fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PrivateFund>

## Definition

managed investment that cannot offer securities to the public

## Relationships

- **See also**: [private-funds](<https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/private-funds>)
- **Subclass of**: [ManagedInvestment](/concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md)

## Constraints

- **[isPrivate](/concepts/fibo/SEC/Funds/Funds/isPrivate.md)**: has value value `true`

## Annotations

- **label**: private fund
- **definition**: managed investment that cannot offer securities to the public
- **explanatoryNote**: Private funds are not required to be registered or regulated as investment companies under the U.S. federal securities laws. They raise capital from investors through exempt offerings, which means the offering must fall within an exemption from registration under the Securities Act of 1933.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
