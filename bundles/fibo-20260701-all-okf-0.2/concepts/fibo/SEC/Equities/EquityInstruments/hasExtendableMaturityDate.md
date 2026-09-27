---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has extendable maturity date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the issuer and/or holders of redeemable shares with a fixed maturity date have the option to
      extend the maturity date
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasExtendableMaturityDate
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has extendable maturity date
type: Ontology Property
---

# has extendable maturity date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasExtendableMaturityDate>

## Definition

indicates whether the issuer and/or holders of redeemable shares with a fixed maturity date have the option to extend the maturity date

## Relationships

- **Domain**: [PreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: has extendable maturity date
- **definition**: indicates whether the issuer and/or holders of redeemable shares with a fixed maturity date have the option to extend the maturity date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
