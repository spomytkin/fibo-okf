---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: expected closing date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The date on which the transfer of positions to underwriters is expected to take place. This date is provided by
      underwriters as part of an announcement.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/OfferingProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/OfferingProcess
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/expectedClosingDate
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: expected closing date
type: Ontology Property
---

# expected closing date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/expectedClosingDate>

## Definition

The date on which the transfer of positions to underwriters is expected to take place. This date is provided by underwriters as part of an announcement.

## Relationships

- **Domain**: [OfferingProcess](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/OfferingProcess.md)
- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label** (en): expected closing date
- **definition** (en): The date on which the transfer of positions to underwriters is expected to take place. This date is provided by underwriters as part of an announcement.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
