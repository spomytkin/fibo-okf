---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: redeemable preferred share with extendable maturity date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: redeemable preferred share with a fixed maturity date whose issuer has the option to extend the maturity date
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasExtendableMaturityDate
    value: 'true'
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithFixedMaturityDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithFixedMaturityDate
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/RedeemablePreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RedeemablePreferredShare
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RedeemablePreferredShareWithExtendableMaturityDate
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: redeemable preferred share with extendable maturity date
type: Ontology Class
---

# redeemable preferred share with extendable maturity date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RedeemablePreferredShareWithExtendableMaturityDate>

## Definition

redeemable preferred share with a fixed maturity date whose issuer has the option to extend the maturity date

## Relationships

- **Subclass of**: [PreferredShareWithFixedMaturityDate](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithFixedMaturityDate.md)
- **Subclass of**: [RedeemablePreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/RedeemablePreferredShare.md)

## Constraints

- **[hasExtendableMaturityDate](/concepts/fibo/SEC/Equities/EquityInstruments/hasExtendableMaturityDate.md)**: has value value `true`

## Annotations

- **label**: redeemable preferred share with extendable maturity date
- **definition**: redeemable preferred share with a fixed maturity date whose issuer has the option to extend the maturity date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
