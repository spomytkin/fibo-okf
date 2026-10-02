---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is held by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the party that possesses and has at least partial control of something, regardless of ownership
  inverse_of:
  - concept: /concepts/fibo/FND/Relations/Relations/holds.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/experiencesWith
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
sources:
- id: fibo-source-2c7ef9cc41
  resource: references/fibo/FND/Parties/Parties.rdf
  sha256: 2c7ef9cc4107e85b5bba3894094e496bcf4e8fe3ef9d6ce3b7d0830fb284f61d
  title: FIBO source FND/Parties/Parties.rdf
- id: fibo-source-5bd2fc8cf9
  resource: references/fibo/FND/Relations/Relations.rdf
  sha256: 5bd2fc8cf9713fc293309a78a9ec760e0eacc6a4c5e9499bbbb29b4f8a172fa2
  title: FIBO source FND/Relations/Relations.rdf
title: is held by
type: Ontology Property
---

# is held by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy>

## Definition

indicates the party that possesses and has at least partial control of something, regardless of ownership

## Relationships

- **Inverse of**: [holds](/concepts/fibo/FND/Relations/Relations/holds.md)
- **Subproperty of**: [experiencesWith](<https://www.omg.org/spec/Commons/PartiesAndSituations/experiencesWith>)

## Annotations

- **label**: is held by
- **definition**: indicates the party that possesses and has at least partial control of something, regardless of ownership

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
