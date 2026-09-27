---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has first trade settlement date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date on which the first trade of a newly issued security is settled
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasFirstTradeSettlementDate
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: has first trade settlement date
type: Ontology Property
---

# has first trade settlement date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasFirstTradeSettlementDate>

## Definition

indicates the date on which the first trade of a newly issued security is settled

## Relationships

- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label**: has first trade settlement date
- **definition**: indicates the date on which the first trade of a newly issued security is settled

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
