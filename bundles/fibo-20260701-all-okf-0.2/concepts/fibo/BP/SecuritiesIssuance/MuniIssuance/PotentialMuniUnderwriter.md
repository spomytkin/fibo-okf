---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: potential muni underwriter
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An intermediary between an issuer of a security and the investing public. An underwriter can either be DTC Participant
      or Correspondent who would clear the underwriting deal using the Crediting Participant.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/underwrites
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/PotentialUnderwriter.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/PotentialUnderwriter
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/PotentialMuniUnderwriter
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: potential muni underwriter
type: Ontology Class
---

# potential muni underwriter

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/PotentialMuniUnderwriter>

## Definition

An intermediary between an issuer of a security and the investing public. An underwriter can either be DTC Participant or Correspondent who would clear the underwriting deal using the Crediting Participant.

## Relationships

- **Subclass of**: [PotentialUnderwriter](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/PotentialUnderwriter.md)

## Constraints

- **[underwrites](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/underwrites.md)**: some values from of type [SecuritiesUnderwritingIssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md)

## Annotations

- **label** (en): potential muni underwriter
- **definition** (en): An intermediary between an issuer of a security and the investing public. An underwriter can either be DTC Participant or Correspondent who would clear the underwriting deal using the Crediting Participant.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
