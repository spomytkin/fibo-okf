---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: allotment information
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Information about the allotment of quantities of the issue to different subscribers. This relates a single instrument
      allotment against the subscription amounts allotted to each Subscriber.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/describesAllotmentOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SubscriptionClosingInformation
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/AllotmentInformation
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: allotment information
type: Ontology Class
---

# allotment information

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/AllotmentInformation>

## Definition

Information about the allotment of quantities of the issue to different subscribers. This relates a single instrument allotment against the subscription amounts allotted to each Subscriber.

## Relationships

- **Subclass of**: [TradedInstrumentIssuanceProcessInformation](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md)

## Constraints

- **[describesAllotmentOf](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/describesAllotmentOf.md)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [SubscriptionClosingInformation](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SubscriptionClosingInformation.md)

## Annotations

- **label** (en): allotment information
- **definition** (en): Information about the allotment of quantities of the issue to different subscribers. This relates a single instrument allotment against the subscription amounts allotted to each Subscriber.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
