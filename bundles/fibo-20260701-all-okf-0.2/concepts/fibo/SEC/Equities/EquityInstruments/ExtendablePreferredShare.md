---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: extendable preferred share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share whose redemption date can be extended at the issuer or holder option
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An extendable preferred share may be redeemed at the option of the issuer and/or of the shareholder with an extendable
      redemption (meturity) date.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: extendible preferred share
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ExtendablePreferredShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: extendable preferred share
type: Ontology Class
---

# extendable preferred share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ExtendablePreferredShare>

## Definition

preferred share whose redemption date can be extended at the issuer or holder option

## Relationships

- **Subclass of**: [PreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md)

## Annotations

- **label**: extendable preferred share
- **definition**: preferred share whose redemption date can be extended at the issuer or holder option
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote**: An extendable preferred share may be redeemed at the option of the issuer and/or of the shareholder with an extendable redemption (meturity) date.
- **synonym**: extendible preferred share

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
