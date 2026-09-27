---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: minimum issue subscription
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Minimum or incremental denomination required for the transfer or change of ownership of a security.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssueSubscriptionInformation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssueSubscriptionInformation
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/minimumIssueSubscription
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: minimum issue subscription
type: Ontology Property
---

# minimum issue subscription

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/minimumIssueSubscription>

## Definition

Minimum or incremental denomination required for the transfer or change of ownership of a security.

## Relationships

- **Domain**: [IssueSubscriptionInformation](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssueSubscriptionInformation.md)
- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label** (en): minimum issue subscription
- **definition** (en): Minimum or incremental denomination required for the transfer or change of ownership of a security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
