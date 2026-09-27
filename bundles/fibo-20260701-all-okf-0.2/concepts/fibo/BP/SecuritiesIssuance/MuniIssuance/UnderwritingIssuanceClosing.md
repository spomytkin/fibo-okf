---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underwriting issuance closing
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/UnderwriterTakedown
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/refersTo
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssuanceClosing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssuanceClosing
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/UnderwritingIssuanceClosing
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: underwriting issuance closing
type: Ontology Class
---

# underwriting issuance closing

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/UnderwritingIssuanceClosing>

## Relationships

- **Subclass of**: [IssuanceClosing](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssuanceClosing.md)

## Constraints

- **[refersTo](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/refersTo.md)**: some values from of type [UnderwriterTakedown](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/UnderwriterTakedown.md)

## Annotations

- **label** (en): underwriting issuance closing

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
