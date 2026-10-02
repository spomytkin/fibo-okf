---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: actual closing date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The Closing Date for the Issue, recorded after the event.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/actualClosingDate
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: actual closing date
type: Ontology Property
---

# actual closing date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/actualClosingDate>

## Definition

The Closing Date for the Issue, recorded after the event.

## Relationships

- **Domain**: [IssuedSecurityIssueInformation](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation.md)
- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label** (en): actual closing date
- **definition** (en): The Closing Date for the Issue, recorded after the event.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
