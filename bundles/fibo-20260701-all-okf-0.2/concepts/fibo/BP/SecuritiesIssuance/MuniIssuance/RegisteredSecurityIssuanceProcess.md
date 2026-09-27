---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: registered security issuance process
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Registration
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/includesStep
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/RegisteredSecurityIssuanceProcess
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: registered security issuance process
type: Ontology Class
---

# registered security issuance process

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/RegisteredSecurityIssuanceProcess>

## Relationships

- **Subclass of**: [SecuritiesIssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess.md)

## Constraints

- **[includesStep](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/includesStep.md)**: some values from of type [Registration](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/Registration.md)

## Annotations

- **label** (en): registered security issuance process

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
