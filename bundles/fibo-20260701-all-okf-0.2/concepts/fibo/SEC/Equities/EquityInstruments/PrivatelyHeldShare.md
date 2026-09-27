---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: privately held share
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: share in a security that signifies ownership in an entity that is not publicly traded
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Privately owned companies include family-owned businesses, sole proprietorships and the vast majority of small
      and medium-sized businesses. These companies are often too small for an initial public offering (IPO) due, for example
      to a small market capitalization and/or low trading volume, and fulfill their financing requirements in other ways,
      including through smaller offerings.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/ListedShare.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ListedShare
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PrivatelyHeldShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: privately held share
type: Ontology Class
---

# privately held share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PrivatelyHeldShare>

## Definition

share in a security that signifies ownership in an entity that is not publicly traded

## Relationships

- **Subclass of**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Constraints

- **Disjoint with**: [ListedShare](/concepts/fibo/SEC/Equities/EquityInstruments/ListedShare.md)

## Annotations

- **label** (en): privately held share
- **definition** (en): share in a security that signifies ownership in an entity that is not publicly traded
- **explanatoryNote**: Privately owned companies include family-owned businesses, sole proprietorships and the vast majority of small and medium-sized businesses. These companies are often too small for an initial public offering (IPO) due, for example to a small market capitalization and/or low trading volume, and fulfill their financing requirements in other ways, including through smaller offerings.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
