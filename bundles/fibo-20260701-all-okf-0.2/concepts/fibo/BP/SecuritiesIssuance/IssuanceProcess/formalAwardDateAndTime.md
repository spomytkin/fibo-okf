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
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/OfferingProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/OfferingProcess
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/formalAwardDateAndTime
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: formal award date and time
type: Ontology Property
---

# formal award date and time

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/formalAwardDateAndTime>

## Definition

Date and time the issuer formally accepts a bid for Competitive Issues or, the Date and Time the Bond Purchase Agreement is executed for Negotiated Issues. Time Zone: Include in date/time data or add a term for it?

## Relationships

- **Domain**: [OfferingProcess](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/OfferingProcess.md)
- **Range**: [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)

## Annotations

- **label** (en): formal award date and time
- **definition** (en): Date and time the issuer formally accepts a bid for Competitive Issues or, the Date and Time the Bond Purchase Agreement is executed for Negotiated Issues. Time Zone: Include in date/time data or add a term for it?

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
