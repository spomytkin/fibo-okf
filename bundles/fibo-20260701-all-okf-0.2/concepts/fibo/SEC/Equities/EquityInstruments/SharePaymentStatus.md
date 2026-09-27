---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: share payment status
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier that specifies the overall payment status for shares issued
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: When a company issues shares upon incorporation or through an initial or secondary issuance, shareholders are required
      to pay a set amount for those shares. Once the company has received the full amount from shareholders, the shares become
      fully paid shares.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStatus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStatus
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SharePaymentStatus
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: share payment status
type: Ontology Class
---

# share payment status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SharePaymentStatus>

## Definition

classifier that specifies the overall payment status for shares issued

## Relationships

- **Subclass of**: [LifecycleStatus](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStatus.md)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Annotations

- **label**: share payment status
- **definition**: classifier that specifies the overall payment status for shares issued
- **explanatoryNote**: When a company issues shares upon incorporation or through an initial or secondary issuance, shareholders are required to pay a set amount for those shares. Once the company has received the full amount from shareholders, the shares become fully paid shares.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
