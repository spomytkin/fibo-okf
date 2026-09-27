---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: remarketing agent
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/facililtatesRemarketing
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/RemarketingAgent
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: remarketing agent
type: Ontology Class
---

# remarketing agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/RemarketingAgent>

## Constraints

- **[facililtatesRemarketing](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/facililtatesRemarketing.md)**: some values from of type [SecuritiesUnderwritingIssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md)

## Annotations

- **label** (en): remarketing agent

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
