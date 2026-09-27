---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: traded instrument issuance process information
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Information on one Security issue, arising from the Issuance Process. Note that one Issuance Process (Offering)
      may relate to more than on Issue, which itself may be the issue of more than one Traded Security.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isPartOf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Document
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: traded instrument issuance process information
type: Ontology Class
---

# traded instrument issuance process information

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation>

## Definition

Information on one Security issue, arising from the Issuance Process. Note that one Issuance Process (Offering) may relate to more than on Issue, which itself may be the issue of more than one Traded Security.

## Relationships

- **Subclass of**: [Document](<https://www.omg.org/spec/Commons/Documents/Document>)

## Constraints

- **[isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)**: some values from of type [IssuedSecurityIssueInformation](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation.md)

## Annotations

- **label** (en): traded instrument issuance process information
- **definition** (en): Information on one Security issue, arising from the Issuance Process. Note that one Issuance Process (Offering) may relate to more than on Issue, which itself may be the issue of more than one Traded Security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
