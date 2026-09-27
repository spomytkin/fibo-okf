---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: formal award date and time
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'Date and time the issuer formally accepts a bid for Competitive Issues or, the Date and Time the Bond Purchase
      Agreement is executed for Negotiated Issues. Time Zone: Include in date/time data or add a term for it?'
  domain:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/DebtOffering
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/formalAwardDateAndTime
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: formal award date and time
type: Ontology Property
---

# formal award date and time

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/formalAwardDateAndTime>

## Definition

Date and time the issuer formally accepts a bid for Competitive Issues or, the Date and Time the Bond Purchase Agreement is executed for Negotiated Issues. Time Zone: Include in date/time data or add a term for it?

## Relationships

- **Domain**: [DebtOffering](/concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md)
- **Range**: [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)

## Annotations

- **label** (en): formal award date and time
- **definition** (en): Date and time the issuer formally accepts a bid for Competitive Issues or, the Date and Time the Bond Purchase Agreement is executed for Negotiated Issues. Time Zone: Include in date/time data or add a term for it?

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
