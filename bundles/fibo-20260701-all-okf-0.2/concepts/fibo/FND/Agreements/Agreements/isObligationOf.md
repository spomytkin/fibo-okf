---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is obligation of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a party that has a given obligation
  range:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Obligor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligor
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/isObligationOf
sources:
- id: fibo-source-e7ad375c83
  resource: references/fibo/FND/Agreements/Agreements.rdf
  sha256: e7ad375c83c6ea909be45886e03aec3dd509a8c794a40149ee25f56176cbee08
  title: FIBO source FND/Agreements/Agreements.rdf
title: is obligation of
type: Ontology Property
---

# is obligation of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/isObligationOf>

## Definition

identifies a party that has a given obligation

## Relationships

- **Range**: [Obligor](/concepts/fibo/FND/Agreements/Agreements/Obligor.md)
- **Subproperty of**: [hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)

## Annotations

- **label**: is obligation of
- **definition**: identifies a party that has a given obligation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
