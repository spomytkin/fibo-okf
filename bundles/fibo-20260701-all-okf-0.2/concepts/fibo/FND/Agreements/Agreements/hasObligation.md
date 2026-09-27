---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has obligation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a duty or obligation that a given party has taken on
  domain:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Obligor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligor
  inverse_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/isObligationOf.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/isObligationOf
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/hasObligation
sources:
- id: fibo-source-e7ad375c83
  resource: references/fibo/FND/Agreements/Agreements.rdf
  sha256: e7ad375c83c6ea909be45886e03aec3dd509a8c794a40149ee25f56176cbee08
  title: FIBO source FND/Agreements/Agreements.rdf
title: has obligation
type: Ontology Property
---

# has obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/hasObligation>

## Definition

identifies a duty or obligation that a given party has taken on

## Relationships

- **Domain**: [Obligor](/concepts/fibo/FND/Agreements/Agreements/Obligor.md)
- **Inverse of**: [isObligationOf](/concepts/fibo/FND/Agreements/Agreements/isObligationOf.md)

## Annotations

- **label**: has obligation
- **definition**: identifies a duty or obligation that a given party has taken on

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
