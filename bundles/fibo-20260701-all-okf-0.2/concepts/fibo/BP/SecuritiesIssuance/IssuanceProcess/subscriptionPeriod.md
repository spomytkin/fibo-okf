---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: subscription period
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Period during which the security can be subscribed to.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssueSubscriptionInformation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssueSubscriptionInformation
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/subscriptionPeriod
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: subscription period
type: Ontology Property
---

# subscription period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/subscriptionPeriod>

## Definition

Period during which the security can be subscribed to.

## Relationships

- **Domain**: [IssueSubscriptionInformation](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssueSubscriptionInformation.md)
- **Range**: [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label** (en): subscription period
- **definition** (en): Period during which the security can be subscribed to.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
