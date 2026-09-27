---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has earliest redemption date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a date on or after which a stock can be redeemed
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityRedemptionProvision
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasEarliestRedemptionDate
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has earliest redemption date
type: Ontology Property
---

# has earliest redemption date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasEarliestRedemptionDate>

## Definition

indicates a date on or after which a stock can be redeemed

## Relationships

- **Domain**: [EquityRedemptionProvision](/concepts/fibo/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md)
- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label**: has earliest redemption date
- **definition**: indicates a date on or after which a stock can be redeemed

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
