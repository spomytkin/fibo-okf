---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: holds
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: is the relationship between a party and something it possesses, or over which it exercises some ownership or control
      or has at its discretion the ability to dispose of it as it sees fit
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/directlyAffects
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds
sources:
- id: fibo-source-2c7ef9cc41
  resource: references/fibo/FND/Parties/Parties.rdf
  sha256: 2c7ef9cc4107e85b5bba3894094e496bcf4e8fe3ef9d6ce3b7d0830fb284f61d
  title: FIBO source FND/Parties/Parties.rdf
- id: fibo-source-5bd2fc8cf9
  resource: references/fibo/FND/Relations/Relations.rdf
  sha256: 5bd2fc8cf9713fc293309a78a9ec760e0eacc6a4c5e9499bbbb29b4f8a172fa2
  title: FIBO source FND/Relations/Relations.rdf
title: holds
type: Ontology Property
---

# holds

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds>

## Definition

is the relationship between a party and something it possesses, or over which it exercises some ownership or control or has at its discretion the ability to dispose of it as it sees fit

## Relationships

- **Subproperty of**: [directlyAffects](<https://www.omg.org/spec/Commons/PartiesAndSituations/directlyAffects>)

## Annotations

- **label**: holds
- **definition**: is the relationship between a party and something it possesses, or over which it exercises some ownership or control or has at its discretion the ability to dispose of it as it sees fit

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
