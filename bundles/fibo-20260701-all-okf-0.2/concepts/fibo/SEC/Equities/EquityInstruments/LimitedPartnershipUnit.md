---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: limited partnership unit
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: share in a form of partnership similar to a general partnership, except that in addition to one or more general
      partners (GPs), there are one or more limited partners (LPs)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Like shareholders in a corporation, the LPs have limited liability, i.e., they are only liable on debts incurred
      by the firm to the extent of their registered investment and they have no management authority. The GPs pay the LPs
      the equivalent of a dividend on their investment, the nature and extent of which is usually defined in the partnership
      agreement.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasCounterparty
    value: N3259142a0db348e88a58a35c2510f0e1
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/LimitedPartnershipUnit
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: limited partnership unit
type: Ontology Class
---

# limited partnership unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/LimitedPartnershipUnit>

## Definition

share in a form of partnership similar to a general partnership, except that in addition to one or more general partners (GPs), there are one or more limited partners (LPs)

## Relationships

- **Subclass of**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Constraints

- **[hasCounterparty](/concepts/fibo/FND/Agreements/Contracts/hasCounterparty.md)**: some values from value `N3259142a0db348e88a58a35c2510f0e1`

## Annotations

- **label** (en): limited partnership unit
- **definition** (en): share in a form of partnership similar to a general partnership, except that in addition to one or more general partners (GPs), there are one or more limited partners (LPs)
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): Like shareholders in a corporation, the LPs have limited liability, i.e., they are only liable on debts incurred by the firm to the extent of their registered investment and they have no management authority. The GPs pay the LPs the equivalent of a dividend on their investment, the nature and extent of which is usually defined in the partnership agreement.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
