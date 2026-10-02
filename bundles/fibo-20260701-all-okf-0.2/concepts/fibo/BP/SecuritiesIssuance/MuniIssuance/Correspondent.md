---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: correspondent
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A bank, brokerage or other financial institution that is not a direct DTC member. Correspondents rely on direct
      DTC Participants to perform their DTC settlement services
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/participatesIn
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/MuniIssuanceProcessParticipant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/MuniIssuanceProcessParticipant
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Correspondent
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: correspondent
type: Ontology Class
---

# correspondent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Correspondent>

## Definition

A bank, brokerage or other financial institution that is not a direct DTC member. Correspondents rely on direct DTC Participants to perform their DTC settlement services

## Relationships

- **Subclass of**: [MuniIssuanceProcessParticipant](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/MuniIssuanceProcessParticipant.md)
- **Subclass of**: [ContractThirdParty](/concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md)

## Constraints

- **[participatesIn](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/participatesIn.md)**: some values from of type [SecuritiesUnderwritingIssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md)

## Annotations

- **label** (en): correspondent
- **definition** (en): A bank, brokerage or other financial institution that is not a direct DTC member. Correspondents rely on direct DTC Participants to perform their DTC settlement services

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
