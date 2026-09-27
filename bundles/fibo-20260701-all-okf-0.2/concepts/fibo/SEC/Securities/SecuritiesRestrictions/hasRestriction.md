---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has restriction
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a restriction applicable to a given financial instrument or listing
  range:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/specifies
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/hasRestriction
sources:
- id: fibo-source-241669b0c1
  resource: references/fibo/SEC/Securities/SecuritiesRestrictions.rdf
  sha256: 241669b0c114de2a69849d3c5ae0b04d6c14efbda13080a5a41e98a49ceef1f2
  title: FIBO source SEC/Securities/SecuritiesRestrictions.rdf
title: has restriction
type: Ontology Property
---

# has restriction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/hasRestriction>

## Definition

identifies a restriction applicable to a given financial instrument or listing

## Relationships

- **Range**: [SecuritiesRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md)
- **Subproperty of**: [specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)

## Annotations

- **label**: has restriction
- **definition**: identifies a restriction applicable to a given financial instrument or listing

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
