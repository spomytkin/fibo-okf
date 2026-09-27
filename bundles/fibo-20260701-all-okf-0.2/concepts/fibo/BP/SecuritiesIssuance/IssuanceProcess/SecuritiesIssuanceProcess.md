---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: securities issuance process
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The process by which a financial security is issued.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecurityIssuanceGuarantor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasIssuanceGuarantor
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/PotentialIssuer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasPotentialIssuer
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/Subscriber
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/subscriber.1
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/produces
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: securities issuance process
type: Ontology Class
---

# securities issuance process

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess>

## Definition

The process by which a financial security is issued.

## Constraints

- **[hasIssuanceGuarantor](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasIssuanceGuarantor.md)**: some values from of type [SecurityIssuanceGuarantor](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecurityIssuanceGuarantor.md)
- **[hasPotentialIssuer](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasPotentialIssuer.md)**: some values from of type [PotentialIssuer](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/PotentialIssuer.md)
- **[subscriber.1](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/subscriber.1.md)**: some values from of type [Subscriber](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/Subscriber.md)
- **[produces](/concepts/fibo/FND/Relations/Relations/produces.md)**: some values from of type [TradedInstrumentIssuanceProcessInformation](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md)

## Annotations

- **label** (en): securities issuance process
- **definition** (en): The process by which a financial security is issued.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
