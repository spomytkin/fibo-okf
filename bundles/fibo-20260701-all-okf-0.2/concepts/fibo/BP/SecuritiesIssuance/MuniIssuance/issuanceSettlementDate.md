---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issuance settlement date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Settlement date for the initial Issuance transaction.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssuanceSettlement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssuanceSettlement
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/issuanceSettlementDate
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: issuance settlement date
type: Ontology Property
---

# issuance settlement date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/issuanceSettlementDate>

## Definition

Settlement date for the initial Issuance transaction.

## Relationships

- **Domain**: [IssuanceSettlement](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssuanceSettlement.md)
- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label** (en): issuance settlement date
- **definition** (en): Settlement date for the initial Issuance transaction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
