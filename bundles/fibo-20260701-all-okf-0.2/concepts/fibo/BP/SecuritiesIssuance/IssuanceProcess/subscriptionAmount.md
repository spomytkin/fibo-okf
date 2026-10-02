---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: subscription amount
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Number of units of the issue that an individual subscriber is allocated.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SubscriptionClosingInformation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SubscriptionClosingInformation
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#integer
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/subscriptionAmount
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: subscription amount
type: Ontology Property
---

# subscription amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/subscriptionAmount>

## Definition

Number of units of the issue that an individual subscriber is allocated.

## Relationships

- **Domain**: [SubscriptionClosingInformation](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SubscriptionClosingInformation.md)
- **Range**: [integer](<http://www.w3.org/2001/XMLSchema#integer>)

## Annotations

- **label** (en): subscription amount
- **definition** (en): Number of units of the issue that an individual subscriber is allocated.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
