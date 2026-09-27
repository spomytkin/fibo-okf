---
owl:
  annotations:
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: common share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: share that signifies a unit of ownership in a corporation and represents a claim on part of the corporation's assets
      and earnings
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the event that the corporation is liquidated, claims of secured and unsecured creditors and owners of bonds
      and preferred shares take precedence over claims of common share holders.
  - language: en-GB
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: ordinary share
  disjoint_with:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/OrdinaryDividend
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividend
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/CommonShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: common share
type: Ontology Class
---

# common share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/CommonShare>

## Definition

share that signifies a unit of ownership in a corporation and represents a claim on part of the corporation's assets and earnings

## Relationships

- **Subclass of**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Constraints

- **Disjoint with**: [PreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md)
- **[hasDividend](/concepts/fibo/SEC/Equities/EquityInstruments/hasDividend.md)**: min qualified cardinality 0 of type [OrdinaryDividend](/concepts/fibo/SEC/Equities/EquityInstruments/OrdinaryDividend.md)

## Annotations

- **label** (en-US): common share
- **definition**: share that signifies a unit of ownership in a corporation and represents a claim on part of the corporation's assets and earnings
- **explanatoryNote**: In the event that the corporation is liquidated, claims of secured and unsecured creditors and owners of bonds and preferred shares take precedence over claims of common share holders.
- **synonym** (en-GB): ordinary share

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
