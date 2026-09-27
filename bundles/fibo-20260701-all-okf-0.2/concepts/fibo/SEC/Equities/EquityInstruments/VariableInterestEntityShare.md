---
owl:
  annotations:
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: variable interest entity share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: share that certifies ownership of a contractual right to a percentage of a company's profits
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Unlike a traditional stock certificate, the VIE share provides a legal proprietary interest in a completely separate
      company's assets, sometimes referred to as a shell company. The contractual right certified by the VIE share is derived
      from a contract between (1) the company named on the VIE share and (2) the shell company. In other words, VIE shareholders
      only have a traditional stock certificate in the completely separate shell company, which is entitled to a percentage
      of the named company's profits via a private contract.
  - language: en-GB
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: VIE share
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: N899d65845af04a2bbdb14a2295d8c426
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/VariableInterestEntityShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: variable interest entity share
type: Ontology Class
---

# variable interest entity share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/VariableInterestEntityShare>

## Definition

share that certifies ownership of a contractual right to a percentage of a company's profits

## Relationships

- **Subclass of**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from value `N899d65845af04a2bbdb14a2295d8c426`

## Annotations

- **label** (en-US): variable interest entity share
- **definition**: share that certifies ownership of a contractual right to a percentage of a company's profits
- **explanatoryNote**: Unlike a traditional stock certificate, the VIE share provides a legal proprietary interest in a completely separate company's assets, sometimes referred to as a shell company. The contractual right certified by the VIE share is derived from a contract between (1) the company named on the VIE share and (2) the shell company. In other words, VIE shareholders only have a traditional stock certificate in the completely separate shell company, which is entitled to a percentage of the named company's profits via a private contract.
- **synonym** (en-GB): VIE share

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
