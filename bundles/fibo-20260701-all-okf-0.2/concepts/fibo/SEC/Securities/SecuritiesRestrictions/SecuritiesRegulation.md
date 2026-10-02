---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: securities regulation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: regulation codified in law specific to securities and investments
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/StatuteLaw
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Regulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Regulation
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRegulation
sources:
- id: fibo-source-241669b0c1
  resource: references/fibo/SEC/Securities/SecuritiesRestrictions.rdf
  sha256: 241669b0c114de2a69849d3c5ae0b04d6c14efbda13080a5a41e98a49ceef1f2
  title: FIBO source SEC/Securities/SecuritiesRestrictions.rdf
title: securities regulation
type: Ontology Class
---

# securities regulation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRegulation>

## Definition

regulation codified in law specific to securities and investments

## Relationships

- **Subclass of**: [Regulation](/concepts/fibo/FND/Law/LegalCapacity/Regulation.md)

## Constraints

- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: some values from of type [StatuteLaw](/concepts/fibo/FND/Law/LegalCore/StatuteLaw.md)
- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: all values from of type [SecuritiesRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md)

## Annotations

- **label**: securities regulation
- **definition**: regulation codified in law specific to securities and investments

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
