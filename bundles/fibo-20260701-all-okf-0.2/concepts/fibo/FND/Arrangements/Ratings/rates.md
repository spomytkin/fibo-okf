---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rates
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the instrument, party or something else to which a rating applies
  domain:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/Rating.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/Rating
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Classifiers/classifies
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/rates
sources:
- id: fibo-source-7c2fc71488
  resource: references/fibo/FND/Arrangements/Ratings.rdf
  sha256: 7c2fc71488bd4a404f2e849642c58fd6f6f98a8d7814d532f2ebdae686174802
  title: FIBO source FND/Arrangements/Ratings.rdf
title: rates
type: Ontology Property
---

# rates

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/rates>

## Definition

indicates the instrument, party or something else to which a rating applies

## Relationships

- **Domain**: [Rating](/concepts/fibo/FND/Arrangements/Ratings/Rating.md)
- **Subproperty of**: [classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)

## Annotations

- **label**: rates
- **definition**: indicates the instrument, party or something else to which a rating applies

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
